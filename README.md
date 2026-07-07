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

# Architecture

Educational PDF
|
↓
Text Extraction (PyMuPDF)
|
↓
Text Cleaning & Chunking
|
↓
Sentence Transformer Embeddings
|
↓
FAISS Vector Database
|
↓
Semantic Retrieval
|
↓
Context Construction
|
↓
LLM Generation (FLAN-T5)
|
↓
Final Answer


---

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

# Project Structure


The system follows a Retrieval-Augmented Generation (RAG) architecture:
