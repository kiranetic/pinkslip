import yaml
from config import YAML_RESUME_DATA
from core.sheets import fetch_job_applications
from core.resume_loader import load_resume_yaml
from core.resume_generator import generate_custom_resume
from core.logger import logger


if __name__ == "__main__":
    apps = fetch_job_applications(sheet_name="PS-Jobs")
    for app in apps:
        print(f"{app.id}: {app.role} at {app.company} — Contact: {app.name} ({app.email})")

    try:
        logger.info("Starting resume generation process...")
        resume_dict = load_resume_yaml(YAML_RESUME_DATA)
        resume_yaml_str = yaml.dump(resume_dict)

        job_description = "Looking for a backend Python engineer experienced with FastAPI, PostgreSQL, and CI/CD on cloud infrastructure."

        tailored_resume = generate_custom_resume(resume_yaml_str, job_description)

        if tailored_resume:
            logger.info("Successfully generated tailored resume.")
            print("\n" + tailored_resume)
        else:
            logger.warning("Failed to generate a tailored resume. Empty response.")
    except Exception as e:
        logger.exception(f"Unexpected error in main: {str(e)}")
        raise

