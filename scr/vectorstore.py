import faiss
import numpy as np


class VectorStore:
    def __init__(self, dimension):
        self.index = faiss.IndexFlatL2(dimension)
        self.texts = []

    def add(self, embeddings, texts):
        embeddings = np.asarray(embeddings).astype("float32")
        self.index.add(embeddings)
        self.texts.extend(texts)

    def search(self, query_embedding, k=3):
        query_embedding = np.array([query_embedding]).astype("float32")

        distances, indices = self.index.search(query_embedding, k)

        results = []
        for i in indices[0]:
            if i != -1:
                results.append(self.texts[i])

        return results
