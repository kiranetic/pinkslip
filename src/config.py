from decouple import config

EMAIL_USER = config("EMAIL_USER")
EMAIL_PASS = config("EMAIL_PASS")
SMTP_SERVER = config("SMTP_SERVER", default="smtp.gmail.com")
SMTP_PORT = config("SMTP_PORT", cast=int, default=587)
USE_TLS = config("USE_TLS", cast=bool, default=True)
GOOGLE_API_CREDENTIALS = config("GOOGLE_API_CREDENTIALS", default="credentials.json")
