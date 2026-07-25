from services.email_service import send_email


send_email(
    subject="AI News Agent test",
    body="""
Hello!

This is a test email from my AI News Agent.

🚀
"""
)

print("Email sent!")