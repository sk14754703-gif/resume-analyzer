from flask import Flask, render_template, request
import os
from resume_parser import extract_resume_text, extract_skills
from matcher import calculate_score

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    score = None
    skills = []

    if request.method == "POST":
        resume = request.files["resume"]
        job_desc = request.form["job_desc"]

        file_path = os.path.join(UPLOAD_FOLDER, resume.filename)
        resume.save(file_path)

        resume_text = extract_resume_text(file_path)
        skills = extract_skills(resume_text)
        score = calculate_score(resume_text, job_desc)

    return render_template("index.html", score=score, skills=skills)

if __name__ == "__main__":
    app.run(debug=True)
