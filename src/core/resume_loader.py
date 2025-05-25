import yaml
from core.logger import logger


def load_resume_yaml(file_path: str) -> dict:
    try:
        with open(file_path, "r") as file:
            data = yaml.safe_load(file)

        if data:
            logger.info(f"Successfully loaded resume YAML. Top-level keys: {list(data.keys())}")
            return data
        logger.warning(f"File '{file_path}' is empty or contains invalid data.")
        return {}
        
    except FileNotFoundError:
        logger.error(f"File '{file_path}' was not found.")
        raise
    except yaml.YAMLError as e:
        logger.error(f"Error parsing YAML file: {str(e)}")
        raise
    except Exception as e:
        logger.exception(f"Unexpected error while loading YAML file '{file_path}': {str(e)}")
        raise

