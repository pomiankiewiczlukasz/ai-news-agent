import asyncio

from services.tts_service import generate_audio


text = """
Die Situation in Al-Obeid verschärft sich weiter.
Die Kinder leiden unter einem Mangel an Lebensmitteln und Medikamenten.
"""


async def main():
    await generate_audio(
        text,
        "de-DE-KatjaNeural",
        "data/test_german.mp3"
    )

    print("Audio generated!")


if __name__ == "__main__":
    asyncio.run(main())