import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv(
        "GROQ_API_KEY"
    )
)


def generate_summary(
        resume_text):

    prompt = f"""
    Analyze this resume.

    Create a concise
    professional summary.

    Resume:

    {resume_text}

    Summary:
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

        temperature=0.3
    )

    return (
        response
        .choices[0]
        .message
        .content
    )