
import os
import json
import pandas as pd
import streamlit as st
import plotly.express as px

from src.auth import login, logout, is_authenticated
from src.parser import extract_text, clean_text
from src.skills import extract_skills
from src.ats import calculate_ats_score
from src.matcher import semantic_match
from src.ranking import get_candidate_rank
from src.recruiter import calculate_final_score
from src.zip_processor import extract_zip

from src.summary import generate_summary
from src.feedback import generate_feedback
from src.job_fit import analyze_job_fit
from src.chat import chat_with_resume
from src.comparison import compare_candidates

from src.embeddings import get_embedding
from src.faiss_store import add_resume
from src.recommendation import recommend_candidates
from src.report_generator import generate_report

from database.db import (
    create_db,
    insert_candidate,
    get_candidates,
    clear_database,
    delete_by_name
)

st.set_page_config(page_title="AI Resume Intelligence Platform", layout="wide")
create_db()

if not is_authenticated():
    login()
    st.stop()

logout()

st.title("🤖 AI Resume Intelligence Platform")

with st.sidebar:
    st.header("Controls")
    if st.button("Clear Database"):
        clear_database()
        st.success("Database Cleared")

    st.sidebar.markdown("---")
    st.sidebar.write("Version 1.0")

    st.markdown("---")
    st.caption("👨‍💻 Developed by Varun")

uploaded_resumes = st.file_uploader(
    "Upload Resumes",
    type=["pdf"],
    accept_multiple_files=True
)

uploaded_zip = st.file_uploader(
    "Upload ZIP Resumes",
    type=["zip"]
)

job_description = st.text_area("Job Description")


results = []

all_resumes = []

if uploaded_resumes:
    all_resumes.extend(
        uploaded_resumes
    )

if uploaded_zip:

    import io

    files = extract_zip(
        uploaded_zip
    )

    for file_path in files:

        with open(
            file_path,
            "rb"
        ) as f:

            pdf_bytes = f.read()

        fake_resume = io.BytesIO(
            pdf_bytes
        )

        fake_resume.name = os.path.basename(
            file_path
        )

        all_resumes.append(
            fake_resume
        )
        
if (uploaded_resumes or uploaded_zip) and job_description:  

    jd_text = clean_text(job_description)
    jd_skills = extract_skills(jd_text)

    for resume in all_resumes:

        resume_text = clean_text(extract_text(resume))

        semantic = semantic_match(resume_text, jd_text)
        resume_skills = extract_skills(resume_text)
        ats = calculate_ats_score(resume_skills, jd_skills)
        final = calculate_final_score(ats, semantic)
        rating = get_candidate_rank(final)

        try:
            summary = generate_summary(
                resume_text
            )
        except:
            summary = "Groq rate limit reached."

        try:
            feedback = generate_feedback(
                resume_text,
                job_description
            )
        except:
            feedback = "Groq rate limit reached."

        try:
            job_fit = analyze_job_fit(
                resume_text
            )
        except:
            job_fit = '{"AI Engineer":0,"ML Engineer":0,"Data Scientist":0,"NLP Engineer":0,"Backend Engineer":0}'
    

        delete_by_name(
            resume.name
)

        insert_candidate(
            resume.name,
            ats,
            semantic,
            final
        )

        add_resume(
            get_embedding(resume_text),
            resume.name
        )

        report_name = f"reports/{resume.name}_report.pdf"
        os.makedirs("reports", exist_ok=True)

        try:
            generate_report(
                report_name,
                resume.name,
                ats,
                semantic,
                final,
                summary,
                feedback
            )
        except:
            pass

        results.append({
            "Candidate": resume.name,
            "ATS": round(ats,2),
            "Semantic": round(semantic,2),
            "Final": round(final,2),
            "Rating": rating,
            "Summary": summary,
            "Feedback": feedback,
            "Job Fit": job_fit,
            "Resume Text": resume_text
        })

