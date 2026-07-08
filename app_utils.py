import re
import PyPDF2

def clean_resume_text(text: str) -> str:
    """
    Cleans raw text by removing URLs, hashtags, special characters, and extra spaces.
    """
    text = re.sub(r'http\S+\s*', ' ', text)
    text = re.sub(r'RT|cc', ' ', text)
    text = re.sub(r'#\S+', ' ', text)
    text = re.sub(r'@\S+', ' ', text)
    text = re.sub(r'[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', text)
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip().lower()

def extract_text_from_pdf(file) -> str:
    """
    Extracts raw text from an uploaded PDF file.
    """
    try:
        pdf_reader = PyPDF2.PdfReader(file)
    except Exception:
        return ""

    extracted_text = ""

    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            extracted_text += page_text + "\n"

    return extracted_text