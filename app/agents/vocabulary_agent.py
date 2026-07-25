import json

from services.ollama_client import ask_llm


def extract_vocabulary(summary_de):
    prompt = f"""
You are a German language teacher.

Analyze the German news summary and extract useful vocabulary
for a German learner at B2 level.

IMPORTANT RULES:
- Return ONLY valid JSON.
- No markdown.
- No explanations.
- Choose 5 important words or phrases.
- Provide accurate Polish translations.
- Do not invent meanings.
- Use standard dictionary translations.
IMPORTANT:
- Extract complete vocabulary expressions, not isolated words only.
- Prefer words that appear in the article.
- Verify translations carefully.
- For verbs include infinitive form.
- For separable verbs include the full expression.
- Avoid inventing phrases.

JSON format:

[
  {{
    "word": "German word",
    "translation": "Polish translation",
    "example_de": "Example sentence in German",
    "example_pl": "Polish translation"
  }}
]

Text:

{summary_de}
"""

    response = ask_llm(prompt)

    return json.loads(response)