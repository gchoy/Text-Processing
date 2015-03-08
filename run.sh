#!/usr/bin/env bash



chmod a+x ./src/word_count.py
chmod a+x ./src/running_median.py

#Executes word count and running median scripts
python3 ./src/word_count.py ./wc_input ./wc_output/wc_result.txt
python3 ./src/running_median.py ./wc_input ./wc_output/med_result.txt
