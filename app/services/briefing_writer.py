from datetime import datetime
from pathlib import Path


def save_briefing(article, summary):
    output_dir = Path("data/briefings")
    output_dir.mkdir(parents=True, exist_ok=True)

    filename = output_dir / f"{datetime.now().strftime('%Y-%m-%d')}.md"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("# German News Briefing\n\n")
        file.write(f"Generated: {datetime.now():%Y-%m-%d %H:%M}\n\n")

        file.write("## Selected article\n\n")
        file.write(f"**Title:** {article['title']}\n\n")
        file.write(f"**Link:** {article['link']}\n\n")

        file.write("## AI Summary\n\n")
        file.write(summary)
        file.write("\n")