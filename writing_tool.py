#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 19:11:31 2018

@author: kezzine
"""

# imports
import nltk, re, string
from nltk.stem.porter import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer
from collections import Counter
#nltk.download('wordnet')

# user inputs paragraph
pargraph_str = input('Copy paste paragraph: \n--------------------- \n ')
pargraph_str = pargraph_str.lower()

# removes punctuation and creates list of words
pargraph_str = pargraph_str.replace(',', ' ')
pargraph_str = pargraph_str.replace('.', ' ')
pargraph_str = pargraph_str.replace("'", '')
pargraph_str_split = pargraph_str.split()

# list of stop words to ignore, can add to this list
stop_words = ['a','the','and','this','of','is','to','as','in','by','an','into','it','be','on','that','at']

# removes stopwords from list
new_words = [word for word in pargraph_str_split if (word not in stop_words) 
and (word.isdigit()==False) # to remove digits
and (word != '=') # to remove equations
and ('(' not in word)] # to remove citations

# stemmers
ps = PorterStemmer()
lan = LancasterStemmer()

# lemmatizer
lm = WordNetLemmatizer()

# empty lists
new_lst_stem = []
new_lst_lem = []
new_lst_lan = []

# creates list with only stem words
for i in new_words:
    new_lst_stem.append(ps.stem(i))

for i in new_words:
    new_lst_lem.append(lm.lemmatize(i))

for i in new_words:
    new_lst_lan.append(lan.stem(i))

#counter
counter_stem = dict(Counter(new_lst_stem))
counter_lem = dict(Counter(new_lst_lem))
counter_lan = dict(Counter(new_lst_lan))

# remove when value of dict/counter is equal to 1
new_dict_stem = {key:val for key, val in counter_stem.items() if val != 1}
new_dict_lem = {key:val for key, val in counter_lem.items() if val != 1}
new_dict_lan = {key:val for key, val in counter_lan.items() if val != 1}

# output
if (bool(new_dict_stem)==False) and (bool(new_dict_lem)==False) and (bool(new_dict_lan)==False):
	print('\n No repetitions found') # prints in case no repetitions found
else:
	print('--------------------- \n')
	print('Porter stem: \n')
	for k,v in new_dict_stem.items():
	    print(k,v)
	print('\n')
	print('Lancaster stem:\n')
	for k,v in new_dict_lan.items():
	    print(k,v)
	print('\n')
	print('Wornet lem:\n')
	for k,v in new_dict_lem.items():
	    print(k,v)