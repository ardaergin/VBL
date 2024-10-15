from flask import Blueprint, render_template, redirect, url_for
import os
from app.utils import render_markdown_with_context
from app.utils import NAVIGATION, full_page_hierarchy


bp = Blueprint('main', __name__)


# Landing page
@bp.route('/')
def index():
    return render_template('landing.html')


@bp.route('/home')
def home():
    return redirect(url_for('main.index'))


# Standalone route (e.g., /create-a-new-study)
@bp.route('/<page_name>')
def show_page(page_name):
    standalone_file_path = os.path.join('markdown_files', f'{page_name}.md')
    if os.path.exists(standalone_file_path):
        # Use render_markdown_with_context to get both the content and YAML data
        content, yaml_data = render_markdown_with_context(standalone_file_path, {})

        # Get the title from YAML if it exists, otherwise fallback to page name
        title = yaml_data.get('name', page_name.replace('_', ' ').capitalize())

        # Build the breadcrumb path using the full_page_hierarchy or fallback to default
        breadcrumb_path = full_page_hierarchy.get(page_name, [{"name": "home", "display": "Home"}])

        return render_template(
            'base.html',
            content=content,
            title=title,
            navigation=NAVIGATION,
            breadcrumb_path=breadcrumb_path
        )
    else:
        return "Page not found", 404
