"""Resume Skill Gap Analyzer — lightweight public portfolio edition."""
import streamlit as st
from modules.analyzer import analyze, role_catalog, from_description
from modules.resume_parser import extract_resume_text

st.set_page_config(page_title="Resume Skill Gap Analyzer", page_icon="📄", layout="wide")
st.title("Resume Skill Gap Analyzer")
st.caption("Skill coverage estimates are heuristic, not official ATS scores or hiring predictions.")

catalog = role_catalog()
left, right = st.columns([1, 1], gap="large")

with left:
    st.subheader("1 · Your resume")
    uploaded = st.file_uploader("Upload a PDF or DOCX (optional)", type=["pdf", "docx"])
    pasted = st.text_area("Or paste resume text", height=180, placeholder="Skills: Python, Flask, SQL...")
    resume = pasted.strip()
    if uploaded and not resume:
        try:
            resume = extract_resume_text(uploaded)
            st.success("Resume text extracted.")
        except Exception as exc:
            st.error(str(exc))
    st.caption("Resumes are not written to a repository or permanent file by this app.")

with right:
    st.subheader("2 · Compare against a role")
    mode = st.radio("Source of requirements", ["Example job role", "Custom job description"], horizontal=True)
    if mode == "Example job role":
        role = st.selectbox("Target role", list(catalog))
        requirements = catalog[role]
    else:
        role = "Custom Job Description"
        description = st.text_area("Paste the job description", height=140)
        requirements = from_description(description, catalog)
        st.caption("Recognizes known skills from the example catalogue. Add skills to the JSON catalogue as needed.")

if st.button("Analyze skill gap", type="primary"):
    if not resume:
        st.warning("Add resume text or upload a resume first.")
    elif not requirements:
        st.warning("No recognized required skills found for this comparison.")
    else:
        result = analyze(resume, requirements)
        st.metric("Estimated skill overlap", f'{result["score"]}%')
        st.progress(result["score"] / 100)
        c1, c2 = st.columns(2)
        with c1:
            st.success(f'Matched skills ({len(result["matched"])})')
            st.write(", ".join(result["matched"]) or "None")
        with c2:
            st.warning(f'Skill gaps ({len(result["missing"])})')
            st.write(", ".join(result["missing"]) or "None")
        st.subheader("Suggested next steps")
        if result["missing"]:
            st.write("Explore beginner projects, documentation, or courses covering:")
            st.write(", ".join(result["missing"][:8]))
        else:
            st.write("All listed skills were detected in the text. Validate proficiency through practical projects.")
        report = ("Resume Skill Gap Analysis\n"
                  f"Target role: {role}\n"
                  f"Estimated overlap: {result['score']}%\n"
                  f"Matched: {', '.join(result['matched'])}\n"
                  f"Missing: {', '.join(result['missing'])}\n"
                  "This report is not an official ATS assessment.\n")
        st.download_button("Download report", report, file_name="skill_gap_report.txt")
st.divider()
st.caption("Portfolio edition · Python, Streamlit, text parsing and rule-based matching")
