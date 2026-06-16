from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

text = "Robot arm has three joints"

embedding = model.encode(text)

print("Embedding Length:", len(embedding))
print(embedding[:10])