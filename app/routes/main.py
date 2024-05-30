from flask import Blueprint, render_template, request
import os
from app.utils import markdown_to_html
from app.utils import NAVIGATION, full_page_hierarchy

bp = Blueprint('main', __name__)

@bp.route('/<page_name>')
def show_page(page_name):
    file_path = os.path.join('markdown_files', f'{page_name}.md')
    if os.path.exists(file_path):
        content = markdown_to_html(file_path)
        title = page_name.replace('_', ' ').capitalize()
        # Get the breadcrumb path for the current page, defaulting to just Home if not defined
        breadcrumb_path = full_page_hierarchy.get(page_name, [{"name": "home", "display": "Home"}])
        return render_template('base.html', content=content, title=title, navigation=NAVIGATION, breadcrumb_path=breadcrumb_path)
    else:
        return "Page not found", 404
