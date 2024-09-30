import markdown
import re
from jinja2 import Template
from flask import url_for

# Existing regex for callouts
CALLOUT_RE = re.compile(
    r">\[\!(\w+)\](.*?)\n((?:>\s?.*?\n)+)(?=\n[^>]|$)",
    re.MULTILINE | re.DOTALL
)

# New regex for video embedding
VIDEO_RE = re.compile(r'\[video\]\((.*?)\)')

def preprocess_markdown(md_content):
    def replace_callout(match):
        callout_type = match.group(1).lower()
        title = match.group(2).strip()
        content = match.group(3).strip()

        content_html = markdown.markdown(
            '\n'.join(line.lstrip('> ') for line in content.split('\n')), 
            extensions=['extra', 'toc', 'sane_lists', 'smarty']
        )
        
        toggle_id = f"toggle_{id(content)}"
        return (f'<div class="callout callout-{callout_type}">'
                f'<button onclick="toggleVisibility(\'{toggle_id}\')" aria-expanded="false">'
                f'<span class="callout-title">{title}</span>'
                f'</button>'
                f'<div id="{toggle_id}" class="callout-content">{content_html}</div>'
                f'</div>')


    def replace_video(match):
        video_url = match.group(1)
        # Assuming the poster image has the same name as the video but with a '.jpg' extension
        poster_url = video_url.replace('.mp4', '.jpg')  # Adjust this logic as needed for your project
        
        video_tag = (
            f'<div class="embed-responsive embed-responsive-16by9">'
            f'<video controls class="embed-responsive-item" poster="{poster_url}">'
            f'<source src="{video_url}" type="video/mp4">'
            f'Your browser does not support the video tag.'
            f'</video>'
            f'</div>'
        )
        return video_tag

    # Preprocess callouts and videos
    processed_content = CALLOUT_RE.sub(replace_callout, md_content)
    processed_content = VIDEO_RE.sub(replace_video, processed_content)

    return processed_content

def adjust_links(html_content):
    """Adjust links that should be standalone instead of within the step paths."""
    
    # Define the regex pattern for relative links (not starting with 'http' or '/')
    pattern = r'href="([^http|/][^"]*)"'

    # Function to replace the matched link with the standalone version
    def replace_link(match):
        relative_link = match.group(1)
        # Convert the relative link to a standalone format using Flask's `url_for`
        standalone_url = url_for('main.show_page', page_name=relative_link)
        return f'href="{standalone_url}"'

    # Use re.sub to replace all the matching links in the HTML content
    adjusted_html = re.sub(pattern, replace_link, html_content)

    return adjusted_html

def render_markdown_with_context(file_path, context):
    """Render the markdown file with the given context (like faculty, study_type, assistant_status)."""
    with open(file_path, 'r', encoding='utf-8') as f:
        template = Template(f.read())

        # Render the markdown file with the given context (faculty, study_type, etc.)
        rendered_content = template.render(context)
        
        # Preprocess callouts and videos within the rendered content
        preprocessed_content = preprocess_markdown(rendered_content)

        # Convert the rendered markdown content to HTML
        html_content = markdown.markdown(preprocessed_content, extensions=['extra', 'toc', 'sane_lists', 'smarty'])

        # Adjust the links to point to standalone pages where necessary
        html_content = adjust_links(html_content)

    return html_content
