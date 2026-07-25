from services.ollama_client import ask_llm


def clean_polish_text(text):
    prompt = f"""
Jesteś profesjonalnym korektorem języka polskiego.

Twoim zadaniem jest poprawić poniższy tekst.

Zasady:
- Zwróć wyłącznie poprawiony tekst.
- Pisz tylko po polsku.
- Usuń chińskie, niemieckie i inne obce fragmenty.
- Popraw błędy gramatyczne i stylistyczne.
- Zachowaj oryginalne znaczenie.
- Tekst ma być naturalny do słuchania w nagraniu audio.
- Poziom języka: B2.

Tekst do poprawy:

{text}
"""

    return ask_llm(prompt)
