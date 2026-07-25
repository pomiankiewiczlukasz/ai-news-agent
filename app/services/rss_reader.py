import feedparser


RSS_URL = "https://rss.dw.com/xml/rss-de-all"


def get_news(limit=5):
    feed = feedparser.parse(RSS_URL)

    articles = []

    for entry in feed.entries[:limit]:
        articles.append(
            {
                "title": entry.title,
                "link": entry.link,
                "summary": entry.get("summary", ""),
            }
        )

    return articles