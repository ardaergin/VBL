from flask import Flask, render_template, render_template_string, url_for
import markdown
import os

app = Flask(__name__)

def markdown_to_html(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        # Enable the 'extra' extension to allow for markdown features like tables and fenced code blocks
        # You can also add 'sane_lists' and 'smarty' for more functionalities
        html = markdown.markdown(text, extensions=['extra', 'toc', 'sane_lists', 'smarty'])
    return html

@app.route('/<page_name>')
def show_page(page_name):
    file_path = os.path.join('markdown_files', f'{page_name}.md')
    if os.path.exists(file_path):
        md = markdown.Markdown(extensions=['extra', 'toc', 'sane_lists', 'smarty'])
        with open(file_path, 'r', encoding='utf-8') as f:
            content = md.convert(f.read())
        toc = md.toc
        # Ensure that 'base.html' is the name of your base template file.
        return render_template('base.html', content=content, toc=toc, title=page_name.capitalize())
    else:
        return "Page not found", 404


if __name__ == "__main__":
    app.run(debug=True)