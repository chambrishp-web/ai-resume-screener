import re
import PyPDF2

def clean_resume_text(text):
    """
    Cleans raw text by removing URLs, hashtags, special characters, and extra spaces.
    """
    text = re.sub(r'http\S+\s*', ' ', text)  # Remove URLs
    text = re.sub(r'RT|cc', ' ', text)      # Remove RT and cc
    text = re.sub(r'#\S+', ' ', text)       # Remove hashtags
    text = re.sub(r'@\S+', ' ', text)       # Remove mentions
    text = re.sub(r'[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', text)  # Remove punctuations
    text = re.sub(r'[^\x00-\x7F]+', r' ', text) # Remove non-ASCII characters
    text = re.sub(r'\s+', ' ', text)        # Remove extra whitespaces
    return text.strip().lower()

def extract_text_from_pdf(file):
    """
    Extracts raw text from an uploaded PDF file.
    """
    pdf_reader = PyPDF2.PdfReader(file)
    extracted_text = ""
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            extracted_text += page_text + "\n"
    return extracted_text