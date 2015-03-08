#!usr/bin/env python3

#Script implemtented in python 3.4.2
#Calculates the running mean of files in wc_input. Takes up files in alphabetical order through a file stream.


import string
import glob
import fileinput
import sys

L=[]
mid = 0
med =0

path = sys.argv[1]

rm=open(sys.argv[2],'w')

for line in fileinput.input(sorted(glob.glob(path+'/*.txt'))):  #fileinput reads each file line by line while sorted. Will select only those that have a .txt extension in their name. 
    
        
    line = line.translate(str.maketrans("","", string.punctuation)) #Strips all the punctuation from a line of text.
    line = line.split()

    nwords = len(line)
    L.append(nwords)
    L = sorted(L)

    if len(L) > 1:
       if len(L)%2 == 0:
           mid = len(L)//2
           med = float((L[mid-1] + L[mid]))/2
           
       else:
          mid = len(L)//2 
          med = float(L[mid])
          
    elif len(L) == 1:
          med = float(L[0])
              
    #print (med)
    rm.write(str(med) + '\n') 
print("med_result generated")
rm.close()  
