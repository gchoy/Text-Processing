#!usr/bin/env python3


#Word_count with file streaming implemented for python 3.4
#Implementing sys.argv variables

import string
import glob
import fileinput
import sys

d={}

path = sys.argv[1]                 

r=open(sys.argv[2],'w') 

for line in fileinput.input(glob.glob(path+'/*.txt')):
    
    #print line
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

