import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

# Sample job description and resume text
job_description = "Looking for a Python developer with experience in machine learning."
resume = "Experienced Python developer skilled in machine learning."

# Tokenize text
def tokenize(text):
    return word_tokenize(text)

# Perform POS tagging and filter specific words with their POS tags
def pos_tagging(text):
    tokens = tokenize(text)
    tagged = pos_tag(tokens)
    specific_words = ['Python', 'developer', 'machine', 'learning']
    specific_words_pos_tagged = [(word, tag) for word, tag in tagged if word in specific_words]
    return specific_words_pos_tagged

# Perform Named Entity Recognition (NER) and filter specific words with their POS tags
def ner(text):
    tokens = tokenize(text)
    tagged = pos_tag(tokens)
    chunked = ne_chunk(tagged)
    specific_words = ['Python', 'developer', 'machine', 'learning']
    
    # Extract specific words from the NER tree structure with their POS tags
    specific_words_ner = []
    for entity in chunked:
        if hasattr(entity, 'label') and isinstance(entity, nltk.Tree):
            leaves = entity.leaves()
            for word, tag in leaves:
                if word in specific_words:
                    specific_words_ner.append((word, tag))
    
    return specific_words_ner

# Applying the functions to the job description and resume
print("Specific Words with POS Tags in POS Tagging for Job Description:")
print(pos_tagging(job_description))

print("\nSpecific Words with POS Tags in NER for Job Description:")
print(ner(job_description))

print("\nSpecific Words with POS Tags in POS Tagging for Resume:")
print(pos_tagging(resume))

print("\nSpecific Words with POS Tags in NER for Resume:")
print(ner(resume))
