from services.ollama_client import ask_llm


def summarize_article(article):
    prompt = f"""
You are a German news analyst.

Summarize the following article in German.

Title:
{article["title"]}

Content:
{article["summary"]}

Create:
- a short summary (3-5 sentences)
- key points
- why this news matters
"""

    return ask_llm(prompt)