from config import YAML_RESUME_DATA
from core.sheets import fetch_job_applications
from core.resume_loader import load_resume_yaml

if __name__ == "__main__":
    apps = fetch_job_applications(sheet_name="PS-Jobs")
    for app in apps:
        print(f"{app.id}: {app.role} at {app.company} — Contact: {app.name} ({app.email})")

    resume = load_resume_yaml(YAML_RESUME_DATA)
    print("Loaded resume keys:", list(resume.keys()))
