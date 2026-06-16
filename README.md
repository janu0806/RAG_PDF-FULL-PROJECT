# RAG Project using Gemini + FAISS

## Overview

This project is a Retrieval-Augmented Generation (RAG) system that answers questions from a PDF document.

## Features

- Read PDF files
- Split text into chunks
- Generate embeddings using Sentence Transformers
- Store embeddings in FAISS
- Retrieve relevant chunks
- Generate answers using Gemini AI

## Project Structure

```
RAG_PROJECT/
│
├── main.py
├── pdf_reader.py
├── chunking.py
├── vector_store.py
├── gemini_service.py
├── sample.pdf
└── README.md
```

## Technologies Used

- Python
- FAISS
- Sentence Transformers
- Gemini API
- PyPDF

## How to Run

Install dependencies:

```bash
pip install pypdf
pip install sentence-transformers
pip install faiss-cpu
pip install google-generativeai
```

Run the project:

```bash
python main.py
```

Enter your question when prompted.

## Example

Question:

```
How many joints are used in the robot arm?
```

Answer:

```
Three joints.
```

## Author

Janani