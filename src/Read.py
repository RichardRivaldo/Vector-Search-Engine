# Read the file and tokenize the texts

# Libraries

import string
import nltk

# Read a file and change it to lowercase

def readfile(namafile):
    # Open File
    with open(namafile, 'r') as File:
        # Replace newlines with space
        contents = File.read().replace("\n", " ")
        
        # Change the texts into lowercase
        contents = contents.lower()
        
    return contents

# Cleaning special characters (punctuarions)

def cleaning(strings):
    # Can be used to remove HTML Tags for Web Scraping
    # Replace with Whitespace, same length with the punctuation
    punc = str.maketrans(string.punctuation, ' '*len(string.punctuation))
    return (strings.translate(punc))

# Tokenization process

def token(strings):
    # Tokenize the strings into a list containing words
    return (nltk.word_tokenize(strings))