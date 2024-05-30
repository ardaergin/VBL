from flask import Blueprint, request, jsonify, render_template
import faiss
import numpy as np
import json
import torch
from transformers import AutoTokenizer, AutoModel
import logging
import gc
import os

os.environ['OMP_NUM_THREADS'] = '1'
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

# Setup logging
logging.basicConfig(level=logging.INFO)

bp = Blueprint('search', __name__)

# Load the embeddings and metadata
embeddings = np.load('embeddings.npy')
with open('metadata.json', 'r', encoding='utf-8') as meta_file:
    metadata = json.load(meta_file)

# Create the FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Determine the appropriate device (GPU if available, otherwise CPU)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load the tokenizer and model with quantization
tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2').to(device)
logging.info("Model and tokenizer loaded successfully on %s", device)

def embed_text(text):
    try:
        inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512).to(device)
        with torch.no_grad():
            outputs = model(**inputs, output_hidden_states=False, output_attentions=False)
            embeddings = outputs.last_hidden_state.mean(dim=1).detach().cpu().numpy()
        # Clear GPU memory
        gc.collect()
        torch.cuda.empty_cache()
        return embeddings
    except Exception as e:
        logging.error("Error during text embedding: %s", e)
        raise

from flask import redirect, url_for, session

import uuid
import os
import json

@bp.route('/search', methods=['GET', 'POST'])
def search():
    try:
        if request.method == 'POST':
            query = request.json.get('query')
        else:
            query = request.args.get('query')
        logging.info("Received query: %s", query)

        if not isinstance(query, str) or not query.strip():
            logging.error("Invalid input: %s", query)
            return jsonify({"error": "Invalid input"}), 400

        query_embedding = embed_text(query).reshape(1, -1)
        logging.info("Query embedding created successfully")

        distances, indices = index.search(query_embedding, k=5)
        logging.info("Search completed. Distances: %s, Indices: %s", distances, indices)

        results = [metadata[idx] for idx in indices[0]]
        for result in results:
            result['title'] = result['filename'].replace('.md', '').replace('-', ' ').capitalize()
        logging.info("Search results: %s", results)

        # Generate a unique ID for the search results
        search_id = str(uuid.uuid4())
        search_results_path = os.path.join('/tmp/flask_session/', f'{search_id}.json')

        # Save results to a file
        with open(search_results_path, 'w', encoding='utf-8') as f:
            json.dump({'query': query, 'results': results}, f)

        # Store only the reference (unique ID) in the session
        session['search_id'] = search_id

        return redirect(url_for('search.results_page'))
    except Exception as e:
        logging.error("Error during search: %s", e)
        return jsonify({"error": "An error occurred during the search process"}), 500
@bp.route('/results', methods=['GET'])
def results_page():
    search_id = session.get('search_id')
    if not search_id:
        return "No search results found.", 404

    search_results_path = os.path.join('/tmp/flask_session/', f'{search_id}.json')
    if not os.path.exists(search_results_path):
        return "Search results file not found.", 404

    with open(search_results_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    query = data.get('query', '')
    results = data.get('results', [])

    return render_template('search_results.html', query=query, results=results)
