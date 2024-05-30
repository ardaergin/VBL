import faiss
import numpy as np
import json
from search.nlp import generate_embeddings

def load_embeddings(file_path):
    return np.load(file_path)

def create_faiss_index(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index

def search_index(query_embedding, index, k=5):
    distances, indices = index.search(query_embedding, k)
    return distances, indices

def main():
    embeddings_path = 'embeddings.npy'
    metadata_path = 'metadata.json'
    
    embeddings = load_embeddings(embeddings_path)
    index = create_faiss_index(embeddings)
    
    with open(metadata_path, 'r', encoding='utf-8') as meta_file:
        metadata = json.load(meta_file)
    
    # Example query
    query = "Your search query here"
    query_embedding = generate_embeddings([query])
    
    distances, indices = search_index(query_embedding, index, k=5)
    
    results = [metadata[idx] for idx in indices[0]]
    for result in results:
        print(result['filename'], result['content'][:200])  # Print first 200 characters of content

if __name__ == "__main__":
    main()
