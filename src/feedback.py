import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv(
        "GROQ_API_KEY"
    )
)


def generate_feedback(
        resume_text,
        job_description):

    prompt = f"""
You are an expert AI recruiter.

Analyze the resume against the job description.

Provide:

1. Strengths
2. Weaknesses
3. Missing Skills
4. Recommendations

Keep response concise.

JOB DESCRIPTION:

{job_description}

RESUME:

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

        temperature=0.2
    )

    return (
        response
        .choices[0]
        .message
        .content
    )