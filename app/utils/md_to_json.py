import os
import json

def read_markdown_files(directory):
    """
    Read all markdown files in the specified directory and return their content.

    This function iterates through the given directory, reads the content of each
    markdown file, and stores the filename and content in a list of dictionaries.

    :param directory: The directory containing markdown files.
    :return: A list of dictionaries, each containing the filename and content of a markdown file.
    """
    markdown_files = []
    
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file has a .md extension
        if filename.endswith(".md"):
            # Read the content of the markdown file
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                content = file.read()
                # Append the filename and content to the list
                markdown_files.append({
                    "filename": filename,
                    "content": content
                })
    
    return markdown_files

def save_to_json(data):
    """
    Save the given data to a JSON file.

    This function writes the provided data to a JSON file named 'markdown_files.json'.

    :param data: The data to be saved in JSON format.
    """
    # Write the data to 'markdown_files.json' with an indentation of 4 spaces
    with open("markdown_files.json", 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    # Prompt the user to enter the directory path containing markdown files
    directory = input("Enter the path to the directory containing markdown files: ")
    
    # Read markdown files from the specified directory
    markdown_files = read_markdown_files(directory)
    
    # Save the read markdown files to a JSON file
    save_to_json(markdown_files)
    
    print(f"Successfully saved markdown files to markdown_files.json")
