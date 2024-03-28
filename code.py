from flask import Flask, render_template_string
import markdown
import os

app = Flask(__name__)

def markdown_to_html(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        html = markdown.markdown(text)
    return html

@app.route('/<page_name>')
def show_page(page_name):
    file_path = os.path.join('markdown_files', f'{page_name}.md')
    if os.path.exists(file_path):
        content = markdown_to_html(file_path)
        return render_template_string(content)
    else:
        return "Page not found", 404

if __name__ == "__main__":
    app.run(debug=True)
