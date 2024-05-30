import numpy as np
import faiss
import torch
from transformers import AutoTokenizer, AutoModel
import os
import logging
import json
import gc

os.environ['OMP_NUM_THREADS'] = '1'
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

# Determine the appropriate device (GPU if available, otherwise CPU)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2').to(device)
logging.info("Model and tokenizer loaded successfully on %s", device)

def load_embeddings_metadata():
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data')
    embeddings = np.load(os.path.join(data_path, 'embeddings.npy'))
    with open(os.path.join(data_path, 'metadata.json'), 'r', encoding='utf-8') as meta_file:
        metadata = json.load(meta_file)
    return embeddings, metadata

def create_faiss_index(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index

def embed_text(text):
    try:
        inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512).to(device)
        with torch.no_grad():
            outputs = model(**inputs, output_hidden_states=False, output_attentions=False)
            embeddings = outputs.last_hidden_state.mean(dim=1).detach().cpu().numpy()
        gc.collect()
        torch.cuda.empty_cache()
        return embeddings
    except Exception as e:
        logging.error("Error during text embedding: %s", e)
        raise
