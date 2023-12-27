import pdfminer.high_level
import spacy
# resume_path
def preprocess_resume(resume_path):
    text = ""
    if resume_path.endswith(".pdf"):
        text = pdfminer.high_level.extract_text(resume_path)
    # elif resume_path.endswith((".docx", ".doc")):
    #     # Use a library like docx2txt to extract text
    else:
        with open(resume_path, "r") as f:
            text = f.read()

    # Clean and normalize text
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if not token.is_stop]
    return " ".join(tokens)

def extract_skills(processed_text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(processed_text)
    skills = [ent.text for ent in doc.ents if ent.label_ in ["SKILL", "ORG"]]
    return skills

print(extract_skills(preprocess_resume()))
