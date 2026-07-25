from services.ollama_client import ask_llm


def translate_summary(summary_de):
    prompt = f"""
You are a professional German-Polish translator.

Translate the German text into natural Polish.

IMPORTANT RULES:
- Return ONLY Polish.
- Do not explain your translation.
- Do not add comments.
- Keep headings and bullet points.

German text:

{summary_de}
"""

    return ask_llm(prompt)