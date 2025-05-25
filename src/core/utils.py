import os
import yaml
from core.logger import logger


def validate_file(file_path, file_name):
    if os.path.isfile(file_path):
        return file_path
    logger.warn(f"File {file_name} not found. Default will be used.")
    return None


def parse_ai_resume(tailored_resume_yaml: str, output_dir: str, resume_prefix: str) -> str:
    try:
        parsed_yaml = yaml.safe_load(tailored_resume_yaml)

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

    except Exception as e:
        logger.error(f"Failed to parse/save AI resume: {e}")
        raise

