import json

from services.ollama_client import ask_llm


def review_vocabulary(vocabulary):
    prompt = f"""
You are an expert German language teacher.

Review the following vocabulary list created by another AI.

Your tasks:
- Fix incorrect Polish translations.
- Remove invented or incorrect expressions.
- Correct German word forms.
- Prefer B2-level useful vocabulary.
- Keep only 5 items.
- Return ONLY valid JSON.

Required JSON format:

[
  {{
    "word": "German word or expression",
    "translation": "Polish translation",
    "example_de": "German example sentence",
    "example_pl": "Polish translation"
  }}
]

Vocabulary to review:

{json.dumps(vocabulary, ensure_ascii=False)}
"""

    response = ask_llm(prompt)

    return json.loads(response)