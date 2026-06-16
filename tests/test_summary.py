from src.summary import (
    generate_summary
)

sample_resume = """
Python developer with
Machine Learning,
NLP,
LangChain,
FastAPI,
Streamlit,
and RAG experience.
"""

summary = generate_summary(
    sample_resume
)

print(summary)
