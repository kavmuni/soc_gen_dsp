#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 14:05:10 2019

@author: gunnvantsaini
"""

#### Pre-assement? access? 23 June
## Not graded, some baseline from you
#### opencv, install by wednesday next week
# pip install opencv-python

### Numbers, Strings, Lists, list comprehension, maps,lambdas

### tuple,dictionary,files
a=[1,2,3,4,5] #list
t=(1,2,3,4,5) #tuple, iterables

t[0]
for i in t:
    print(i)
type(a)   
a[0]=10000
t[0]=10000

### dictionaries (hash maps, key-value pairs,iterables)
# d={'key1':data1,'kay2',data2}
d={'one':[1,2,3,4,5],'two':'string',0:['value1','value2']}
d[0]
d['one']
d['two']
d.keys()
d.values()

for i in d:
    print(i,d[i])

## create keys on the fly
d[11]=['eleven']

'''e={}
for i in seq:
    do some operation to create some key and value
    e[key]=value'''

"one" in d
23 in d

### Use assign_txt and give me the count of each word
## create a dictionary where the keys are the words and values are the counts
s="This is rpeated like This"
bw=s.split(" ")
count={}
count['The']=1
bow=assign_txt.split(" ")
d={}
for word in bow:
    if word in d:
        d[word]=d[word]+1           
    else:
        d[word]=1
### files (text files, binary, read/write) 
"D:\F1\File1.txt" ===> "D:/F1/File1.txt"
====> "D:\\F1\\File1.text" ====> r"D:\F1\File1.text"
path="/Users/gunnvantsaini/Data/Work/Python Trainings/PythonForModellers/Data/tweets_assignment.txt" 

con=open(path,"r") 
data1=con.read()
con.close()      
    
path_json="/Users/gunnvantsaini/Documents/Work/Jigsaw Academy/IPBA/Introduction R /Data/sample_json.json"

con=open(path_json,"r")
data2=con.read()
con.close()

## json, toml,yaml,xml,html
import json
data2_json=json.loads(data2)
data2_json['id']
data2_json['batters']['batter'][0]['id']

path3="/Users/gunnvantsaini/Documents/Work/large.json"

con=open(path3,"r")
data3=con.read()
data3_json=json.loads(data3)
data3_json.keys()

data3_json['features']
type(data3_json['features'])
data3_json['features'][0].keys()
data3_json['features'][0]['properties']['type']

### What if I wanted to extact type from all elements?
l=[]
for i in data3_json['features']:
    l.append(i['properties']['type'])
    
## List comprehension?
l=[i['properties']['type'] for i in data3_json['features']]

## map?
def get_type(x):
    return x['properties']['type']
list(map(get_type,data3_json['features']))

### extract lat and long?
data3_json['features'][0]

for i in data3_json['features']:
    print(i['geometry']['coordinates'][0])
    print(i['geometry']['coordinates'][1])
    