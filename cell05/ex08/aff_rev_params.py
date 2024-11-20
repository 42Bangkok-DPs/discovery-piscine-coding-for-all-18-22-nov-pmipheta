#!/usr/bin/env python3
import sys

text = sys.argv[1:] #ไม่รวม ชื่อไฟล์
if len(text)<2:
    print("none")
else :
    for word in reversed(text):
        print(word)