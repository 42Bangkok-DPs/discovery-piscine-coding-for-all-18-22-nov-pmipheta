#!/bin/python3

import sys

def greeting(name):
    if not isinstance(name,str):
        print("Error! It was not a name.")
    else:
        print(f"Hello,{name}")

if len(sys.argv)>1:
    for args in sys.argv[1:]:
        greeting(args)
else:
    greeting()  