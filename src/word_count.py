#!usr/bin/env python3

#Script implemented in python 3.4.2
#Counts the word frequency for files located in wc_input folder



import string
import glob
import fileinput
import sys

d={}

path = sys.argv[1]                 

r=open(sys.argv[2],'w') 

for line in fileinput.input(glob.glob(path+'/*.txt')): #fileinput reads each file line by line. Will select only those that have a .txt extension in their name.
    
    line = line.rstrip('\n')
    line = line.translate(str.maketrans("","", string.punctuation))
    line = line.split()

    for word in line:
        word = word.lower()
        if word in d:
           d[word] +=1
        else:
           d.update({word:1}) 

for key in sorted(d):
    #print (key + '\t' + str(d[key]) + '\n')
    r.write(key + '\t' + str(d[key]) + '\n')

print("wc_result generated")
r.close()

