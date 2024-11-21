#!/bin/python3

import sys

def shrink(string):
    print(string[:8])

def enlarge(string):
    print(string.ljust(8,'Z'))

if len(sys.argv)<2:
    print("none")
else:
    for text in sys.argv[1:]:
        if len(text)>8:
            shrink(text) #มากกว่า 8
        elif len(text)<8:
            enlarge(text) #น้อยกว่า 8
        else:
            print(text)