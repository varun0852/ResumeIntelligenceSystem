from src.feedback import (
    generate_feedback
)

resume_text = """
Python developer with
Machine Learning,
NLP,
LangChain,
FastAPI,
Streamlit,
and RAG experience.
"""

job_description = """
Looking for an AI Engineer.

Required:

Python
Machine Learning
NLP
Docker
AWS
FastAPI
"""

feedback = generate_feedback(
    resume_text,
    job_description
)

print(feedback)