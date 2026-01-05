import re
from pdfminer.high_level import extract_text

SKILLS_DB = [
    "html", "css", "javascript", "react", "bootstrap",
    "python", "flask", "git", "github", "responsive design"
]

def extract_resume_text(file_path):
    return extract_text(file_path).lower()

def extract_skills(text):
    return [
        skill for skill in SKILLS_DB
        if re.search(rf"\b{re.escape(skill)}\b", text)
    ]
