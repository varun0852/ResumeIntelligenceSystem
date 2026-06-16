def calculate_ats_score(
    resume_skills,
    jd_skills
):

    if len(jd_skills) == 0:
        return 0

    matched_skills = len(
        set(resume_skills)
        &
        set(jd_skills)
    )

    ats_score = (
        matched_skills /
        len(jd_skills)
    ) * 100

    return round(
        ats_score,
        2
    )
    
    SKILL_ALIASES = {
    "machine learning": [
        "machine learning",
        "ml"
    ],

    "nlp": [
        "nlp",
        "natural language processing"
    ],

    "scikit-learn": [
        "scikit learn",
        "sklearn",
        "scikit-learn"
    ],

    "tensorflow": [
        "tensorflow",
        "tf"
    ]
}