from services.ollama_client import ask_llm


def summarize_article(article):
    prompt = f"""
You are a professional German news analyst.

Your task is to summarize a German news article.

IMPORTANT RULES:
- Write ONLY in German.
- Do not use English.
- Do not use Chinese characters.
- Do not translate the text.
- Use clear B2-level German.

Create:

1. Kurzfassung (3-5 sentences)
2. Wichtigste Punkte (3 bullet points)
3. Warum ist diese Nachricht wichtig? (2-3 sentences)

Article title:

{article["title"]}

Article content:

{article["summary"]}
"""

    return ask_llm(prompt)