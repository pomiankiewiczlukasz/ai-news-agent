from services.rss_reader import get_news
from services.briefing_writer import save_briefing

from agents.news_ranker import rank_news
from agents.summary_agent import summarize_article
from agents.translation_agent import translate_summary
from agents.vocabulary_agent import extract_vocabulary
from agents.vocabulary_reviewer import review_vocabulary


def main():
    # 1. Pobierz wiadomości z RSS
    articles = get_news()

    # 2. Wybierz najważniejszy artykuł
    best_article = rank_news(articles)

    print("Selected article:")
    print(best_article["title"])
    print(best_article["link"])
    print()

    # 3. Generuj streszczenie po niemiecku
    summary_de = summarize_article(best_article)

    print("German Summary:")
    print(summary_de)
    print()

    # 4. Tłumaczenie na polski
    summary_pl = translate_summary(summary_de)

    print("Polish Translation:")
    print(summary_pl)
    print()

    # 5. Ekstrakcja słownictwa
    vocabulary_raw = extract_vocabulary(summary_de)

    # 6. Korekta jakości słownictwa
    vocabulary = review_vocabulary(vocabulary_raw)

    print("Vocabulary:")
    print(vocabulary)
    print()

    # 6. Zapis briefingu
    save_briefing(
        best_article,
        summary_de,
        summary_pl,
        vocabulary
    )

    print("Briefing saved.")


if __name__ == "__main__":
    main()