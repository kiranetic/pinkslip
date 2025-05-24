from core.sheets import fetch_job_applications

if __name__ == "__main__":
    apps = fetch_job_applications(sheet_name="PS-Jobs")
    for app in apps:
        print(f"{app.id}: {app.role} at {app.company} — Contact: {app.name} ({app.email})")

    send_email(
        to_email="sample.mail@gmail.com",
        subject="Application for Python Developer Role",
        body="Hi there,\n\nPlease find my application attached.\n\nRegards,\nYou",
        attachment_path="pdf/sample_resume.pdf"
    )
