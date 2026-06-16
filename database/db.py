import sqlite3
import pandas as pd

DATABASE_NAME = "resumes.db"


def create_db():
    """
    Creates the candidates table if it doesn't exist.
    """

    conn = sqlite3.connect(
        DATABASE_NAME
    )

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS candidates (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        ats_score REAL NOT NULL,

        semantic_score REAL NOT NULL,

        final_score REAL NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def insert_candidate(
        name,
        ats_score,
        semantic_score,
        final_score):
    """
    Inserts a candidate record.
    """

    conn = sqlite3.connect(
        DATABASE_NAME
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO candidates (
            name,
            ats_score,
            semantic_score,
            final_score
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            str(name),
            float(ats_score),
            float(semantic_score),
            float(final_score)
        )
    )

    conn.commit()
    conn.close()


def candidate_exists(name):
    """
    Check if candidate already exists.
    """

    conn = sqlite3.connect(
        DATABASE_NAME
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM candidates
        WHERE name = ?
        """,
        (name,)
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count > 0


def delete_by_name(name):
    """
    Delete candidate by name.
    Useful for preventing duplicates.
    """

    conn = sqlite3.connect(
        DATABASE_NAME
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM candidates
        WHERE name = ?
        """,
        (name,)
    )

    conn.commit()
    conn.close()


def get_candidates():
    """
    Returns all candidates sorted by final score.
    """

    conn = sqlite3.connect(
        DATABASE_NAME
    )

    query = """
    SELECT
        id,
        name,
        ats_score,
        semantic_score,
        final_score
    FROM candidates
    ORDER BY final_score DESC
    """

    df = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    if not df.empty:

        df["ats_score"] = pd.to_numeric(
            df["ats_score"],
            errors="coerce"
        )

        df["semantic_score"] = pd.to_numeric(
            df["semantic_score"],
            errors="coerce"
        )

        df["final_score"] = pd.to_numeric(
            df["final_score"],
            errors="coerce"
        )

    return df


def clear_database():
    """
    Deletes all candidate records.
    """

    conn = sqlite3.connect(
        DATABASE_NAME
    )

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM candidates"
    )

    conn.commit()
    conn.close()


def delete_candidate(candidate_id):
    """
    Deletes a specific candidate by ID.
    """

    conn = sqlite3.connect(
        DATABASE_NAME
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM candidates
        WHERE id = ?
        """,
        (candidate_id,)
    )

    conn.commit()
    conn.close()


def get_top_candidate():
    """
    Returns top ranked candidate.
    """

    conn = sqlite3.connect(
        DATABASE_NAME
    )

    query = """
    SELECT *
    FROM candidates
    ORDER BY final_score DESC
    LIMIT 1
    """

    df = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    return df