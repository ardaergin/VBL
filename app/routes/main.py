from flask import Blueprint, render_template, request, redirect, url_for
import os
from app.utils import render_markdown_with_context
from app.utils import NAVIGATION, full_page_hierarchy
from app.utils import step_1, step_2, step_3

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return redirect(url_for('main.show_page', page_name='home'))

# Standalone route (e.g., /create-a-new-study)
@bp.route('/<page_name>')
def show_page(page_name):
    standalone_file_path = os.path.join('markdown_files', f'{page_name}.md')
    if os.path.exists(standalone_file_path):
        content = render_markdown_with_context(standalone_file_path, {})  # Empty context for standalone pages
        title = page_name.replace('_', ' ').capitalize()
        breadcrumb_path = full_page_hierarchy.get(page_name, [{"name": "home", "display": "Home"}])
        return render_template(
            'base.html', 
            content=content, 
            title=title, 
            navigation=NAVIGATION, 
            breadcrumb_path=breadcrumb_path)
    else:
        return "Page not found", 404

@bp.route('/step-<int:step>/<faculty>/<study_type>/<assistant_status>/<page_name>')
def show_step(step, faculty, study_type, assistant_status, page_name):
    """
    Handle both online and lab studies, using the 'assistant_status' 
    as a placeholder for online studies (e.g., '/n/').
    """
    file_path = os.path.join('markdown_files', f'{page_name}.md')

    if os.path.exists(file_path):
        # Prepare the context to be passed to the markdown file
        context = {
            'faculty': faculty,
            'study_type': study_type,
            'assistant_status': assistant_status
        }

        content = render_markdown_with_context(file_path, context)
        title = page_name.replace('_', ' ').capitalize()

        # Dynamically get the step data (step_1, step_2, etc.)
        step_data = {
            1: step_1,
            2: step_2,
            3: step_3,
        }.get(step)

        if not step_data:
            return "Step not found", 404

        # Construct the key based on faculty, study type, and assistant status
        key = f"{faculty}-{study_type}-{assistant_status}"

        # Check if the page exists for the specific path
        if key not in step_data or page_name not in step_data[key]:
            return "Page not found", 404

        # Get the current, previous, and next steps
        current_index = step_data[key].index(page_name)
        total_steps = len(step_data[key])
        current_step = current_index + 1
        progress = (current_step / total_steps) * 100

        previous_page = step_data[key][current_index - 1] if current_index > 0 else None
        next_page = step_data[key][current_index + 1] if current_index < total_steps - 1 else None

        return render_template(
            'step_base.html',
            content=content,
            title=title,
            navigation=NAVIGATION,
            current_step=current_step,
            total_steps=total_steps,
            progress=progress,
            previous_page=previous_page,
            next_page=next_page,
            step=step,
            faculty=faculty,  # Pass the faculty
            study_type=study_type,  # Pass the study type
            assistant_status=assistant_status,  # Pass the assistant status (even if it's 'n' for online)
            breadcrumb_path=full_page_hierarchy.get(step, [{"name": "home", "display": "Home"}])
        )
    else:
        return "Page not found", 404


@bp.route('/researcher-account')
def researcher_account():
    return render_template(
        'researcher_account.html',
        navigation=NAVIGATION,
        breadcrumb_path=full_page_hierarchy.get("account-check", [{"name": "home", "display": "Home"}])
    )


@bp.route('/researcher-overview')
def researcher_overview():
    return render_template(
        'researcher_overview.html',
        navigation=NAVIGATION,
        breadcrumb_path=full_page_hierarchy.get("account-check", [{"name": "home", "display": "Home"}])
    )
