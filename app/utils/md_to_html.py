import markdown
import re

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
                f'<button onclick="toggleVisibility(\'{toggle_id}\')">'
                f'<span class="callout-title">{title}</span>'
                f'</button>'
                f'<div id="{toggle_id}" class="callout-content" style="display:none;">{content_html}</div>'
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

def markdown_to_html(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        preprocessed_text = preprocess_markdown(text)
        html = markdown.markdown(preprocessed_text, extensions=['extra', 'toc', 'sane_lists', 'smarty'])
    return html
