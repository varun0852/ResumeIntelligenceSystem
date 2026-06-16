import faiss
import numpy as np
import pickle
import os

INDEX_PATH = "vectorstore/faiss.index"
META_PATH = "vectorstore/metadata.pkl"


def create_index(dimension=384):
    """
    Create a FAISS index.
    """
    return faiss.IndexFlatL2(dimension)


def save_index(index, metadata):
    """
    Save index and metadata.
    """

    os.makedirs(
        "vectorstore",
        exist_ok=True
    )

    faiss.write_index(
        index,
        INDEX_PATH
    )

    with open(
        META_PATH,
        "wb"
    ) as f:

        pickle.dump(
            metadata,
            f
        )


def load_index():
    """
    Load existing FAISS index.
    """

    if (
        not os.path.exists(INDEX_PATH)
        or
        not os.path.exists(META_PATH)
    ):

        return None, []

    index = faiss.read_index(
        INDEX_PATH
    )

    with open(
        META_PATH,
        "rb"
    ) as f:

        metadata = pickle.load(
            f
        )

    return index, metadata


def add_resume(
        embedding,
        candidate_name):
    """
    Add candidate embedding
    without duplicates.
    """

    index, metadata = load_index()

    if index is None:

        index = create_index(
            len(
                embedding
            )
        )

    # Skip if already exists
    for item in metadata:

        if (
            item["candidate"]
            ==
            candidate_name
        ):
            return

    embedding = np.array(
        [embedding]
    ).astype(
        "float32"
    )

    index.add(
        embedding
    )

    metadata.append({

        "candidate":
        candidate_name

    })

    save_index(
        index,
        metadata
    )

def search_candidates(
        query_embedding,
        top_k=5):
    """
    Search most relevant candidates.
    """

    index, metadata = load_index()

    if (
        index is None
        or
        len(metadata) == 0
    ):

        return []

    actual_k = min(
        top_k,
        len(metadata)
    )

    query_embedding = np.array(
        [query_embedding]
    ).astype(
        "float32"
    )

    distances, indices = index.search(
        query_embedding,
        actual_k
    )

    results = []

    seen = set()

    for idx in indices[0]:

        if (
            idx >= 0
            and
            idx < len(metadata)
            and
            idx not in seen
        ):

            results.append({

                "candidate":
                metadata[idx][
                    "candidate"
                ]
            })

            seen.add(
                idx
            )

    return results


def get_total_candidates():
    """
    Return total candidates
    stored in vector DB.
    """

    _, metadata = load_index()

    return len(
        metadata
    )


def reset_vector_store():
    """
    Delete FAISS index
    and metadata.
    """

    if os.path.exists(
            INDEX_PATH):

        os.remove(
            INDEX_PATH
        )

    if os.path.exists(
            META_PATH):

        os.remove(
            META_PATH
        )