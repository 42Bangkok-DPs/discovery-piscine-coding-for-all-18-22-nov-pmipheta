#!/usr/bin/env python3
import sys

text = sys.argv

if len(text)<2:
    print("none")
else:
    if text[1]!=input("What was the parameters? "):
        print("Good job")