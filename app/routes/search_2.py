from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session
import os
import json
import logging
import uuid
from app.services.embedding_service import embed_text, create_faiss_index, load_embeddings_metadata
import gc

bp = Blueprint('search', __name__)

# Setup logging
logging.basicConfig(level=logging.INFO)

# Load the embeddings and metadata
embeddings, metadata = load_embeddings_metadata()
index = create_faiss_index(embeddings)

@bp.route('/search', methods=['GET', 'POST'])
def search():
    try:
        query = request.json.get('query') if request.method == 'POST' else request.args.get('query')
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

        search_id = str(uuid.uuid4())
        search_results_path = os.path.join('/tmp/flask_session/', f'{search_id}.json')

        with open(search_results_path, 'w', encoding='utf-8') as f:
            json.dump({'query': query, 'results': results}, f)

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
