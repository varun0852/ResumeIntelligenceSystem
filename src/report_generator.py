from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def generate_report(
        filename,
        candidate_name,
        ats_score,
        semantic_score,
        final_score,
        summary,
        feedback):

    doc = SimpleDocTemplate(
        filename
    )

    styles = (
        getSampleStyleSheet()
    )

    story = []

    story.append(
        Paragraph(
            "AI Resume Intelligence Report",
            styles["Title"]
        )
    )

    story.append(
        Spacer(1, 12)
    )

    story.append(
        Paragraph(
            f"Candidate: {candidate_name}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"ATS Score: {ats_score}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Semantic Score: {semantic_score}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Final Score: {final_score}",
            styles["BodyText"]
        )
    )

    story.append(
        Spacer(1, 12)
    )

    story.append(
        Paragraph(
            "Summary",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            summary,
            styles["BodyText"]
        )
    )

    story.append(
        Spacer(1, 12)
    )

    story.append(
        Paragraph(
            "Recruiter Feedback",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            feedback,
            styles["BodyText"]
        )
    )

    doc.build(
        story
    )