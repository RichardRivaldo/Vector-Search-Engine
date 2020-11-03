# Preprocess the tokenized text

# Libraries

import nltk
import nltk.corpus

# Remove stopwords using stopwords corpus in NLTK as database

def stopwords(Tokens):
    return([i for i in Tokens if i not in nltk.corpus.stopwords.words("english")])

# Stemming words to its root using Porter Stemmer

def stemming(Tokens):
    # Create an object of Porter Stemmer
    Porter_Stemmer = nltk.stem.PorterStemmer()
    
    # Saving the stemmed version of each word into a list
    Stemmed = list()
    for words in Tokens:
        Stemmed.append(Porter_Stemmer.stem(words))        
    return(Stemmed)

# Lemmatize words to its root using NLTK WordNet Lemmatizer

def lemmatize(Tokens):
    # Create an object of Word Net Lemmatizer
    WordNetLemmatizer = nltk.stem.wordnet.WordNetLemmatizer()
    
    # Saving the lemmatized version of each word into a list
    Lemmatized = list()
    for words in Tokens:
        Lemmatized.append(WordNetLemmatizer.lemmatize(words))
    return(Lemmatized)