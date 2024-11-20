#!/usr/bin/env python3
import sys
import re

text =sys.argv

if len(text)!=3:
    print("none")
else:
    first_String = text[1]
    second_String = text[2]

    ##count = second_String.count(first_String)
    
    count = len(re.findall(first_String,second_String)) #first string ที่ปรากฏอยุ้ใน second string

    print(count)