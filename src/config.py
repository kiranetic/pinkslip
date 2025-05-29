from decouple import config

EMAIL_USER = config("EMAIL_USER")
EMAIL_PASS = config("EMAIL_PASS")
SMTP_SERVER = config("SMTP_SERVER", default="smtp.gmail.com")
SMTP_PORT = config("SMTP_PORT", cast=int, default=587)
USE_TLS = config("USE_TLS", cast=bool, default=True)
GOOGLE_API_CREDENTIALS = config("GOOGLE_API_CREDENTIALS", default="credentials.json")
YAML_RESUME_DATA = config("YAML_RESUME_DATA", default="resume_data.yaml")
LOG_FILE=config("LOG_FILE", default="ps.log")
RENDERCV_DIR=config("RENDERCV_DIR")
SHEET_NAME=config("GOOGLE_SHEET_NAME")
RESUME_NAME_PREFIX=config("RESUME_NAME_PREFIX")
LLM_PROVIDER = config("LLM_PROVIDER")
OPENAI_API_KEY = config("OPENAI_API_KEY")
OPENAI_MODEL = config("OPENAI_MODEL")
OLLAMA_MODEL = config("OLLAMA_MODEL", default="llama2")
OLLAMA_HOST = config("OLLAMA_HOST", default="http://localhost:11434")

