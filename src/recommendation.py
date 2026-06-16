from src.embeddings import (
    get_embedding
)

from src.faiss_store import (
    search_candidates
)


def recommend_candidates(
        query,
        top_k=5):

    query_embedding = (
        get_embedding(
            query
        )
    )

    results = (
        search_candidates(
            query_embedding,
            top_k
        )
    )

    return results