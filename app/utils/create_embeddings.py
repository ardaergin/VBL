import json
import torch
from transformers import AutoTokenizer, AutoModel
import numpy as np

def load_json_file(file_path):
    """
    Load data from a JSON file.

    :param file_path: Path to the JSON file.
    :return: Parsed JSON data as a Python dictionary.
    """
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


def generate_embeddings(texts, model_name='sentence-transformers/all-MiniLM-L6-v2'):
    """
    Generate embeddings for a list of texts using a pre-trained model.

    :param texts: List of texts to be embedded.
    :param model_name: Name of the pre-trained model to use.
    :return: Numpy array of embeddings.
    """
    # This was necessary because of memory issues
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # Load the tokenizer and model for embedding text
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name).to(device)
    
    def embed_text(text):
        """
        Embed a single text using the pre-trained model.

        :param text: Text to be embedded.
        :return: Embedding vector as a numpy array.
        """
        inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
        with torch.no_grad():
            embeddings = model(**inputs).last_hidden_state.mean(dim=1).squeeze().cpu().numpy()
        return embeddings
    
    embeddings = [embed_text(text) for text in texts]
    return np.array(embeddings)

def main():
    """
    Main function to load markdown data, generate embeddings, and save the results.

    This function loads markdown content from a JSON file, generates embeddings using a pre-trained model,
    and saves the embeddings and metadata to separate files.
    """
    # Path to the JSON file containing markdown content
    json_file_path = 'markdown_files.json'
    
    # Load the JSON data
    data = load_json_file(json_file_path)
    
    # Extract the text content from the data
    texts = [item['content'] for item in data]
    
    # Generate embeddings for the texts
    embeddings = generate_embeddings(texts)
    
    # Save the embeddings to a .npy file
    np.save('embeddings.npy', embeddings)
    
    # Save the metadata to a JSON file
    with open('metadata.json', 'w', encoding='utf-8') as meta_file:
        json.dump(data, meta_file)
    
    print("Embeddings and metadata saved successfully.")

if __name__ == "__main__":
    main()
