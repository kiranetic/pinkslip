from ollama import chat, Client
from config import OLLAMA_MODEL, OLLAMA_HOST


PROMPT_TEMPLATE = """
You are a resume assistant AI.

You will receive:
1. The candidate's complete resume data in YAML.
2. A job description (or role title).

Your job is to generate a **tailored ATS friendly YAML resume** that better aligns with the job.

---
Job Description:
{job_description}

---
Original Resume (YAML):
{resume_yaml}

---
Now return only the **modified YAML** resume. Do not include any explanation. Do not hallucinate.
"""


client = Client(host=OLLAMA_HOST)


def generate_custom_resume(resume_yaml: str, job_description: str, model: str) -> str:
    prompt = PROMPT_TEMPLATE.format(resume_yaml=resume_yaml, job_description=job_description)

    try:
        response = client.chat(model=OLLAMA_MODEL, messages=[
            {
                "role": "user", 
                "content": prompt
            }
        ])
        return response['message']['content'].strip()
    except Exception as e:
        print(f"[ERROR] Failed to generate resume: {e}")
        return ""
