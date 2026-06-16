from src.chat import (
    chat_with_resume
)

resume_text = """
Python developer with
Machine Learning,
NLP,
FastAPI,
LangChain,
LangGraph,
Qdrant,
MongoDB,
and RAG experience.
"""

while True:

    question = input(
        "\nAsk recruiter assistant: "
    )

    if question.lower() == "exit":

        break

    answer = chat_with_resume(
        resume_text,
        question
    )

    print(
        "\nAnswer:\n"
    )

    print(answer)
    