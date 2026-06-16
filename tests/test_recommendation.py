from src.recommendation import (
    recommend_candidates
)

query = """
Python NLP LangChain
"""

results = (
    recommend_candidates(
        query
    )
)

print(
    "\nRecommended Candidates:\n"
)

for rank, candidate in enumerate(
        results,
        start=1):

    print(
        f"{rank}. "
        f"{candidate['candidate']}"
    )