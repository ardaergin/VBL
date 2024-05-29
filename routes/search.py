from flask import Blueprint, request, jsonify
import faiss
import numpy as np
import json
import torch
from transformers import AutoTokenizer, AutoModel

bp = Blueprint('search', __name__)

# Load the embeddings and metadata
embeddings = np.load('embeddings.npy')
with open('metadata.json', 'r', encoding='utf-8') as meta_file:
    metadata = json.load(meta_file)

# Create the FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Load the tokenizer and model for generating query embeddings
tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')

def embed_text(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        embeddings = model(**inputs).last_hidden_state.mean(dim=1).squeeze().cpu().numpy()
    return embeddings

@bp.route('/search', methods=['POST'])
def search():
    query = request.json.get('query')
    query_embedding = embed_text(query).reshape(1, -1)
    distances, indices = index.search(query_embedding, k=5)
    
    results = [metadata[idx] for idx in indices[0]]
    return jsonify(results)
