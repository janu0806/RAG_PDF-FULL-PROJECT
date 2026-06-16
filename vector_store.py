import faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_vector_store(chunks):

    embeddings = model.encode(chunks)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index, embeddings


def retrieve_chunk(question, index, chunks):

    question_embedding = model.encode([question])

    distances, indices = index.search(question_embedding, 1)

    return chunks[indices[0][0]]