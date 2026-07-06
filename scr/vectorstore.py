import faiss
import numpy as np
class VectorStore:
    def __init__(self, dimension):
        self.index = faiss.IndexFlatL2(dimension)
        self.texts=[]

    def add(self, embedding,texts):
        embeddings = np.asarray(embedding).astype('float32')
        self.index.add(embeddings)
        self.texts.extend(texts)

    def search(self, query_embedding, k=3):
        query_embedding = np.array([query_embedding]).astype("float32") #[] for 2D
        distances, indices = self.index.search(query_embedding, k)

        results = [self.texts[i] for i in indices[0]]
        return results




