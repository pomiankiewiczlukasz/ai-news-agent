import os
import smtplib

from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()


def send_email(
    subject,
    article_title,
    article_link,
    summary_de,
    summary_pl,
    vocabulary,
    attachment_path=None
):
    gmail_user = os.getenv("GMAIL_USER")
    gmail_password = os.getenv("GMAIL_PASSWORD")

    msg = EmailMessage()

    msg["From"] = gmail_user
    msg["To"] = gmail_user
    msg["Subject"] = subject

    vocabulary_text = ""

    for item in vocabulary:
        vocabulary_text += f"""
        <li>
            <b>{item['word']}</b> -
            {item['translation']}<br>
            🇩🇪 {item['example_de']}<br>
            🇵🇱 {item['example_pl']}
        </li>
        """

    html = f"""
    <html>
    <body>

    <h2>🇩🇪 Daily German News Briefing</h2>

    <h3>📰 Article</h3>

    <p>
    <b>{article_title}</b>
    </p>

    <p>
    🔗 <a href="{article_link}">
    Open original article
    </a>
    </p>


    <h3>🇩🇪 German Summary</h3>

    <p>
    {summary_de.replace(chr(10), "<br>")}
    </p>


    <h3>🇵🇱 Polish Translation</h3>

    <p>
    {summary_pl.replace(chr(10), "<br>")}
    </p>


    <h3>📚 Vocabulary</h3>

    <ul>
    {vocabulary_text}
    </ul>


    <h3>🎧 Audio</h3>

    <p>
    Daily briefing audio is attached.
    </p>


    </body>
    </html>
    """

    msg.add_alternative(
        html,
        subtype="html"
    )


    if attachment_path:
        with open(attachment_path, "rb") as file:
            data = file.read()

        msg.add_attachment(
            data,
            maintype="audio",
            subtype="mpeg",
            filename="daily_briefing.mp3"
        )


    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465
    ) as smtp:

        smtp.login(
            gmail_user,
            gmail_password
        )

        smtp.send_message(msg)