import re

def clean_text(text):
    # 1. remove newlines
    text = text.replace("\n", " ")

    # 2. remove numbering like 1. 2.1 10.
    text = re.sub(r"\b\d+(\.\d+)?\s*\:", "", text)

    # 3. remove bullet points
    text = text.replace("•", "")

    # 4. replace arrows
    text = text.replace("→", " to ")

    # 5. normalize spaces
    text = " ".join(text.split())

    return text


def split_into_paragraphs(text):
    sentences = text.split('. ')
    return [s.strip() for s in sentences if len(s)>20]

#each chunk contains 5 sentences
#each new chunk repeats 2 sentences from previous one
def create_chunks(sentences,chunk_size=5,overlap=2):
    chunks =[]
    i=0
    while i < len(sentences):
        chunk = sentences[i:i+chunk_size]
        print(chunk)
        chunks.append(". ".join(chunk))
        i+= (chunk_size - overlap)

    return chunks



