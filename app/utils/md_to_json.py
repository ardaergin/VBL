import os
import json

def read_markdown_files(directory):
    markdown_files = []
    
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                content = file.read()
                markdown_files.append({
                    "filename": filename,
                    "content": content
                })
    
    return markdown_files

def save_to_json(data):
    with open("markdown_files.json", 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    directory = input("Enter the path to the directory containing markdown files: ")
    
    markdown_files = read_markdown_files(directory)
    save_to_json(markdown_files)
    print(f"Successfully saved markdown files to markdown_files.json")
