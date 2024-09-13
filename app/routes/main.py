from flask import Blueprint, render_template, request, redirect, url_for
import os
from app.utils import markdown_to_html
from app.utils import NAVIGATION, full_page_hierarchy
from app.utils import step_1, step_2, step_3, step_4

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return redirect(url_for('main.show_page', page_name='home'))

# Standalone route (e.g., /create-a-new-study)
@bp.route('/<page_name>')
def show_page(page_name):
    standalone_file_path = os.path.join('markdown_files', f'{page_name}.md')
    if os.path.exists(standalone_file_path):
        content = markdown_to_html(standalone_file_path)
        title = page_name.replace('_', ' ').capitalize()
        breadcrumb_path = full_page_hierarchy.get(page_name, [{"name": "home", "display": "Home"}])
        return render_template('base.html', content=content, title=title, navigation=NAVIGATION, breadcrumb_path=breadcrumb_path)
    else:
        return "Page not found", 404

# Step-based route for all steps (e.g., /step-1/Online/overview)
@bp.route('/step-<int:step>/<path_type>/<page_name>')
def show_step(step, path_type, page_name):
    """
    Show the step pages based on the step number (1, 2, 3, 4) and path type (either 'Online' or 'Lab').
    """
    file_path = os.path.join('markdown_files', f'{page_name}.md')
    
    if os.path.exists(file_path):
        content = markdown_to_html(file_path)
        title = page_name.replace('_', ' ').capitalize()

        # Dynamically get the step dictionary (step_1, step_2, etc.)
        step_data = {
            1: step_1,
            2: step_2,
            3: step_3,
            4: step_4
        }.get(step)

        if not step_data:
            return "Step not found", 404

        # Choose the correct path (Online or Lab)
        manual_order = step_data.get(path_type)

        if not manual_order or page_name not in manual_order:
            return "Page not found", 404

        # Determine the current, previous, and next steps
        current_index = manual_order.index(page_name)
        total_steps = len(manual_order)
        current_step = current_index + 1
        progress = (current_step / total_steps) * 100

        previous_page = manual_order[current_index - 1] if current_index > 0 else None
        next_page = manual_order[current_index + 1] if current_index < total_steps - 1 else None

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
            step=step,  # Pass the current step to the template for navigation
            path_type=path_type  # Pass the path type to the template for navigation
        )
    else:
        return "Page not found", 404
