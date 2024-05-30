from flask import Blueprint, render_template, request
from whoosh import index
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser
import os
import markdown
from utils.navigation import NAVIGATION

bp = Blueprint('search', __name__)

schema = Schema(title=TEXT(stored=True), content=TEXT, path=ID(stored=True))
index_dir = os.path.join(os.getcwd(), "index")
if not os.path.exists(index_dir):
    os.mkdir(index_dir)
    ix = index.create_in(index_dir, schema)

    writer = ix.writer()
    for filename in os.listdir('markdown_files'):
        if filename.endswith('.md'):
            file_path = os.path.join('markdown_files', filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
                html = markdown.markdown(text)
                title = filename.replace('_', ' ').replace('.md', '').capitalize()
                writer.add_document(title=title, content=html, path=filename)
    writer.commit()
else:
    ix = index.open_dir(index_dir)

@bp.route('/search', methods=['GET'])
def search():
    query_str = request.args.get('q', '')
    parser = QueryParser("content", ix.schema)
    query = parser.parse(query_str)
    results = []
    with ix.searcher() as searcher:
        result_docs = searcher.search(query, limit=None)
        for result in result_docs:
            results.append({'title': result['title'], 'filename': result['path']})
    return render_template(
        'search_results.html', 
        query=query_str, 
        results=results, 
        navigation=NAVIGATION, 
        breadcrumb_path=[{"name": "home", "display": "Home"}])