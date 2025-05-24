import yaml

def load_resume_yaml(file_path: str) -> dict:
    try:
        with open(file_path, "r") as file:
            data = yaml.safe_load(file)

        if data:
            return data
        print(f"File '{file_path}' is empty.")
        return {}
        
    except FileNotFoundError:
        print("File not found.")
    except yaml.YAMLError as e:
        print(f"Error loading YAML: {str(e)}")
    except Exception as e:
        print(f"An unknown error occurred: {str(e)}")
