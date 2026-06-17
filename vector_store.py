import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_vector_store(chunks):

    if len(chunks) == 0:
        raise ValueError("No chunks generated. PDF text is empty.")

    embeddings = model.encode(chunks)

    embeddings = np.array(
        embeddings,
        dtype="float32"
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index, embeddings


def retrieve_chunk(question, index, chunks):

    question_embedding = model.encode([question])

    question_embedding = np.array(
        question_embedding,
        dtype="float32"
    )

    distances, indices = index.search(
        question_embedding,
        3
    )

    context = "\n\n".join(
        [chunks[i] for i in indices[0]]
    )

    return context