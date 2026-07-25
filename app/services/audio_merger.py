from pydub import AudioSegment


def merge_audio_files(
    files,
    output_file,
    pause_seconds=2
):
    combined = AudioSegment.empty()

    pause = AudioSegment.silent(
        duration=pause_seconds * 1000
    )

    for file in files:
        audio = AudioSegment.from_mp3(file)

        combined += audio
        combined += pause

    combined.export(
        output_file,
        format="mp3"
    )