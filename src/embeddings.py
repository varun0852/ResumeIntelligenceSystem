from sentence_transformers import SentenceTransformer

# Load once
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def get_embedding(text):

    """
    Convert text into vector embedding.
    """

    embedding = model.encode(
        text,
        convert_to_numpy=True
    )

    return embedding