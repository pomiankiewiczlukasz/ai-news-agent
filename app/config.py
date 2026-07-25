import os

from dotenv import load_dotenv

load_dotenv()


RSS_URL = os.getenv(
    "RSS_URL",
    "https://rss.dw.com/xml/rss-de-all"
)


LLM_MODEL = os.getenv(
    "LLM_MODEL",
    "qwen2.5:7b"
)


NEWS_LIMIT = int(
    os.getenv(
        "NEWS_LIMIT",
        5
    )
)


GERMAN_VOICE = os.getenv(
    "GERMAN_VOICE",
    "de-DE-KatjaNeural"
)


POLISH_VOICE = os.getenv(
    "POLISH_VOICE",
    "pl-PL-MarekNeural"
)