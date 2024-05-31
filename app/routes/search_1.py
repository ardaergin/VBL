from flask import Blueprint, render_template, request
from whoosh import index
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser
import os
import markdown
from app.utils import NAVIGATION

# Defining a Blueprint for the search functionality
bp = Blueprint('search', __name__)

# Defining the schema for the Whoosh index
schema = Schema(title=TEXT(stored=True), content=TEXT, path=ID(stored=True))

# Specifying the directory to store the Whoosh index
index_dir = os.path.join(os.getcwd(), "index")

# If the index directory does not exist, create it and index the markdown files
if not os.path.exists(index_dir):
    os.mkdir(index_dir)  # Create the directory
    ix = index.create_in(index_dir, schema)  # Create the index

    # Create a writer to add documents to the index
    writer = ix.writer()
    # Iterate over markdown files in the 'markdown_files' directory
    for filename in os.listdir('markdown_files'):
        if filename.endswith('.md'):
            file_path = os.path.join('markdown_files', filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()  # Read the content of the markdown file
                html = markdown.markdown(text)  # Convert markdown to HTML
                title = filename.replace('_', ' ').replace('.md', '').capitalize()  # Generate a title
                # Add the document to the index
                writer.add_document(title=title, content=html, path=filename)
    writer.commit()  # Commit the changes to the index
else:
    ix = index.open_dir(index_dir)  # Open the existing index

@bp.route('/search', methods=['GET'])
def search():
    """
    Handle search requests and render search results.

    This route handles GET requests to perform a search on the indexed markdown files.
    It parses the query, performs the search, and renders the search results page.

    :return: Rendered template of search results.
    """
    query_str = request.args.get('q', '')  # Get the search query from the request parameters
    parser = QueryParser("content", ix.schema)  # Create a query parser for the 'content' field
    query = parser.parse(query_str)  # Parse the query string
    results = []  # List to store the search results

    # Perform the search using the index searcher
    with ix.searcher() as searcher:
        result_docs = searcher.search(query, limit=None)  # Execute the search query
        # Collect the results
        for result in result_docs:
            results.append({'title': result['title'], 'filename': result['path']})

    # Render the search results template
    return render_template(
        'search_results.html', 
        query=query_str, 
        results=results, 
        navigation=NAVIGATION, 
        breadcrumb_path=[{"name": "home", "display": "Home"}]
    )
