from core.emailer import send_email

if __name__ == "__main__":
    send_email(
        to_email="sample.mail@gmail.com",
        subject="Application for Python Developer Role",
        body="Hi there,\n\nPlease find my application attached.\n\nRegards,\nYou",
        attachment_path="pdf/sample_resume.pdf"
    )
