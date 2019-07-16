#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 10:24:04 2019

@author: gunnvantsaini
"""

### Basic data structures in python
a=67
b=67.0
type(a)
type(b)

# strings: iterables (index, loop)
s='socgen'
s[0]
s[-1]
s[0:3]

# loop: statement, end with a :
for i in s:
    print(i)
    
# Object oriented nature of python
# What are the things I can do with a given object
# What are the operations I can do with a number or a string or .... in python?

# What kind of operations we can do on strings?

print(dir(s))
## dir helps me know what are the functionality associated with an object

s.upper()
s.__len__()

len(s)
    
## lists: they are like buckets
l=[3,9,8,'abc',[5,6,7,8], "anypython object"]
l[-2][0]

for i in l:
    print(i)
print(dir(l))

l.append("ghi")

len(l)

s="This is sentence one. This is sentence two"