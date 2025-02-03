# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:06:33 2024

@author: KHUSHI GURAVE
"""

"""1. Implement a simple Named Entity Recognition (NER)
function that identifies named entities in a sentence. The
function should return a list of these named entities.
For example, given the sentence "Ramesh lives in
Mumbai", the function should return ["Ramesh",
"Mumbai"].
Text1: “James is the author of Atomic Habits”
Text2: “Aarti works at Accenture”"""

import nltk
nltk.download('punkt')
from nltk import word_tokenize
text1=word_tokenize("jamesh is the author of atomic habits")
text2=word_tokenize("aarti works at accenture")
print(text1)
print(text2)

"""2.Design a function that classifies a text as either "spam"
or "imp" (non-spam) based on the presence of certain
keywords. For example, if the text contains words like
"buy", "free", "offer", or "click", it should be classified as
"spam". If these words are not present, the text should be
classified as "imp". The function should return the
appropriate classification.
Text1: “Buy 1 Get 1 Free
Text2: “Meeting is scheduled at 12 PM ”
Text2: “Click on the link below to see the offer.”"""

import re 
text1="buy 1 get 1 free"
text2="metting is scheduled at 12pm"
text3="click on the link below to see the offer"


"""3. Create a function that should return a list of stemmed
words.
e.g [‘running’] = [‘run’]
list = [‘painful’,’standing’,’abstraction’,’magically’]"""
stemmer=nltk.stem.PorterStemmer()
stemmer.stem("painful")
stemmer.stem("standing")
stemmer.stem("abstraction")
stemmer.stem("magically")

"""4. Implement a function that takes a list of tokens (words)
and removes all stopwords from it. For example, if the
input tokens are ["This", "is", "a", "test"] and
the stopwords are ["is", "a", "the"], the function should
return ["This", "test"].
Stopwords = [“is”,”a”,”the”, “an”,”she”]
Sentence1: “an apple is on the table.”
Sentence2: “She is an engineer.”"""


import nltk
from nltk.corpus import stopwords
nltk.download('stopwords') 
stop_words=stopwords.words('English')
print(stop_words)




"""5 Perform lemmatzation on the given text
 text= "Dancing is an art. Students should be taught
dance as a subject in schools . I danced in many of my
school function. Some people are always hesitating
to dance." """
from nltk.tokenize import sent_tokenize
sent=sent_tokenize("Dancing is an art. Students should be taughtdance as a subject in schools . I danced in many of myschool function. Some people are always hesitatingto dance")
sent
