import edge_tts

from config import GERMAN_VOICE, POLISH_VOICE
from services.audio_merger import merge_audio_files


async def generate_audio(text, voice, output_file):
    communicate = edge_tts.Communicate(
        text=text,
        voice=voice
    )

    await communicate.save(output_file)


async def generate_briefing_audio(
    summary_de,
    summary_pl,
    vocabulary
):
    # =========================
    # German summary
    # =========================

    await generate_audio(
        summary_de,
        GERMAN_VOICE,
        "data/audio/summary_de.mp3"
    )


    # =========================
    # Polish summary
    # =========================

    await generate_audio(
        summary_pl,
        POLISH_VOICE,
        "data/audio/summary_pl.mp3"
    )


    # =========================
    # Vocabulary split by language
    # =========================

    vocab_de = ""
    vocab_pl = ""

    for item in vocabulary:
        vocab_de += (
            f"{item['word']}. "
            f"{item['example_de']}. "
        )

        vocab_pl += (
            f"{item['translation']}. "
            f"{item['example_pl']}. "
        )


    # =========================
    # German vocabulary
    # =========================

    await generate_audio(
        vocab_de,
        GERMAN_VOICE,
        "data/audio/vocabulary_de.mp3"
    )


    # =========================
    # Polish vocabulary
    # =========================

    await generate_audio(
        vocab_pl,
        POLISH_VOICE,
        "data/audio/vocabulary_pl.mp3"
    )


    # =========================
    # Merge final briefing
    # =========================

    merge_audio_files(
        [
            "data/audio/summary_de.mp3",
            "data/audio/summary_pl.mp3",
            "data/audio/vocabulary_de.mp3",
            "data/audio/vocabulary_pl.mp3",
        ],
        "data/audio/daily_briefing.mp3"
    )