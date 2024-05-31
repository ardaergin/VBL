from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session
import os
import json
import logging
import uuid
from app.services.embedding_service import embed_text, create_faiss_index, load_embeddings_metadata
import gc

# Define a Blueprint for the search functionality
bp = Blueprint('search', __name__)

# Setup logging to record information and errors
logging.basicConfig(level=logging.INFO)

# Load the embeddings and metadata from files
embeddings, metadata = load_embeddings_metadata()

# Create the FAISS index using the loaded embeddings
index = create_faiss_index(embeddings)

@bp.route('/search', methods=['GET', 'POST'])
def search():
    """
    Handle search requests and return search results.

    This route handles both GET and POST requests to perform a search using the FAISS index.
    It embeds the query text, performs the search, and redirects to the results page.

    :return: A redirect to the results page or a JSON response with an error message.
    """
    try:
        # Get the search query from the request
        query = request.json.get('query') if request.method == 'POST' else request.args.get('query')
        logging.info("Received query: %s", query)

        # Validate the query
        if not isinstance(query, str) or not query.strip():
            logging.error("Invalid input: %s", query)
            return jsonify({"error": "Invalid input"}), 400

        # Embed the query text
        query_embedding = embed_text(query).reshape(1, -1)
        logging.info("Query embedding created successfully")

        # Perform the search using the FAISS index
        distances, indices = index.search(query_embedding, k=5)
        logging.info("Search completed. Distances: %s, Indices: %s", distances, indices)

        # Retrieve the search results using the indices
        results = [metadata[idx] for idx in indices[0]]
        for result in results:
            result['title'] = result['filename'].replace('.md', '').replace('-', ' ').capitalize()
        logging.info("Search results: %s", results)

        # Generate a unique ID for the search results
        search_id = str(uuid.uuid4())
        search_results_path = os.path.join('/tmp/flask_session/', f'{search_id}.json')

        # Save the search results to a file
        with open(search_results_path, 'w', encoding='utf-8') as f:
            json.dump({'query': query, 'results': results}, f)

        # Store the search ID in the session
        session['search_id'] = search_id

        # Redirect to the results page
        return redirect(url_for('search.results_page'))
    except Exception as e:
        logging.error("Error during search: %s", e)
        return jsonify({"error": "An error occurred during the search process"}), 500

@bp.route('/results', methods=['GET'])
def results_page():
    """
    Render the search results page.

    This route handles GET requests to display the search results stored in the session.

    :return: Rendered template of search results or a 404 error message.
    """
    # Retrieve the search ID from the session
    search_id = session.get('search_id')
    if not search_id:
        return "No search results found.", 404

    # Construct the path to the search results file
    search_results_path = os.path.join('/tmp/flask_session/', f'{search_id}.json')
    if not os.path.exists(search_results_path):
        return "Search results file not found.", 404

    # Load the search results from the file
    with open(search_results_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Extract the query and results from the data
    query = data.get('query', '')
    results = data.get('results', [])

    # Render the search results template
    return render_template('search_results.html', query=query, results=results)
