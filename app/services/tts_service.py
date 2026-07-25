import edge_tts
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
    await generate_audio(
        summary_de,
        "de-DE-KatjaNeural",
        "data/audio/summary_de.mp3"
    )

    await generate_audio(
        summary_pl,
        "pl-PL-MarekNeural",
        "data/audio/summary_pl.mp3"
    )

    vocab_text = ""

    for item in vocabulary:
        vocab_text += (
            f"{item['word']}. "
            f"{item['translation']}. "
            f"{item['example_de']}. "
            f"{item['example_pl']}. "
        )

    await generate_audio(
        vocab_text,
        "de-DE-KatjaNeural",
        "data/audio/vocabulary.mp3"
    )

    merge_audio_files(
        [
            "data/audio/summary_de.mp3",
            "data/audio/summary_pl.mp3",
            "data/audio/vocabulary.mp3",
        ],
        "data/audio/daily_briefing.mp3"
    )
    