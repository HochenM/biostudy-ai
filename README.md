# BioStudy AI v1 🧬

A Domain-Specific AI Learning Assistant Based on Retrieval-Augmented Generation (RAG)

## Overview

BioStudy AI v1 is an AI-powered learning assistant designed to help students study specialized academic subjects using their own educational materials.

Unlike general AI assistants that answer from broad knowledge, BioStudy AI focuses on course-specific information by retrieving relevant content from uploaded documents and generating explanations based on those materials.

The first version focuses on biology educational content and demonstrates a complete RAG pipeline from PDF processing to AI-generated answers.

---

# Problem

Students often struggle with scattered and unstructured learning resources across:

- Lecture notes
- Textbooks
- Course materials
- Online resources

This makes it difficult to focus on important concepts and prepare efficiently for exams.

---

# Solution

BioStudy AI provides a specialized AI tutor that:

- Processes educational PDFs
- Understands the content using semantic embeddings
- Retrieves relevant information using vector search
- Generates focused explanations using a language model

The goal is to create a subject-specific learning assistant rather than a general-purpose chatbot.

---

# Version 1 Scope

BioStudy AI v1 implements the core RAG pipeline:

PDF document → Text processing → Embeddings → Vector Search → LLM Answer Generation

The first version focuses on:

- Single PDF knowledge source
- Biology educational materials
- Question answering
- Retrieval-based explanations

---
## Architecture

The system follows a Retrieval-Augmented Generation (RAG) architecture:

```text
Educational PDF
       │
       ▼
Text Extraction (PyMuPDF)
       │
       ▼
Text Cleaning & Chunking
       │
       ▼
Sentence Transformer Embeddings
       │
       ▼
FAISS Vector Database
       │
       ▼
Semantic Retrieval
       │
       ▼
Context Construction
       │
       ▼
LLM Generation (FLAN-T5)
       │
       ▼
Final Answer

```


# Features

## Document Processing

- Extract text from PDF files
- Clean and normalize extracted text
- Split documents into meaningful chunks

## Semantic Search

- Convert text chunks into vector representations
- Use Sentence Transformer embeddings
- Retrieve relevant information using FAISS similarity search

## AI Answer Generation

- Use retrieved context from documents
- Generate natural language explanations using an instruction-tuned LLM

## Domain-Specific Learning

- Answers are based on uploaded educational materials
- Designed for specialized academic subjects

---

# Technologies Used

## Programming Language

- Python

## NLP & AI

- Hugging Face Transformers
- Sentence Transformers
- FLAN-T5

## Vector Search

- FAISS (Facebook AI Similarity Search)

## Document Processing

- PyMuPDF

## Numerical Computing

- NumPy

---

## Project Structure

```text
BioStudyAI/
│
├── main.py              # Application entry point
├── pipeline.py          # Connects all RAG components
├── ingest.py            # PDF text extraction
├── chunking.py          # Cleaning and text chunking
├── embeddings.py        # Sentence Transformer embeddings
├── vectorstore.py       # FAISS vector database implementation
├── llm.py               # Language model generation
├── data/
│   └── biology.pdf      # Example educational document
├── requirements.txt     # Required Python packages
└── README.md            # Project documentation
```



# Features

## Document Processing

- Extract text from PDF files
- Clean and normalize extracted text
- Split documents into meaningful chunks

## Semantic Search

- Convert text chunks into vector representations
- Use Sentence Transformer embeddings
- Retrieve relevant information using FAISS similarity search

## AI Answer Generation

- Use retrieved context from documents
- Generate natural language explanations using an instruction-tuned LLM

## Domain-Specific Learning

- Answers are based on uploaded educational materials
- Designed for specialized academic subjects

---

# Technologies Used

## Programming Language

- Python

## NLP & AI

- Hugging Face Transformers
- Sentence Transformers
- FLAN-T5

## Vector Search

- FAISS (Facebook AI Similarity Search)

## Document Processing

- PyMuPDF

## Numerical Computing

- NumPy

---



## Installation

1. **Clone the repository:**
   ```bash
   git clone <https://github.com/HochenM/biostudy-ai>
   cd BioStudyAI
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   ## Usage

**Run the application:**
```bash
python main.py
```

**The system will:**
1. Load the educational PDF.
2. Extract and process text.
3. Create embeddings.
4. Build the FAISS knowledge database.
5. Retrieve relevant information.
6. Generate an AI answer.

---

## Example

**Question:** > *"What is the function of mitochondria?"*

**Retrieved Knowledge:** > *Mitochondria produces energy through respiration. Cells break down glucose to produce energy (ATP).*

**BioStudy AI Answer:** > *"Mitochondria are organelles responsible for producing energy in cells through cellular respiration. They generate ATP, which provides energy for cellular activities."*

---

## Current Limitations (v1)

* Supports a single PDF knowledge source.
* No user accounts.
* No conversation memory (stateless interactions).
* Basic chunking strategy.
* Uses a small local language model.
* No graphical/web interface yet.

---

## Future Improvements

### Version 2
* Better chunking strategies
* Multiple PDF support
* Metadata storage (chapter, page number)
* Source citations
* Improved retrieval evaluation

### Version 3
* Web interface
* Chat history (conversational memory)
* User accounts
* Course management system

### Version 4
* Deployment as a full educational platform
* Integration of larger language models
* Personalized learning recommendations

---

## Learning Goals

This project demonstrates practical implementation of:
* Retrieval-Augmented Generation (RAG)
* Vector databases and semantic search
* Transformer-based embeddings
* LLM application development
* AI system architecture

---

## Author

Created as an AI Engineering portfolio project focused on applying Machine Learning and Generative AI to education.
