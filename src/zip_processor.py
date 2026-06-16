import zipfile
import os


UPLOAD_DIR = "uploads"


def extract_zip(zip_file):

    """
    Extract all PDFs from ZIP.
    """

    os.makedirs(
        UPLOAD_DIR,
        exist_ok=True
    )

    zip_path = os.path.join(
        UPLOAD_DIR,
        "temp.zip"
    )

    with open(
        zip_path,
        "wb"
    ) as f:

        f.write(
            zip_file.getbuffer()
        )

    with zipfile.ZipFile(
            zip_path,
            "r") as zip_ref:

        zip_ref.extractall(
            UPLOAD_DIR
        )

    pdf_files = []

    for root, _, files in os.walk(
            UPLOAD_DIR):

        for file in files:

            if file.lower().endswith(
                    ".pdf"):

                pdf_files.append(

                    os.path.join(
                        root,
                        file
                    )
                )

    return pdf_files