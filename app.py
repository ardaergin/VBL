from flask import Flask, render_template, render_template_string, url_for
import markdown
import os
import re

app = Flask(__name__)

NAVIGATION = [
    {
        "title": "Home",
        "pages": [
            {"name": "home", "display": "Home Page"}
        ]
    },
    {
        "title": "Using SONA",
        "pages": [
            {"name": "conduct_study", "display": "Overview of Steps"},
            {"name": "Log_in_to_SONA", "display": "Step 1: Log in"},
            {"name": "Create_a_New_Study", "display": "Step 2: Create a New Study"},
            {"name": "Initial_Study_Verification", "display": "Step 3: Initial Study Verification"},
            {"name": "Initial_Study_Verification", "display": "Step 4: Additional Steps for Physical Studies"}
        ]
    },
    # Add more sections as needed
]

CALLOUT_RE = re.compile(
    r">\[\!(\w+)\]\-(.*?)\n((?:>\s?.*?\n)+)(?=\n[^>]|$)",
    re.MULTILINE | re.DOTALL
)



def preprocess_markdown(md_content):
    def replace(match):
        callout_type = match.group(1).lower()
        title = match.group(2).strip()
        content = match.group(3).strip()

        # Process each line, removing the '>' prefix and converting to HTML
        content_html = markdown.markdown('\n'.join(line.lstrip('> ') for line in content.split('\n')), 
                                         extensions=['extra', 'toc', 'sane_lists', 'smarty'])
        
        toggle_id = f"toggle_{id(content)}"
        return (f'<div class="callout callout-{callout_type}">'
                f'<button onclick="toggleVisibility(\'{toggle_id}\')">'
                f'<span class="callout-title">{title}</span>'
                f'</button>'
                f'<div id="{toggle_id}" class="callout-content" style="display:none;">{content_html}</div>'
                f'</div>')

    # Preprocess callouts
    processed_content = CALLOUT_RE.sub(replace, md_content)
    # Now convert the rest of the markdown which was not in a callout block
    return markdown.markdown(processed_content, extensions=['extra', 'toc', 'sane_lists', 'smarty'])



def markdown_to_html(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        preprocessed_text = preprocess_markdown(text)
        html = markdown.markdown(preprocessed_text, extensions=['extra', 'toc', 'sane_lists', 'smarty'])
    return html

page_hierarchy = {
    "home": 0,

    "Request_a_Physical_Lab_or_Online_Study": {
        "parent": "home", 
        "display": "Overview on Requesting a Study"
        },
    "Create_a_New_Study": {
        "parent": "Request_a_Physical_Lab_or_Online_Study", 
        "display": "Create a New Study"
        },
        "Select_the_Study_Type": {
            "parent": "Create_a_New_Study", 
            "display": "Select the Study Type"
            },
            
        "Fill_in_the_Study_Information": {
            "parent": "Create_a_New_Study", 
            "display": "Fill in the Study Information"
            },

            "Study_Name": {
                "parent": "Fill_in_the_Study_Information", 
                "display": "Study Name"
                },
            "Brief_Abstract": {
                "parent": "Fill_in_the_Study_Information", 
                "display": "Brief Abstract"
                },
            "Detailed_Description": {
                "parent": "Fill_in_the_Study_Information", 
                "display": "Detailed Description"
                },
            "Eligibility_Requirements": {
                "parent": "Fill_in_the_Study_Information", 
                "display": "Eligibility Requirements"
                },
            "Duration": {
                "parent": "Fill_in_the_Study_Information", 
                "display": "Duration"
                },
            "Preparation": {
                "parent": "Fill_in_the_Study_Information", 
                "display": "Preparation"
                },
            "Duration": {
                "parent": "Fill_in_the_Study_Information", 
                "display": "Duration"
                },
            "Ethical_Approval": {
                "parent": "Fill_in_the_Study_Information", 
                "display": "Ethical Approval"
                },
            
}




def build_full_breadcrumb_path(page_hierarchy):
    full_paths = {}

    def build_path(page_name):
        # Base case: if this page is the "home" page or has no parent defined
        if page_hierarchy[page_name] == 0:
            return [{"name": "home", "display": "Home"}]

        page_info = page_hierarchy[page_name]
        parent_path = build_path(page_info["parent"]) if page_info["parent"] in page_hierarchy else []
        current_page_path = {"name": page_name, "display": page_info["display"]}
        return parent_path + [current_page_path]

    for page in page_hierarchy:
        full_paths[page] = build_path(page)

    return full_paths

# Transform the simplified hierarchy into the full breadcrumb paths
full_page_hierarchy = build_full_breadcrumb_path(page_hierarchy)


@app.route('/<page_name>')
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



if __name__ == "__main__":
    app.run(debug=True)

