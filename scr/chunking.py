import re

def clean_text(text):
    text = text.replace("\n", " ")
    text = text.replace("•", "")
    text = text.replace("→", " to ")

    # normalize spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def split_into_sentences(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)

    return [
        s.strip()
        for s in sentences
        if len(s.split()) >= 4
    ]


def create_chunks(sentences, chunk_size=5, overlap=2):
    chunks = []

    i = 0

    while i < len(sentences):
        chunk = sentences[i:i + chunk_size]
        chunks.append(" ".join(chunk))
        i += chunk_size - overlap

    return chunks
