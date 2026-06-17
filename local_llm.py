from transformers import pipeline

generator = None

def ask_local_llm(context, question):
    global generator

    if generator is None:
        generator = pipeline(
            "text-generation",
            model="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
        )

    prompt = f"""
You are an AI assistant.

Answer ONLY from the given context.
If the answer is not in the context, say:
"I could not find the answer in the document."

Context:
{context}

Question:
{question}

Answer:
"""

    result = generator(
        prompt,
        max_new_tokens=80,
        do_sample=False,
        truncation=True
    )

    generated_text = result[0]["generated_text"]

    if "Answer:" in generated_text:
        answer = generated_text.split("Answer:")[-1].strip()
    else:
        answer = generated_text.strip()

    # Remove unwanted extra generated text
    if "Question:" in answer:
        answer = answer.split("Question:")[0].strip()

    return answer

