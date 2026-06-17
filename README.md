# 🤖 RAG PDF AI Assistant

A Retrieval-Augmented Generation (RAG) based PDF Question Answering system built using Streamlit, FAISS, Sentence Transformers, and TinyLlama.

## 📌 Overview

This project allows users to upload PDF documents and ask questions related to the content. The system retrieves the most relevant information from the document using semantic search and generates answers using a Local Large Language Model (LLM).

---

## 🚀 Features

* 📄 PDF Upload Support
* 🔍 Semantic Search using FAISS
* 🧠 Sentence Embeddings with Sentence Transformers
* 🤖 Local AI Answer Generation using TinyLlama
* 📚 Multiple PDF Support
* ⚡ Fast Retrieval-Augmented Generation (RAG)
* 🗑️ Clear Chat Option
* 🌙 Modern Streamlit User Interface

---

## 🏗️ Project Architecture

1. Upload PDF Document
2. Extract Text from PDF
3. Split Text into Chunks
4. Generate Embeddings
5. Store Embeddings in FAISS Vector Database
6. Retrieve Relevant Chunks
7. Generate Answer using TinyLlama
8. Display Response to User

---

## 🛠️ Technologies Used

* Python
* Streamlit
* FAISS
* Sentence Transformers
* Transformers
* TinyLlama
* PyPDF
* NumPy

---

## 📂 Project Structure

RAG_Project/

├── app.py

├── chunking.py

├── pdf_reader.py

├── vector_store.py

├── local_llm.py

├── requirements.txt

├── README.md

└── .gitignore

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/RAG-PDF-AI-Assistant.git
cd RAG-PDF-AI-Assistant
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 📸 Sample Workflow

1. Upload PDF
2. Enter a Question
3. Click "Get Answer"
4. View AI Generated Response
5. Explore Retrieved Context

---

## 🎯 Example Questions

* What is the aim of the project?
* How many joints are used in the robotic arm?
* What are the movement positions supported by the arm?
* What algorithm is used in the project?

---

## 📈 Future Enhancements

* Chat History Support
* Multi-Document Search
* PDF Summarization
* Source Citation
* Cloud Deployment
* Advanced LLM Integration

---

## 👩‍💻 Author

Janani Nevethitha K S

Department of Artificial Intelligence and Data Science

Velammal Engineering College

---

## 📄 License

This project is developed for educational and learning purposes.
