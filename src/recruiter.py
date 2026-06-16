def calculate_final_score(ats, semantic):
    return round(
        ats * 0.4 + semantic * 0.6, 2
    )