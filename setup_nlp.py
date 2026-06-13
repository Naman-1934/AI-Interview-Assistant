# NLTK will analyze, preprocess, and interpret human language data
# Spacy is a free, open-source and large-scale industrial text processing.

import nltk
import spacy

# Download the Punkt tokenizer models
nltk.download('punkt') 

# Download the stopwords corpus for filtering out common words
nltk.download('stopwords') 

try:
    # en_core_web_sm is a lightweight, pre-trained English language processing pipeline provided by the spaCy open-source library
    spacy.load("en_core_web_sm")

except:
    import os

# It is a Python code snippet used to programmatically download and install a small English language model for the spaCy NLP library
    os.system("python -m spacy download en_core_web_sm")