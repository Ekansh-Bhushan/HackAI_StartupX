import nltk
from nltk.tokenize import word_tokenize

job_description = "Need a python developer you knows machine learning ."
resume_text = "experienced python"


job_description_tokens = word_tokenize(job_description)
resume_tokens = word_tokenize(resume_text)