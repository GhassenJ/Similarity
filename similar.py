#This is intended to be a pseudo-code
import nltk, numpy
import sys, string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import math
#from sklearn.feature_extraction.text import TfidfVectorizer
#


token = {}
stemmer = PorterStemmer()

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tfidf(term, file, files):
    tf = token[file].count(term) / float(len(token[file]))
    count = 0
    for f in files:
        if term in token[f]:
            count = count + 1
    if count > 0:
        return (1.0 + math.log(float(len(files)) / count))* tf
    else:
        return tf
def cosine_distance(a, b):
    return numpy.dot(a, b) / (math.sqrt(numpy.dot(a, a)) * math.sqrt(numpy.dot(b, b)))
    
if __name__ == '__main__':
    files = sys.argv
    max_length = 0
    del files[0] #avoid the executable's name
    for file in files:
        file_read = open(file, 'r')
        text = file_read.read()
        lowers = text.lower()
        no_punctuation = lowers.translate(None, string.punctuation)
        token_dict = no_punctuation
        tokens = nltk.word_tokenize(token_dict)
        #tokens = [x for x in tokens if not x in stopwords.words('english')]
        token[file] = stem_tokens(tokens, stemmer)
        if len(token) > max_length:
            max_length = len
    #We can use the Scikits.learn (sklearn) module or implement it    
        #tfidf = TfidfVectorizer(stop_words='english')
        #tfs[file] = tfidf.fit_transform(token[file])

    #############################################
    #The code should go like this: Initialize a 2-D matrix with the files in the columns and the terms in the rows.
    #For each file: (for each term: calcualte teh tf-idf and put it in the corresponding entry + if the term is non-existentL: 
    #make a new row with all zeroes for previous functions and then put the tf-idf in the new entry).
    #Eventually, we have a matrix. And the Cosine similarity is measured between the different columns where most of the values
    #will be 0's:
    #############################################
    #This is a rushed/failed attempt at initializing an filling the matrix    
    
    #tfs = {}
    #for file in files:
       # a = {}
        #for term in token[file]:
           # a[term] = tfidf(term, file, files)
       # tfs[file] = a
    print tfs
    #Now that we have the tf-idf vectors we can compare the files using cosine similarity
    #For the purpose of this demonstration, I will only compare the first 2 files
    vector1, vector2 = tfs[files[0]], tfs[files[1]]
    #print cosine_distance(vector1, vector2)
    
    
#The current implementation of the tfidf vectorizer doesn't work on files with different tokens. 
#The current cosine calculator only accepts lsits.
#this is intended to show the approach and not a functional code.