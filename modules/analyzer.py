import json
import re
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "skills_dataset.json"

def role_catalog():
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))

def contains_skill(text, skill):
    pattern = r"(?<![a-z0-9])" + re.escape(skill.lower()).replace(r"\ ", r"\s+") + r"(?![a-z0-9])"
    return bool(re.search(pattern, text.lower()))

def analyze(text, requirements):
    requirements = list(dict.fromkeys(s.strip() for s in requirements if s.strip()))
    matched = [skill for skill in requirements if contains_skill(text, skill)]
    missing = [skill for skill in requirements if skill not in matched]
    score = round(len(matched) * 100 / len(requirements)) if requirements else 0
    return {"matched": matched, "missing": missing, "score": score, "total": len(requirements)}

def from_description(description, catalog=None):
    catalog = catalog or role_catalog()
    known = sorted(set(s for skills in catalog.values() for s in skills))
    return [skill for skill in known if contains_skill(description, skill)]
