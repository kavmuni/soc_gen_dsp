#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:04:25 2019

@author: gunnvantsaini
"""

### tables--->
import pandas as pd
path="/Users/gunnvantsaini/Data/Work/Python Trainings/PythonForModellers/Data/tweets_assignment.txt"

data=pd.read_table(path,sep="|")
type(data)

## how do I know what are all the things I can do with a dataframe
print(dir(data))

### Your guesses?
# Count
# (Anything I do in SQL:group by,distinct, sort, agggregations)
# Joins
# Strings, Dates

### Iterable?
# index---> get exact rows and get exact columns
# index columns
data['Tweet_Handle']

## Both the columns
data[['Tweet_Handle','Tweet_Date']]
## table[list of column names]

## index rows, give me row number 4?
## col indexer is []
## row indexer is iloc[]
data.iloc[4] 
## How can I get data for rows 7 and 13?
data.iloc[[7,13]]
## How to get data for rows 7 and 13 and columns tweet_date and tweet_text?
data.iloc[[7,13]][['Tweet_Date','Tweet_Text']]


## get a snapshot of data: a few rows across all columns?
data.head()
## Dimensions of the file
data.shape
## Just the number of rows?
data.shape[0]
## Schema of the table you've read in
data.dtypes ##(numbers->int,float
            ## Stings-> object)