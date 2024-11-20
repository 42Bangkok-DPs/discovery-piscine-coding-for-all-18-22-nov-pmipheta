#!/usr/bin/env python3
import sys

text = sys.argv

if len(text)==1:
    print("none")
else:
    print(f"parameters: {len(text)-1}")

    for string in text[1:]:
        print(f"{string}:{len(text)}")