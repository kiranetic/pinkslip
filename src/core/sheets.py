from dataclasses import dataclass
from typing import List
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from config import GOOGLE_API_CREDENTIALS


@dataclass
class JobApplication:
    id: int
    name: str
    email: str
    role: str
    company: str
    website: str
    job_description: str
    applied: str
    follow_up_date: str
    notes: str


def get_gsheet_client():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_API_CREDENTIALS, scope)
    return gspread.authorize(creds)


def fetch_job_applications(sheet_name: str, worksheet_index: int = 0) -> List[JobApplication]:
    client = get_gsheet_client()
    sheet = client.open(sheet_name).get_worksheet(worksheet_index)
    records = sheet.get_all_records()

    applications = []
    for row in records:
        if str(row.get("Applied", "")).lower() != "yes":  # skip already applied
            try:
                app = JobApplication(
                    id=int(row.get("ID") or 0),
                    name=row.get("Name of Hiring Person", "").strip(),
                    email=row.get("Email", "").strip(),
                    role=row.get("Role", "").strip(),
                    company=row.get("Company", "").strip(),
                    website=row.get("Website", "").strip(),
                    job_description=row.get("Job Description", "").strip(),
                    applied=row.get("Applied", "").strip(),
                    follow_up_date=row.get("Follow-up Date", "").strip(),
                    notes=row.get("Notes", "").strip()
                )
                applications.append(app)
            except Exception as e:
                print(f"Error parsing row: {row}\n{e}")
    return applications
