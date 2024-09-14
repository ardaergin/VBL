import markdown
import re
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
        video_tag = (
            f'<div class="embed-responsive embed-responsive-16by9">'
            f'<video controls class="embed-responsive-item">'
            f'<source src="{video_url}" type="video/mp4">'
            f'Your browser does not support the video tag.'
            f'</video>'
            f'</div>'
        )
        return video_tag

    # Preprocess callouts and videos
    processed_content = CALLOUT_RE.sub(replace_callout, md_content)
    processed_content = VIDEO_RE.sub(replace_video, processed_content)

    return markdown.markdown(processed_content, extensions=['extra', 'toc', 'sane_lists', 'smarty'])

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

def markdown_to_html(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        preprocessed_text = preprocess_markdown(text)
        html = markdown.markdown(preprocessed_text, extensions=['extra', 'toc', 'sane_lists', 'smarty'])

        # Adjust the links to point to standalone pages where necessary
        html = adjust_links(html)
    return html
