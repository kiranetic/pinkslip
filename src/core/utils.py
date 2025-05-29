import os
import yaml
from core.logger import logger


def validate_file(file_path, file_name):
    if os.path.isfile(file_path):
        return file_path
    logger.warn(f"File {file_name} not found. Default will be used.")
    return None


def parse_ai_resume(tailored_resume_yaml: str, output_dir: str, resume_prefix: str) -> str:

    lines = tailored_resume_yaml.strip().splitlines()

    if lines and lines[0].startswith("```yaml"):
        lines = lines[2:-1]
    
    cleaned_yaml = "\n".join(lines)

    try:
        parsed_yaml = yaml.safe_load(cleaned_yaml)

        if not isinstance(parsed_yaml, dict):
            logger.error("Parsed resume is not a valid YAML dictionary")
            raise ValueError("Invalid resume format detected!")

        final_structure = {
            "cv": parsed_yaml
        }

        filename = f"{resume_prefix.replace(' ', '_')}_cv.yaml".lower()
        filepath = os.path.join(output_dir, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            yaml.dump(final_structure, f, allow_unicode=True, sort_keys=False)

        logger.info(f"Saved structured YAML to {filepath}.")
        return filepath

    except yaml.YAMLError as e:
        error_filename = f"{resume_prefix.replace(' ', '_')}_cv_error.yaml".lower()
        error_path = os.path.join(output_dir, error_filename)
        with open(error_path, "w", encoding="utf-8") as f:
            f.write(tailored_resume_yaml)
        logger.error(f"Failed to parse AI YAML. Raw content saved at {error_path}")
        raise

    except Exception as e:
        logger.error(f"Unexpected error while saving resume: {e}")
        raise


def build_resume_prompt(resume_yaml: dict, job_role: str, job_description: str | None = None) -> list[dict]:
    logger.info("Building resume prompt.")

    system_prompt = (
        "You are an experienced resume writer with 20 years of industry experience specializing in technical resumes.\n\n"
        "Your task is to generate an ATS friendly resume in RenderCV YAML format."
    )

    user_prompt = (
        f"---\nJob Role/Position:\n{job_role}\n\n"
        f"---\nUser profile:\n{resume_yaml}"
    )
    
    if job_description:
        user_prompt += f"\n\n---\nTailor it to this job description:\n{job_description}"

    user_prompt += (
        "\n\n---\nNow return only the modified YAML resume in RenderCV format (do not reorder sections).\n"
        "Do not include any explanation.\n"
        "Return valid YAML only. And do not include any hypens in generated texts.\n"
        "Do not hallucinate.\n"
        "Output YAML in markdown code block, but quote all values that include colons (:) to make it YAML-safe."
    )

    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

