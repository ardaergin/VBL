import numpy as np
import faiss
import torch
from transformers import AutoTokenizer, AutoModel
import os
import logging
import json
import gc
# Some Debugging after "segmentation fault" error:
os.environ['OMP_NUM_THREADS'] = '1'
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

# Determine the appropriate device (GPU if available, otherwise CPU)
# This was necessary because of memory issues
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load the tokenizer and model for embedding text
tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2').to(device)
logging.info("Model and tokenizer loaded successfully on %s", device)

def load_embeddings_metadata():
    """
    Load embeddings and metadata from the data directory.

    This function loads the precomputed embeddings and associated metadata from the 'data' directory.

    :return: A tuple containing the embeddings and metadata.
    """
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data')
    embeddings = np.load(os.path.join(data_path, 'embeddings.npy'))
    with open(os.path.join(data_path, 'metadata.json'), 'r', encoding='utf-8') as meta_file:
        metadata = json.load(meta_file)
    return embeddings, metadata

def create_faiss_index(embeddings):
    """
    Create a FAISS index from the provided embeddings.

    This function initializes a FAISS index and adds the embeddings to it.

    :param embeddings: The embeddings to add to the index.
    :return: The created FAISS index.
    """
    dimension = embeddings.shape[1]  # Determine the dimensionality of the embeddings
    index = faiss.IndexFlatL2(dimension)  # Create a flat L2 distance index
    index.add(embeddings)  # Add the embeddings to the index
    return index

def embed_text(text):
    """
    Embed the given text using the preloaded model and tokenizer.

    This function converts the input text into an embedding vector using the loaded model.

    :param text: The input text to embed.
    :return: The embedding vector for the input text.
    """
    try:
        # Tokenize and prepare the text for the model
        inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512).to(device)
        with torch.no_grad():
            # Generate embeddings using the model
            outputs = model(**inputs, output_hidden_states=False, output_attentions=False)
            embeddings = outputs.last_hidden_state.mean(dim=1).detach().cpu().numpy()
        # Clear GPU memory
        gc.collect()
        torch.cuda.empty_cache()
        return embeddings
    except Exception as e:
        logging.error("Error during text embedding: %s", e)
        raise
