#!/usr/bin/env python3
import sys 

text = sys.argv

if len(text) != 2:
    print("none")
else:
    print(text[1].lower()) 