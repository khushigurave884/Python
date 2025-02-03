# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 08:14:04 2024

@author: sai
"""

#python for data science 
""" pandas,matplotlib,numpy,seaborn"""
#python for datascience-to delete the columns to insert to update to change etc
#pandas: will work on series,columns

#SERIES:
#a series is used to model one dimensional data,
#one dimensional: many data and only one features is one dimensional 
#the series is a list in python
#the series object also has a few more bits of data,including an index and name
#means in list there is no index we are assuming but in series there is index as well as name
#in series the index can be 1,2,3 or string,dates etc but it cant be float

import pandas as pd
songs2=pd.Series([145,142,38,13],name="counts")
songs2.index    
# with index as a string
songs3=pd.Series([145,142,88,13],name="counts",
    index=['paul','john','george','ringo']) 
songs3.index
songs3   

#THE NAN VALUE:
#this value stands for not a number
#and usually ignores in arithmatic
#operations.(similar to null in sql)
#numeric column will become nan
import pandas as pd
f1=pd.read_csv('age.csv')
f1
df=pd.read_excel('C:/1 - Python/Bahaman.xlsx')
#none,nan,NaN,and null are synonymus
#the series object behaves similary to a numpy array
#numpy has no name only it will give index 
import numpy as np
numpy_ser = np.array([145,142,38,13])
songs3[1]
numpy_ser[1]
songs3.mean()
numpy_ser.mean()

#THE PANDAS SERIES DATA STRUCTURE PROVIDES
#SUPORT FOR THE BASIC CRUD
#OPERATIONS-CREATE,READ,UPDATE,AND DELETE
#CREATION
#coulmns should not have any space in between
george=pd.Series([10,7,1,22],
index=['1968','1969','1970','1970'],
name='george_songs')
george
#reading 
# to read or select the data from as series
george['1968']
george['1970']
#we can iterate over data in a series
#as well when iterating over a series
for item in george:
    print(item)
#updating series
george['1969']=68
george['1969']
george    

#deletion
# the del statement appears to have problems with duplicate index
import pandas as pd
s=pd.Series([2,3,4],index=[1,2,3])
del s[1]
s
#convert types
#string use.astype(str)
#numeric use pd.to_numeric
#integer use.astype(int),
#note that this will fail with NAN
#datetime use pd.to_datetime
songs_66=pd.Series([3.0,None,11.0,9.0],
index=['george','ringo','john','paul'],
name='counts')
songs_66.dtype
pd.to_numeric(songs_66.apply(str))
#there will be error
pd.to_numeric(songs_66.astype(str),errors='coerce')
#if we pass errors='coerce'
#we can see that it supports many formats
songs_66.dtype

#the .fillna method will replace them with a given value
songs_66=pd.Series([3,None,11,9],
index=['george','ringo','john','paul'],
name='counts')
songs_66.dtype
pd.to_numeric(songs_66.apply(str))                  
songs_66=songs_66.fillna(-1)
songs_66=songs_66.astype(int)
songs_66.dtypes
#NAN values can be dropped from series using .dropna
songs_66=pd.Series([3,None,11,9],
index=['george','ringo','john','paul'],
name='counts')
songs_66=songs_66.dropna()
songs_66

#append.combining,and joining two series
table_69=pd.Series([7,16,21,39],
index=['ram','sham','ghansham','krishna'],
name='counts')
# conacating two series together simply use the .conacat we can use .append also but this system doents allow this 
table=pd.concat([songs_66,table_69])
table

#plotting series
#this matplotlib.pyplot module insisde module matplotlib is one module and pyplt is another one and here . is insisde the module
# so for this we use as plt
#graph
import matplotlib.pyplot as plt
fig = plt.figure()
table_69.plot()
plt.legend()

#bar graph
fig=plt.figure()
table_69.plot(kind='bar')
songs_66.plot(kind='bar',color='r')
plt.legend()

#histograph
#gaussian distribution
import numpy as np
data = pd.Series(np.random.randn(500),name='500_random')
fig = plt.figure()
ax = fig.add_subplot(111)
data.hist()







