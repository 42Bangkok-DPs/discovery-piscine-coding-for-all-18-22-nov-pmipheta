#!/usr/bin/env python3
import sys

text = sys.argv

if len(text)<2 :
    print("none")
else :
    for word in text[1:]:
        if not word.endswith("ism"):
            word_list = list(word)
            word_list.append('i')
            word_list.append('s')
            word_list.append('m')
            word= ''.join(word_list)
            print(word)