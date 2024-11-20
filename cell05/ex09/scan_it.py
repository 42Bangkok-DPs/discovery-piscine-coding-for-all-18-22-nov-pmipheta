#!/usr/bin/env python3
import sys

text =sys.argv

if len(text)!=3:
    print("none")
else:
    first_String = text[1]
    second_String = text[2]

    ##count = second_String.count(first_String)
    count = len(refind(first_String,second_String))

    print(count)