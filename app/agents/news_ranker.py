def rank_news(articles):
    keywords = [
        "Krieg",
        "Konflikt",
        "KI",
        "Künstliche Intelligenz",
        "Cyber",
        "Krise",
        "USA",
    ]

    scored_articles = []

    for article in articles:
        score = 0

        text = (
            article["title"]
            + " "
            + article["summary"]
        )

        for keyword in keywords:
            if keyword.lower() in text.lower():
                score += 1

        scored_articles.append(
            {
                "article": article,
                "score": score,
            }
        )

    scored_articles.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return scored_articles[0]["article"]
