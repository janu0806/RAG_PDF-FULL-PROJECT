from transformers import pipeline

generator = None

def ask_local_llm(context, question):
    global generator

    if generator is None:
        generator = pipeline(
            "text2text-generation",
            model="google/flan-t5-small"
        )

    prompt = f"""
Answer the question only from the context.

Context:
{context}

Question:
{question}

Answer:
"""

    result = generator(
        prompt,
        max_new_tokens=50
    )

    return result[0]["generated_text"]