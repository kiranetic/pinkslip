import yaml
from config import YAML_RESUME_DATA, SHEET_NAME, RESUME_NAME_PREFIX
from core.resume_loader import load_resume_yaml
from core.sheets import fetch_job_applications
from core.logger import logger
from core.rendercv_wrapper import rendercv_init
from core.job_processor import process_job_application


if __name__ == "__main__":
    # apps = fetch_job_applications(sheet_name="PS-Jobs")
    # for app in apps:
    #     print(f"{app.id}: {app.role} at {app.company} — Contact: {app.name} ({app.email})")

    try:
        resume_dict = load_resume_yaml(YAML_RESUME_DATA)
        resume_yaml_str = yaml.dump(resume_dict)

        paths, base_cmd = rendercv_init()

        applications = fetch_job_applications(sheet_name=SHEET_NAME)

        for app in applications:
            process_job_application(app, resume_yaml_str, base_cmd, paths["output"], RESUME_NAME_PREFIX)

    except Exception as e:
        logger.exception(f"Unexpected error in main: {str(e)}")
        raise

