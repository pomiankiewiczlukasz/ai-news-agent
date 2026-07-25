from services.rss_reader import get_news
from services.news_writer import save_news
from agents.news_ranker import rank_news


def main():
    articles = get_news()

    best_article = rank_news(articles)

    print("Selected article:")
    print(best_article["title"])
    print(best_article["link"])

    save_news(articles)


if __name__ == "__main__":
    main()