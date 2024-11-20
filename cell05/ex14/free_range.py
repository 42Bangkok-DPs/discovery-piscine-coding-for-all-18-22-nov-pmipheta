#!/usr/bin/env python3
import sys

text = sys.argv
 
if len(text)==3 :
    for i in range(text[1],text[2]+1):
        print(i)