#!/usr/bin/python
# -*- coding: UTF-8 -*-
import string

stopwords = []
def import_stopwords():
    stopwords_path = "res/stopwords.txt"
    fileObject = open(stopwords_path, 'r')
    for line in fileObject.readlines():
        stopwords.append(line.strip())
    # print stopwords

def remove_noise(input_text):
    words = input_text.split( )
    noise_free_words = [word for word in words if word not in stopwords]
    # print noise_free_words
    return noise_free_words

import_stopwords()

# from nltk.stem.wordnet import WordNetLemmatizer
# lem = WordNetLemmatizer()
# from nltk.stem.porter import PorterStemmer
# stem = PorterStemmer()
#
# word = "multiplying"
# print lem.lemmatize(word, "v")
# print stem.stem(word)

