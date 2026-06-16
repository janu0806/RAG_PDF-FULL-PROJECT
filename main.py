from pdf_reader import read_pdf
from chunking import create_chunks
from gemini_service import ask_gemini
from vector_store import create_vector_store, retrieve_chunk

text = read_pdf("sample.pdf")

chunks = create_chunks(text)

index, embeddings = create_vector_store(chunks)

question = input("Ask Question: ")

context = retrieve_chunk(question, index, chunks)

answer = ask_gemini(context, question)

print(answer)