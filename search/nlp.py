import json
import torch
from transformers import AutoTokenizer, AutoModel
import numpy as np

def load_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data

def generate_embeddings(texts, model_name='sentence-transformers/all-MiniLM-L6-v2'):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    
    def embed_text(text):
        inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
        with torch.no_grad():
            embeddings = model(**inputs).last_hidden_state.mean(dim=1).squeeze().cpu().numpy()
        return embeddings
    
    embeddings = [embed_text(text) for text in texts]
    return np.array(embeddings)

def main():
    json_file_path = 'markdown_files.json'
    data = load_json_file(json_file_path)
    
    texts = [item['content'] for item in data]
    embeddings = generate_embeddings(texts)
    
    np.save('embeddings.npy', embeddings)
    with open('metadata.json', 'w', encoding='utf-8') as meta_file:
        json.dump(data, meta_file)
    
    print("Embeddings and metadata saved successfully.")

if __name__ == "__main__":
    main()
