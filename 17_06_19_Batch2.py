#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 14:05:01 2019

@author: gunnvantsaini
"""

### semi-structured data files: json,xml(xml,lxml)?
## pandas (tabular data)
import pandas as pd
path="/Users/gunnvantsaini/Data/Work/Python Trainings/PythonAdvanced/Data/tweets_assignment.txt"
f=open(path,'r')
data=f.read()
f.close()

table=pd.read_table(path,sep="|") ## dataframe===sqltable===excelsheet

## If you have a sql/excel sheet?
# Query
# Sort
# Filter
# Pivot (group by aggregations)
# Copy a part
# Update a column or a row
# Aggregations

### How would I know what are the different kinds of things I can do with a dataframe?

## Basic methods that are very handy
table.head(5)
## I wanted to know names of the columns
table.columns
## Is dataframe an interable? (Select columns, Select Row(s))
table['Tweet_Date']

table[['Tweet_Date','Tweet_Handle']] ## list of colnames

## Select row label is 6? (Separate indexer function to work with rows and cols)

table.iloc[6]
## Get rows 6 and 16?
table.iloc[[6,16]]

for i in table.values:
    print(i)
    
path="https://datafaculty.s3.us-east-2.amazonaws.com/Store.csv"  
d=pd.read_csv(path)
d.to_csv("Store.csv",index=False)  