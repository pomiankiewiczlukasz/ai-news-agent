from datetime import datetime


def save_news(articles):
    filename = "data/articles/latest_news.md"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("# Daily German News\n\n")
        file.write(
            f"Generated: {datetime.now()}\n\n"
        )

        for article in articles:
            file.write("## ")
            file.write(article["title"])
            file.write("\n\n")

            file.write(article["summary"])
            file.write("\n\n")

            file.write(article["link"])
            file.write("\n\n---\n\n")