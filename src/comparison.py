import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv(
        "GROQ_API_KEY"
    )
)


def compare_candidates(
        candidate_data,
        job_description):

    prompt = f"""
You are a senior technical recruiter.

Compare these candidates.

Select:

1. Best Candidate
2. Runner-Up
3. Explain reasoning

Job Description:

{job_description}

Candidates:

{candidate_data}
"""

    response = client.chat.completions.create(

        model=
        "llama-3.3-70b-versatile",

        messages=[
            {
                "role":
                "user",

                "content":
                prompt
            }
        ],

        temperature=0.2
    )

    return (
        response
        .choices[0]
        .message
        .content
    )