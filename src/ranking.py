def get_candidate_rank(score):

    if score >= 85:
        return "Excellent Candidate"

    elif score >= 70:
        return "Strong Candidate"

    elif score >= 50:
        return "Potential Candidate"

    else:
        return "Needs Improvement"