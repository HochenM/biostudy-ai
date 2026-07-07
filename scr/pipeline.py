from ingest import extract_text_from_pdf
from chunking import clean_text,  split_into_sentences, create_chunks
from embeddings import get_embeddings
from vectorstore import VectorStore
from llm import generate_answer

class RAGPipeline:
    def __init__(self,pdf):
        self.pdf = pdf

        self.chunk = []
        self.embeddings = None
        self.vectorstore = None


    def build(self):
        text = extract_text_from_pdf(self.pdf)
        text = clean_text(text)
        sentences = split_into_sentences(text)

        self.chunk = create_chunks(sentences)

        self.embeddings = get_embeddings(self.chunk)

        self.vectorstore = VectorStore(len(self.embeddings[0]))

        self.vectorstore.add(self.embeddings,self.chunk)


    def search(self,question,k=2):

        query_embedding = get_embeddings([question])[0]
        results = self.vectorstore.search(
        query_embedding,
        k
    )
        return results

    def ask(self, question):

      chunks = self.search(question)

      context = "\n".join(chunks)

      answer = generate_answer(
        context,
        question
    )
      return answer



