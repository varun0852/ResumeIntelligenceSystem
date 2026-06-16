import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv(
        "GROQ_API_KEY"
    )
)


def analyze_job_fit(
        resume_text):

    prompt = f"""
You are an expert career advisor.

Analyze this resume.

Estimate fit percentages for:

1. AI Engineer
2. ML Engineer
3. Data Scientist
4. NLP Engineer
5. Backend Engineer

Return ONLY JSON.

Example:

{{
    "AI Engineer": 92,
    "ML Engineer": 88,
    "Data Scientist": 84,
    "NLP Engineer": 91,
    "Backend Engineer": 70
}}

Resume:

{resume_text}
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

    temperature=0.1
)

    result = (
        response
        .choices[0]
        .message
        .content
    )

    result = (
        result
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return result