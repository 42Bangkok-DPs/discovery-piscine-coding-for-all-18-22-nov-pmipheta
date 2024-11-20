#!/usr/bin/env python3
import sys

text = sys.argv

if len(text)<2 :
    print("none")
else :
    for word in text[1:]:
        if not word.endswith("ism"):
            word.append("i")
            word.append("s")
            word.append("m")
            print("",join(word))