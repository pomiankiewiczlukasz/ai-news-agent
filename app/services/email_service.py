import os
import smtplib

from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()


def send_email(
    subject,
    body,
    attachment_path=None
):
    gmail_user = os.getenv("GMAIL_USER")
    gmail_password = os.getenv("GMAIL_PASSWORD")

    msg = EmailMessage()

    msg["From"] = gmail_user
    msg["To"] = gmail_user
    msg["Subject"] = subject

    msg.set_content(body)

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