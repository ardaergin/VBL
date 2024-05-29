import torch
from transformers import AutoTokenizer, AutoModel

def test_model_loading():
    print("Loading model and tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
    model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
    print("Model and tokenizer loaded successfully")

if __name__ == "__main__":
    test_model_loading()
