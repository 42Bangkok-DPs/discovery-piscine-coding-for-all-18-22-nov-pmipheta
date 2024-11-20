#!/usr/bin/env python3
import sys

text = sys.argv

if len(text)<2:
    print("none")
else:
    input_string = text[1]

    if input_string('z')>0:
        print('z'*input_string.count('z'))