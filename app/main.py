import asyncio

from agents.news_ranker import rank_news
from agents.summary_agent import summarize_article
from agents.translation_agent import translate_summary
from agents.vocabulary_agent import extract_vocabulary
from agents.vocabulary_reviewer import review_vocabulary

from services.rss_reader import get_news
from services.briefing_writer import save_briefing
from services.tts_service import generate_briefing_audio


def main():

    # 1. Get news from RSS
    articles = get_news()

    # 2. Select best article
    best_article = rank_news(articles)

    print("Selected article:")
    print(best_article["title"])
    print(best_article["link"])
    print()


    # 3. German summary
    summary_de = summarize_article(best_article)

    print("German Summary:")
    print(summary_de)
    print()


    # 4. Polish translation
    summary_pl = translate_summary(summary_de)

    print("Polish Translation:")
    print("TEXT FOR POLISH AUDIO:")
    print(summary_pl)
    print()


    # 5. Vocabulary extraction
    vocabulary_raw = extract_vocabulary(summary_de)

    # 6. Vocabulary review
    vocabulary = review_vocabulary(vocabulary_raw)

    print("Vocabulary:")
    print(vocabulary)
    print()


    # 7. Generate audio
    asyncio.run(
        generate_briefing_audio(
            summary_de,
            summary_pl,
            vocabulary
        )
    )

    print("Audio generated!")
    print()


    # 8. Save markdown briefing
    save_briefing(
        best_article,
        summary_de,
        summary_pl,
        vocabulary
    )

    print("Briefing saved!")


if __name__ == "__main__":
    main()