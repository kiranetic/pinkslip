import smtplib
from email.message import EmailMessage
from config import EMAIL_USER, EMAIL_PASS, SMTP_SERVER, SMTP_PORT, USE_TLS

def send_email(to_email, subject, body, attachment_path=None):
    msg = EmailMessage()
    msg["From"] = EMAIL_USER
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body)

    if attachment_path:
        with open(attachment_path, "rb") as f:
            file_data = f.read()
            filename = attachment_path.split("/")[-1]
            msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=filename)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        if USE_TLS:
            server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)
        print(f"Email sent to {to_email}")
