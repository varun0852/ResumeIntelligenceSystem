from src.report_generator import (
    generate_report
)

generate_report(

    filename=
    "sample_report.pdf",

    candidate_name=
    "Varun",

    ats_score=
    85,

    semantic_score=
    64,

    final_score=
    78,

    summary=
    "Strong AI candidate.",

    feedback=
    """
Strengths:
NLP

Weakness:
Docker

Recommendation:
Learn AWS
"""
)

print(
    "PDF Generated!"
)