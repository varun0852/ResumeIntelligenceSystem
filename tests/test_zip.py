from src.zip_processor import (
    extract_zip
)

zip_path = "candidates.zip"

class FakeUpload:

    def __init__(self, path):

        self.path = path

    def getbuffer(self):

        with open(
                self.path,
                "rb") as f:

            return f.read()


uploaded_zip = FakeUpload(
    zip_path
)

pdfs = extract_zip(
    uploaded_zip
)

print(
    "\nExtracted PDFs:\n"
)

for pdf in pdfs:

    print(pdf)