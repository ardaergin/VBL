import numpy as np
import faiss
import os
import logging
import json
from app.utils import initialize_model_and_tokenizer, embed_text

# Some Debugging after "segmentation fault" error:
os.environ['OMP_NUM_THREADS'] = '1'
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

# Initialize the tokenizer and model for embedding text
tokenizer, model, device = initialize_model_and_tokenizer()
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
