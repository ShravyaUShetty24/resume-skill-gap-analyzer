# Resume Skill Gap Analyzer

**Portfolio:** Shravya U Shetty

A Python + Streamlit portfolio app to compare skills in a resume with job-role requirements or a supplied job description. Supports plain text, PDF and DOCX resumes, matched/missing skills, role comparisons, visual summaries, and downloadable reports.

## Portfolio publication note
This is a **cleaned, lightweight GitHub edition** of Shravya's original project, organized for code review. It preserves the main resume-analysis workflow but **does not reproduce the original elaborate Streamlit interface or its 665-role dataset**. The original source package is retained separately. The original large resume/training CSVs and datasets of uncertain redistribution provenance are intentionally omitted. The included example skill catalogue is small and illustrative.

Scores are **heuristic keyword-overlap estimates**, not measured ATS results, predictions of hiring success, or validated machine-learning accuracy.

## Quick start
```bash
python -m venv .venv
# macOS / Linux:
source .venv/bin/activate
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Features
- Paste resume text or upload PDF/DOCX
- Pick a sample job role or enter a custom job description
- View matched and missing skills, and a simple gap percentage
- Compare likely skill overlap across example roles
- Download analysis as a text report
- Basic unit tests (`python -m unittest discover -s tests`)

## Privacy
Input resumes are processed in the running application; this repository contains **no candidate resumes**. Do not commit uploaded documents or reports with personal information. Run locally for private files unless you trust your deployment.

## Stack
Python, Streamlit, PyPDF2, python-docx, standard-library regex, JSON.
