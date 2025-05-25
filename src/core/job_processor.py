import os
from slugify import slugify
from core.resume_generator import generate_custom_resume
from core.utils import parse_ai_resume
from core.rendercv_wrapper import run_rendercv
from core.logger import logger


def process_job_application(app, resume_yaml_str, base_cmd, output_dir, resume_prefix):
    logger.info(f"Processing job ID {app.id}: {app.role} at {app.company}")

    folder_name = f"{app.id}_{slugify(app.role)}_{slugify(app.company)}"
    job_output_dir = os.path.join(output_dir, folder_name)
    os.makedirs(job_output_dir, exist_ok=True)

    tailored_resume = generate_custom_resume(resume_yaml_str, app.job_description)
    if not tailored_resume:
        logger.error(f"Failed to generate resume for job ID {app.id}. Empty response.")
        continue

    cv_file = parse_ai_resume(tailored_resume, job_output_dir, resume_prefix)
    pdf_file_name = f"{resume_prefix}_{app.id}.pdf"
    pdf_path = os.path.join(job_output_dir, pdf_file_name)

    try:
        run_rendercv(cv_file, pdf_path, base_cmd)
    except Exception as e:
        logger.error(f"RenderCV failed for job {app.id}: {str(e)}")

