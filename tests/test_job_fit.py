from src.job_fit import (
    analyze_job_fit
)

resume_text = """
Python developer with
Machine Learning,
NLP,
LangChain,
FastAPI,
Streamlit,
RAG,
Qdrant,
and MongoDB experience.
"""

result = analyze_job_fit(
    resume_text
)

print(result)