if results:

    results_df = pd.DataFrame(results)
    results_df = results_df.sort_values(
        by="Final",
        ascending=False
    ).reset_index(drop=True)

    results_df.insert(
        0,
        "Rank",
        range(1, len(results_df)+1)
    )

    st.subheader("🏆 Rankings")
    st.dataframe(results_df[["Rank","Candidate","ATS","Semantic","Final","Rating"]])

    top = results_df.iloc[0]

    c1,c2,c3 = st.columns(3)
    c1.metric("Top Candidate", top["Candidate"])
    c2.metric("Top Score", f"{top['Final']:.2f}%")
    c3.metric("Rating", top["Rating"])

    fig = px.bar(
        results_df,
        x="Candidate",
        y="Final",
        color="Final",
        text="Final"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.download_button(
        "Download CSV",
        results_df.to_csv(index=False),
        "rankings.csv",
        "text/csv"
    )

    st.subheader("📝 Candidate Details")

    candidate = st.selectbox(
        "Select Candidate",
        results_df["Candidate"]
    )

    row = results_df[results_df["Candidate"]==candidate].iloc[0]

    st.markdown("### AI Summary")
    st.write(row["Summary"])

    st.markdown("### AI Feedback")
    st.write(row["Feedback"])

    st.markdown("### Job Fit")

    try:

        job_fit_data = json.loads(
            row["Job Fit"]
        )

        job_fit_df = pd.DataFrame({

            "Role":
            list(
                job_fit_data.keys()
            ),

            "Fit":
            list(
                job_fit_data.values()
            )

        })

        fig_job_fit = px.bar(
            job_fit_df,
            x="Role",
            y="Fit",
            color="Fit",
            text="Fit",
            title="Job Fit Analysis"
        )

        fig_job_fit.update_traces(
            textposition="outside"
        )

        st.plotly_chart(
            fig_job_fit,
            use_container_width=True
        )

    except Exception:

        st.write(
            row["Job Fit"]
        )

    st.subheader("💬 Resume Chat")

    question = st.text_input("Ask a question")

    st.caption(
    """
    Example Questions:

    • Summarize this candidate

    • What are the candidate's strengths?

    • What skills are missing?

    • Would you recommend an interview?

    • What projects are most relevant?
    """
)

    if question:

        try:

            answer = chat_with_resume(
                row["Resume Text"],
                question
            )

        except:

            answer = (
                "Groq rate limit reached. "
                "Resume Chat temporarily unavailable."
            )

        st.write(answer)

    st.subheader("🔍 Candidate Recommendation")

    query = st.text_input("Search Skills")

    if query:
        recs = recommend_candidates(query)

        for r in recs:
            st.write("•", r["candidate"])

    st.subheader("⚖ Candidate Comparison")

    compare_blob = ""

    for _, r in results_df.iterrows():
        compare_blob += f"""
Candidate: {r['Candidate']}
ATS: {r['ATS']}
Semantic: {r['Semantic']}
Final: {r['Final']}
"""

    try:

        comparison = compare_candidates(
            compare_blob,
            job_description
        )

    except:

        comparison = (
            "Groq rate limit reached. "
            "Candidate comparison unavailable."
        )


    st.info(comparison)

st.divider()

dashboard_df = get_candidates()

st.subheader("📊 Recruiter Dashboard")

if not dashboard_df.empty:

    a,b,c = st.columns(3)

    a.metric("Candidates", len(dashboard_df))
    b.metric("Avg ATS", round(dashboard_df["ats_score"].mean(),2))
    c.metric("Avg Final", round(dashboard_df["final_score"].mean(),2))

    search = st.text_input("Search Stored Candidate")

    if search:
        dashboard_df = dashboard_df[
            dashboard_df["name"].str.contains(search, case=False, na=False)
        ]

    st.dataframe(dashboard_df, use_container_width=True)

## Scatter plot of ATS vs Semantic with final score as size and color for insights into candidate rankings

#     fig2 = px.scatter(
#     dashboard_df,
#     x="ats_score",
#     y="semantic_score",
#     size="final_score",
#     color="final_score",
#     hover_name="name",
#     title="ATS vs Semantic Analysis"
# )

#     st.plotly_chart(
#         fig2,
#         use_container_width=True
#     )


## Pie chart for candidate Candidate Rankings

#     fig2 = px.pie(
#     dashboard_df,
#     names="name",
#     values="final_score",
#     title="Candidate Score Distribution"
# )
#     st.plotly_chart(
#     fig2,
#     use_container_width=True
# )

## Horizontal bar chart for candidate rankings

    fig2 = px.bar(
    dashboard_df.sort_values(
        "final_score",
        ascending=True
    ),
    x="final_score",
    y="name",
    orientation="h",
    color="final_score",
    title="Candidate Rankings"
)

    st.plotly_chart(
        fig2,
        use_container_width=True
)


## Leaderboard style bar chart for candidate rankings
#     fig2 = px.bar(
#     dashboard_df,
#     x="name",
#     y="final_score",
#     color="final_score",
#     text="final_score",
#     title="Candidate Leaderboard"
# )

#     fig2.update_traces(
#         textposition="outside"
#     )

#     st.plotly_chart(
#         fig2,
#         use_container_width=True
# )

st.divider()

st.markdown(
    """
    <center>
    🚀 AI Resume Intelligence Platform v1.0<br>
    Developed by <b>Varun</b>
    </center>
    """,
    unsafe_allow_html=True
)