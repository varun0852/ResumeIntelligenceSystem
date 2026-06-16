from src.embeddings import (
    get_embedding
)

from src.faiss_store import (
    add_resume,
    search_candidates,
    reset_vector_store
)

reset_vector_store()

add_resume(
    get_embedding(
        "Python NLP LangChain RAG"
    ),
    "Varun"
)

add_resume(
    get_embedding(
        "React JavaScript HTML CSS"
    ),
    "Frontend Developer"
)

query = get_embedding(
    "Looking for NLP engineer"
)

results = search_candidates(
    query,
    top_k=5
)

print(results)