from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

generator = None

def ask_local_llm(context, question):
    global generator

    if generator is None:
        model = AutoModelForSeq2SeqLM.from_pretrained(
            "google/flan-t5-small"
        )

        tokenizer = AutoTokenizer.from_pretrained(
            "google/flan-t5-small"
        )

        generator = pipeline(
            "text2text-generation",
            model=model,
            tokenizer=tokenizer
        )

    prompt = f"""
Answer ONLY from the given context.

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