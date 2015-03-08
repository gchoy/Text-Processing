#!/usr/bin/env bash

#import filename
#import glob
#import sys
#import string

chmod a+x ./src/word_count.py
chmod a+x ./src/running_median.py

# finally I'll execute my programs, with the input directory wc_input and output the files in the directory wc_output
python3 ./src/word_count.py ./wc_input ./wc_output/wc_result.txt
python3 ./src/running_median.py ./wc_input ./wc_output/med_result.txt
