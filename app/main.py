import asyncio
import logging

from agents.news_ranker import rank_news
from agents.summary_agent import summarize_article
from agents.translation_agent import translate_summary
from agents.vocabulary_agent import extract_vocabulary
from agents.vocabulary_reviewer import review_vocabulary
from agents.polish_cleaner import clean_polish_text

from services.rss_reader import get_news
from services.briefing_writer import save_briefing
from services.tts_service import generate_briefing_audio
from services.email_service import send_email
from services.logger import setup_logger


def main():

    logger = setup_logger()

    logger.info(
        "AI News Agent started"
    )

    # 1. Get news from RSS
    articles = get_news()

    logger.info(
        f"Articles fetched: {len(articles)}"
    )


    # 2. Select best article
    best_article = rank_news(articles)

    logger.info(
        f"Selected article: {best_article['title']}"
    )

    print("Selected article:")
    print(best_article["title"])
    print(best_article["link"])
    print()


    # 3. German summary
    summary_de = summarize_article(best_article)

    logger.info(
        "German summary generated"
    )

    print("German Summary:")
    print(summary_de)
    print()


    # 4. Polish translation
    summary_pl_raw = translate_summary(summary_de)

    summary_pl = clean_polish_text(
        summary_pl_raw
    )

    logger.info(
        "Polish translation generated"
    )

    print("Polish Translation:")
    print(summary_pl)
    print()


    # 5. Vocabulary
    vocabulary_raw = extract_vocabulary(summary_de)

    vocabulary = review_vocabulary(
        vocabulary_raw
    )

    logger.info(
        "Vocabulary generated"
    )

    print("Vocabulary:")
    print(vocabulary)
    print()


    # 6. Generate audio
    asyncio.run(
        generate_briefing_audio(
            summary_de,
            summary_pl,
            vocabulary
        )
    )

    logger.info(
        "Audio generated"
    )

    print("Audio generated!")
    print()


    # 7. Save briefing
    save_briefing(
        best_article,
        summary_de,
        summary_pl,
        vocabulary
    )

    logger.info(
        "Briefing saved"
    )


    # 8. Send email
    send_email(
    subject="AI News Agent Daily Briefing",
    article_title=best_article["title"],
    article_link=best_article["link"],
    summary_de=summary_de,
    summary_pl=summary_pl,
    vocabulary=vocabulary,
    attachment_path="data/audio/daily_briefing.mp3"
)

    print("Email sent!")
    print()


if __name__ == "__main__":
    main()

