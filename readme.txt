#this is intended to show the approach and not a functional code.
This code can work with importing the scikit module and using its own
tfidf vectorizer. My own tfidf vectorizer implementation is buggy due to 
time constraints.
similar.py: a text-document similarity checking that outputs a score that is
 based on the cosine similarity between the tf-idf vectors.
 ->Compare documents in the set to other documents in the set, using cosine similarity
 RUN: python similar.py file1 file2 file3 ... fileN
 ->doesn't work for the current version
 /*---------------------------------------------------------------------*/
This code might be buggy as it hasn't been tested since it was "intended
 to be a pseudo-code initially".
 /*---------------------------------------------------------------------*/
 Description:
It starts by converting the documents into TF-IDF(term frequency-inverse 
document frequency) vectors. The tf-idf values increase proportionally to
 the number of times a word appears in the document, but are offset by 
 the frequency of the word in the corpus, which helps to control for 
 the fact that some words are generally more common than others. The tf-idf
 values are taken for specific tokens that make up the text. The tokens
 are obtained by splitting and trimming the text as well as limiting it 
 to the stems of the words.
 
/*---------------------------------------------------------------------*/
Why tf-idf model?
/*---------------------------------------------------------------------*/
The tf-idf model is a well know method to evaluate how important is a word 
in a document. Tf-idf vectors are a great way of converting a text into a 
Vector Space Model (VSM), or into sparse features that are simply based on linear 
algebra. It also allows to compute a continuous degree of similarity between
documents(not a categorical exact match or not). Additionally, it allows
 ranking documents based on their relevance as compared to reference 
 documents.(For Classification) Classification can be done by either 
 finding the average tf-idf vector of each category in order to compare
 it to the values of the files we want to classify(choose the most 
similar category as a label). However, for a more precise classification,
 we can use a logisitc regression module that we train on a small sample 
 of the data. And then we can test it on a larger sample of data to check 
 for performace.
Disadvantges of the tf-idf model? It doesn't check the semantic 
difference between words. Therefore, documents with similar context but 
different terms will result in a false negative. Additionally, the order
 of the occurence of the terms is ignored.
/*---------------------------------------------------------------------*/
COSINE SIMILARITY:
It is a very efficient way to compare two text files based on their Vector
Space Model representation.
/*---------------------------------------------------------------------*/
Time spent: ~3 hours. (Mostly reading about various models to check for
similarity and learning the tf-idf + cosine similarity way)