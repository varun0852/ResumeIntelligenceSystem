SKILL_ALIASES = {

    "python": [
        "python"
    ],

    "machine learning": [
        "machine learning",
        "ml"
    ],

    "deep learning": [
        "deep learning",
        "dl"
    ],

    "nlp": [
        "nlp",
        "natural language processing"
    ],

    "sql": [
        "sql",
        "mysql",
        "postgresql"
    ],

    "rag": [
        "rag",
        "retrieval augmented generation"
    ],

    "langchain": [
        "langchain"
    ],

    "langgraph": [
        "langgraph"
    ],

    "agentic ai": [
        "agentic ai",
        "agentic rag"
    ],

    "qdrant": [
        "qdrant"
    ],

    "mongodb": [
        "mongodb",
        "mongodb atlas"
    ],

    "openai": [
        "openai"
    ],

    "huggingface": [
        "huggingface",
        "hugging face"
    ],

    "streamlit": [
        "streamlit"
    ],

    "fastapi": [
        "fastapi"
    ],

    "git": [
        "git",
        "github"
    ],

    "vector databases": [
        "vector database",
        "vector databases"
    ]
}


def extract_skills(text):

    text = text.lower()

    skills_found = []

    for skill, aliases in SKILL_ALIASES.items():

        for alias in aliases:

            if alias in text:

                skills_found.append(
                    skill
                )

                break

    return sorted(
        list(
            set(
                skills_found
            )
        )
    )