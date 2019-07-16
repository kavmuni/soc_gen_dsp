#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:13:48 2019

@author: gunnvantsaini
"""

####
# opencv, install, by wednesday's session
#### 
# Numbers, Strings, Lists,
# Common python programming constructs
# comprehension (list) # for loop alternative
# map                  # for loop alternative
# lambda functions

#### 
a=[1,2,3,4,5]
# b which contains the square of these numbers

b=[]
for i in a:
    b.append(i**2)
    
## Can we write this for loop more succintly
# list comprehension, inspired from set notation in mathematics
# {i where each i belongs to set of positive integers and i%2==0}

b=[i**2 for i in a]

# Create a list of positive cubes of a?
[i**3 for i in a]
# Create a list of all even cubes of a?
[i**3 for i in a if i%2==0]
    
## maps
#a=[a1,a2,a3,a4,a5]
#b=[f(a1),f(a2),f(a3),f(a4),f(a5)] mapping f on each element in a, map(f,a)

## Use map to get the squares of elements in a

def square(x):
    return x**2

list(map(square,a))

## Lambda functions
# trivial, you may want to define the function where it is needed
# Lambda function is an inline function (it is defined where needed, a function without a name)

## lambda arg1,arg2:arg1**2+arg2**2

## def f(arg1,arg2):
#   return arg1**2+arg2**2

f=lambda x:x**2
list(map(lambda x:x**2,a))
list(map(f,a))

### Tuples, very similar to lists with a one point of differnce, it can't be changet at place

t=("ab",67,89,32)
t[0]
for i in t:
    print(i)
a[0]=100
t[0]=123

### dictionaries, key:value pairs

d={'one':[1,2,3,4,5],'two':['a','b','c']}
d[0]
d['one']
d.keys()
d.values()

for i in d:
    print(i,d[i])
    
d['three']=['def','ghi']
d['three']=3
"three" in d
d={}
for i in seq:
    do something and get a result,key
    d[key]=result

## Count the words that exist in the assign_txt 
# create dictionary, where keys are the words and values are their counts   
count={}
bow=(assign_txt.split(" "))
for word in bow:
    if word in count:
        count[word]=count[word]+1
    else:
        count[word]=1
s="This is a sentence and we are repeating This again"
bow=s.split(" ")
count={}
bow[0] in count
count[bow[0]]=1 ## count['This']
bow[1] in count
count[bow[1]]=1
....
....
bow[8] in count
### files (write/read a stream of either text or bytes)        i/o operation
path='/Users/gunnvantsaini/Data/Work/Python Trainings/PythonForModellers/Data/tweets_assignment.txt'
p="D:/Folder1/file.txt"
p="D:\\Folder1\\file.txt"
p=r'D:\Folder1\file.text'

con=open(path,'r') 
data=con.read()       
con.close()       