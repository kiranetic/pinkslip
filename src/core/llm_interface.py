import requests
from openai import OpenAI
from core.logger import logger
from config import (
    LLM_PROVIDER,
    OPENAI_API_KEY,
    OPENAI_MODEL,
    OLLAMA_HOST,
    OLLAMA_MODEL,
)


def call_openai(messages: list[dict]) -> str:
    client = OpenAI(
        api_key=OPENAI_API_KEY
    )

    logger.info(f"Generating tailored resume using model: {OPENAI_MODEL}")

    try:
        completion = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=messages,
            temperature=0.7,
        )

        logger.info("Resume generation complete.")
        return completion.choices[0].message.content
    except Exception as e:
        logger.error(f"Failed to generate resume: {e}")
        return ""


def call_ollama(messages: list[dict]) -> str:
    client = Client(
        host=OLLAMA_HOST
    )

    logger.info(f"Generating tailored resume using model: {OLLAMA_MODEL}")

    try:
        response = client.chat(
            model=OLLAMA_MODEL, 
            messages=messages
        )

        logger.info("Resume generation complete.")
        return response['message']['content'].strip()
    except Exception as e:
        logger.error(f"Failed to generate resume: {e}")
        return ""


def call_llm(messages: list[dict]) -> str:
    if LLM_PROVIDER == "openai":
        return call_openai(messages)
    elif LLM_PROVIDER == "ollama":
        return call_ollama(messages)
    else:
        logger.error(f"Unsupported LLM provider: {LLM_PROVIDER}")
        return ""

