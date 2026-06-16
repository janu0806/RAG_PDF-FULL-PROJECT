import faiss
from sentence_transformers import SentenceTransformer

chunks = [
    "Robot arm has three joints",
    "Machine learning is a subset of AI",
    "Python is a programming language"
]

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(chunks)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

question = "How many joints are there?"

question_embedding = model.encode([question])

distances, indices = index.search(question_embedding, 1)

print("Best Match:")
print(chunks[indices[0][0]])