from sentence_transformers import SentenceTransformer

# load model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embeddings(text_list):
    embeddings = model.encode(text_list)
    return embeddings
