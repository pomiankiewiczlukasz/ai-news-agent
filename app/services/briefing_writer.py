from datetime import datetime
from pathlib import Path


def save_briefing(article, summary_de, summary_pl, vocabulary):
    output_dir = Path("data/briefings")
    output_dir.mkdir(parents=True, exist_ok=True)

    filename = output_dir / f"{datetime.now().strftime('%Y-%m-%d')}.md"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("# 🇩🇪 Daily German News Learning Briefing\n\n")
        file.write(
            f"Generated: {datetime.now():%Y-%m-%d %H:%M}\n\n"
        )

        file.write("## 📰 Article\n\n")
        file.write(f"**{article['title']}**\n\n")
        file.write(f"{article['link']}\n\n")

        file.write("---\n\n")

        file.write("## 🇩🇪 Zusammenfassung\n\n")
        file.write(summary_de)
        file.write("\n\n")

        file.write("---\n\n")

        file.write("## 🇵🇱 Streszczenie po polsku\n\n")
        file.write(summary_pl)
        file.write("\n\n")

        file.write("---\n\n")

        file.write("## 📚 Vocabulary\n\n")

        file.write("| Deutsch | Polski | Beispiel 🇩🇪 | Tłumaczenie 🇵🇱 |\n")
        file.write("|---|---|---|---|\n")

        for item in vocabulary:
            file.write(
                f"| {item['word']} | "
                f"{item['translation']} | "
                f"{item['example_de']} | "
                f"{item['example_pl']} |\n"
            )