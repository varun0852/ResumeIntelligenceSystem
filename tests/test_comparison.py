from src.comparison import (
    compare_candidates
)

job_description = """
Looking for AI Engineer.

Required:
Python
NLP
FastAPI
RAG
Docker
"""

candidate_data = """

Candidate A

ATS: 85
Semantic: 70

Skills:
Python NLP RAG FastAPI

------------------

Candidate B

ATS: 80
Semantic: 60

Skills:
Python ML Pandas

------------------

Candidate C

ATS: 60
Semantic: 50

Skills:
HTML CSS JavaScript
"""

result = compare_candidates(
    candidate_data,
    job_description
)

print(result)