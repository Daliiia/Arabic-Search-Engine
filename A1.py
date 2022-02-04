# -*- coding: utf-8 -*-
"""
this corpus is "Khaleej-2004", an arabic corpus in with 4 categories 
this assignment includes Sports category 
there will be a sample input text in folder to help testing the code

"""

from nltk.corpus import PlaintextCorpusReader
from collections import Counter, defaultdict
import os


corpus_root = os.getcwd() + "/"
file_ids = ".*.html"
corpus = PlaintextCorpusReader(corpus_root, file_ids)

model = defaultdict(lambda: defaultdict(lambda: 0))

words=corpus.raw().split()
#print(words)

for i in range(len(words)-2):
     model[(words[i],words[i+1])][words[i+2]]+=1
    

for w1_w2 in model:
    total_count = float(sum(model[w1_w2].values()))
    for w3 in model[w1_w2]:
        model[w1_w2][w3] /= total_count

w= input("")
text=w.split()
w1,w2=text


dic=dict(model[w1,w2])
#print(dic)

for key, value in sorted(dic.items(), key=lambda item: item[1],reverse=True):
    #print("%s %s %s" % (w1, w2,key))
    dic=dict(model[w2,key])
    for k, va in sorted(dic.items(), key=lambda item: item[1],reverse=True):
         print("%s %s %s %s" % (w1, w2,key,k))
         break
     