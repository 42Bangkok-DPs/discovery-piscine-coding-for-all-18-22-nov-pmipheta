#!/usr/bin/env python3
import sys

text = sys.argv
 
if len(text)==3 :
    input1=int(text[1])
    input2=int(text[2])

    result=[]

    for i in range(input1,input2+1):
        result.append(i)
    print(result)
else:
    print("none")