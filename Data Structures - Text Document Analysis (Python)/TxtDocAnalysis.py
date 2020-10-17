"""
@course:            CS 2302 Data Structures
@author:            Jorge Favela
@assignment:        Lab 5
@instructor:        Dr. Olac Fuentes
Last Modified:      Sun Apr 12 21:16:57 2020
Purpose of program: Elementary analysis of text documents using hash tables
"""
# Starter code for Lab 5

import numpy as np
import os
import hash_table_chain as htc

def get_word_list(text):
    # Receives a string containing a document
    # Returns a list of strings containing the words in the document
    text = text.lower()
    word_list = []
    curr_wrd = ''
    for c in text:
        if ord(c)>=97 and ord(c)<=122:
            curr_wrd = curr_wrd+c
        else:
            if len(curr_wrd)>0:
                word_list.append(curr_wrd)
                curr_wrd = ''
    return word_list

def stopWordsList():
    with open(filename) as tf:
        return tf.read().split('\n')
    
def load_factor(h):
    numEntries = sum([len(listElem) for listElem in h.bucket])
    return round(1.0 * numEntries /len(h.bucket),3)

def fracs(h):
    emptyB=0
    LBCnt=0
    for i in h.bucket:
        if len(i)==0:
            emptyB+=1
        if len(i)>1:
            LBCnt+=1
    emptyBf=(1.0 * emptyB /len(h.bucket))
    LBCntf=(1.0 * LBCnt /len(h.bucket))
    return round(emptyBf,3), round(LBCntf,3)

def longest_bucket(h):
    longest=0
    for i in range(len(h.bucket)):
            if len(h.bucket[i])>longest:
                longest = len(h.bucket[i])
    return longest

def recCnt(h):
    return sum([len(listElem) for listElem in h.bucket])

def WlMnsSw(wl, swht):
    newL=[]
    for i in wl:
        if not (swht.insert(i,1)==-1 and swht.retrieve(i)==0):
            newL.append(i)
    return newL

def analyzeHT(h):
    EBF,LBF = fracs(h)
    print('Analysis of', filename, 'hash table')
    print('Total Buckets:', len(h.bucket), ', total records:',recCnt(h), ', load factor:', load_factor(h))
    print('Empty bucket fraction in table:', EBF)
    print('Long bucket fraction in table:', LBF)
    print('Length of longest bucket in table: ', longest_bucket(h))

def analyzeFile(wl):
    wlh=htc.HashTableChain(len(wl))
    reps=0
    repKey=wl[1]
    for w in wl:
        if wlh.insert(w,1)==-1:
            wlh.update(w,wlh.retrieve(w)+1)
        if wlh.retrieve(w)>reps:
            reps=wlh.retrieve(w)
            repKey=w
    analyzeHT(wlh)
    print('Most common word:', repKey, '- occurs', reps, 'times')
  
            
abs_dir = '.\\abstracts\\'  # abstracts folder must be in current folder. You may want to use an absolute path
file_list =  sorted(os.listdir(abs_dir)) # Abstract contains a list with all abstract file names

print()
filename='stop_words.txt'
stopWordsL = stopWordsList()

swh = htc.HashTableChain(len(stopWordsL))
for w in stopWordsL:
    swh.insert(w,0)

print()
analyzeHT(swh)

for filename in file_list:
    f = open(abs_dir+filename, 'r', encoding="utf8")
    print('\nFile:',filename)
    text = f.read()
    f.close()
    wl = get_word_list(text)
    tw=len(wl)
    wl=WlMnsSw(wl, swh)
    tnsw=len(wl)
    print('Total words:', tw, ',total non-stop-words:', tnsw)
    analyzeFile(wl)
    # # break # Uncomment to run a single iteration