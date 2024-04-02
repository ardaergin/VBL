import markdown
import re

CALLOUT_RE = re.compile(
    r">\[\!(\w+)\](.*?)\n((?:>\s?.*?\n)+)(?=\n[^>]|$)",
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
