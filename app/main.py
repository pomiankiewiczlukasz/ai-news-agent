from services.rss_reader import get_news
from services.briefing_writer import save_briefing
from agents.news_ranker import rank_news
from agents.summary_agent import summarize_article


def main():
    # 1. Pobierz wiadomości z RSS
    articles = get_news()

    # 2. Wybierz najciekawszy artykuł
    best_article = rank_news(articles)

    print("Selected article:")
    print(best_article["title"])
    print(best_article["link"])
    print()

    # 3. Wygeneruj streszczenie przez Qwen2.5 (Ollama)
    summary = summarize_article(best_article)

    print("AI Summary:")
    print(summary)
    print()

    # 4. Zapisz briefing do pliku Markdown
    save_briefing(best_article, summary)

    print("Briefing saved.")


if __name__ == "__main__":
    main()