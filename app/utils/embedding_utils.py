import torch
from transformers import AutoTokenizer, AutoModel
import gc

def initialize_model_and_tokenizer(model_name='sentence-transformers/all-MiniLM-L6-v2'):
    """
    Initialize the model and tokenizer.

    :param model_name: Name of the pre-trained model to use.
    :param device: The device to load the model on (default: auto-detect GPU if available).
    :return: tokenizer, model, and device
    """

    # Determine the appropriate device (GPU if available, otherwise CPU)
    # This was necessary because of memory issues
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # Load the tokenizer and model for embedding text
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name).to(device)
    return tokenizer, model, device

def embed_text(text, tokenizer, model, device):
    """
    Embed the given text using the preloaded model and tokenizer.

    This function converts the input text into an embedding vector using the loaded model.

    :param text: The input text to embed.
    :param tokenizer: The tokenizer to use for encoding the text.
    :param model: The pre-trained model to generate embeddings.
    :param device: The device to perform the computation on.
    :return: The embedding vector for the input text.
    """
    try:
        # Tokenize and prepare the text for the model
        inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512).to(device)
        with torch.no_grad():
            # Generate embeddings using the model
            outputs = model(**inputs)
            embeddings = outputs.last_hidden_state.mean(dim=1).detach().cpu().numpy()
        # Clear GPU memory
        gc.collect()
        torch.cuda.empty_cache()
        return embeddings
    
    except Exception as e:
        raise RuntimeError(f"Error during text embedding: {e}")
