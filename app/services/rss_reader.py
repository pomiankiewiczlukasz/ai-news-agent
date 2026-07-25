import feedparser

from config import RSS_URL, NEWS_LIMIT


def get_news():
    feed = feedparser.parse(RSS_URL)

    articles = []

    for entry in feed.entries[:NEWS_LIMIT]:
        articles.append(
            {
                "title": entry.title,
                "link": entry.link,
                "summary": entry.get("summary", ""),
            }
        )

    return articles