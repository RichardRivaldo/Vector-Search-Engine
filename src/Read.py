# Libraries

import string
import nltk

# Read a file

def readfile(namafile):
    # Open File
    with open(namafile, 'r') as File:
        # Replace newlines with space
        contents = File.read().replace("\n", " ")
        
        # Change the texts into lowercase
        contents = contents.lower()
        
    return contents

# Text Cleaning

def cleaning(strings):
    # Cleaning special characters (#, *, @, etc) and digits
    # Can be used to remove HTML Tags for Web Scraping
    punc = str.maketrans('', '', string.punctuation)
    return (strings.translate(punc))

# Tokenization

def token(strings):
    # Tokenize the strings into a list containing words
    return (nltk.word_tokenize(strings))

def stopwd(strings):
    # Remove stopwords
    stopwords = set(nltk.stopwords.words('english'))

    return (nltk.)

s = cleaning("Can-t")
print(cleaning("Can-t"))
print(token(s))

print(cleaning("<@blue*band$$$>"))

namafile = "../test/Romeo1.txt"
strings = readfile(namafile)
print(strings)
clean = cleaning(strings)
print(clean)
print(token(clean))
