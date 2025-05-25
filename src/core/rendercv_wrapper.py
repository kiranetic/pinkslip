import subprocess
import os
from core.utils import validate_file
from core.logger import logger
from config import RENDERCV_DIR


RENDERCV_DESIGN_FILE = "design.yaml"
RENDERCV_LOCALE_FILE = "locale.yaml"
RENDERCV_SETTINGS_FILE = "rendercv_settings.yaml"


def get_rendercv_dirs():
    input_dir = os.path.join(RENDERCV_DIR, "input")
    output_dir = os.path.join(RENDERCV_DIR, "output")
    tmp_output_dir = os.path.join(RENDERCV_DIR, "temp_output")

    design_file = os.path.join(input_dir, RENDERCV_DESIGN_FILE)
    locale_file = os.path.join(input_dir, RENDERCV_LOCALE_FILE)
    settings_file = os.path.join(input_dir, RENDERCV_SETTINGS_FILE)

    if not os.path.exists(RENDERCV_DIR):
        os.makedirs(RENDERCV_DIR)
        logger.info(f"Created base directory: {RENDERCV_DIR}")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        os.makedirs(tmp_output_dir)
        logger.info(f"Created output directory: {output_dir}")

    use_custom_config = os.path.isdir(input_dir)
    design_file = None
    locale_file = None
    settings_file = None

    if use_custom_config:
        logger.info(f"Found input folder: {input_dir}")

        design_file = validate_file(os.path.join(input_dir, RENDERCV_DESIGN_FILE), RENDERCV_DESIGN_FILE)
        locale_file = validate_file(os.path.join(input_dir, RENDERCV_LOCALE_FILE), RENDERCV_LOCALE_FILE)
        settings_file = validate_file(os.path.join(input_dir, RENDERCV_SETTINGS_FILE), RENDERCV_SETTINGS_FILE)
    else:
        logger.warn(f"No input folder found at {input_dir}. Using default RenderCV settings.")
    
    return {
        "base": RENDERCV_DIR,
        "input": input_dir,
        "output": output_dir,
        "temp_output": tmp_output_dir,
        "use_custom_config": use_custom_config,
        "design_file": design_file,
        "locale_file": locale_file,
        "settings_file": settings_file
    }


def build_rendercv_command(design_file=None, locale_file=None, settings_file=None, temp_output=None):
    cmd = ["rendercv", "render", "-nomd", "-nohtml", "-nopng"]
    
    if design_file:
        cmd += ["--design", design_file]
    if locale_file:
        cmd += ["--locale-catalog", locale_file]
    if settings_file:
        cmd += ["--rendercv-settings", settings_file]
    if temp_output:
        cmd += ["--output-folder-name", temp_output]
    
    return cmd


def run_rendercv(yaml_resume: str, pdf_path: str, base_cmd: list):
    try:
        cmd = base_cmd + [yaml_resume, "-pdf", pdf_path]
        logger.info(f"Running RenderCV: {' '.join(cmd)}")
        
        subprocess.run(cmd, check=True)

        logger.info(f"Rendered PDF: {pdf_path}")

    except subprocess.CalledProcessError as e:
        logger.error(f"RenderCV failed with exit code {e.returncode}")
        raise

    except Exception as e:
        logger.error(f"Unexpected error during RenderCV execution: {str(e)}")
        raise


def rendercv_init():
    paths = get_rendercv_dirs()

    base_cmd = build_rendercv_command(
        design_file=paths.get("design_file"),
        locale_file=paths.get("locale_file"),
        settings_file=paths.get("settings_file"),
        temp_output=paths.get("temp_output")
    )

    return paths, base_cmd

