#!/bin/python3

import sys


def downcase_it(args):
    for text in args :
        print(text.lower())
    
if len(sys.argv)>1:
    text = sys.argv[1:]
    downcase_it(text)
else:
    print("none")
