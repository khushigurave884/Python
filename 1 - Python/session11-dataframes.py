# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 08:23:02 2024

@author: sai
"""

#DATAFRAME
#pandas dataframe is a two dimensional data structure an immutable,hetrogeneous collection of data
#pip unistall pandas
#anaconda,environments,base terminal,click on green
#to check the version of pandas
import pandas as pd
pd.__version__ 

#create dataframe
#create using constructor
#create pandas dataframe from list
import pandas as pd
tech=[["spark",2000,"30days"],
      ["pandas",2400,"40days"]
      ]
df=pd.DataFrame(tech)
print(df)
#since we have not given any label to coulmns and indexes,dataframe by default assigns
#giving columns names and index names
column_name=["courses","fee","duration"]
row_label=["a","b"]
df=pd.DataFrame(tech,columns=column_name,index=row_label)
print(df)
df.dtypes

#assign custom
#data types to columns
#set custom types to dataframe
import pandas as pd
tech={
      'courses':["spark","pyspark","hadoop","python","pandas","oracle","java"],
      'fee':[2000,4000,5000,6000,4700,5234,9000],
      'duration':["30days","40days","50days","60days","70days","80days","90days"],
      'discount':[11.8,33.4,88.8,33.5,44.6,22.7,88.3]
      }
df=pd.DataFrame(tech)
print(df.dtypes)
#convert object types to best possible types
df2=df.convert_dtypes()
print(df2.dtypes)
#change all coulmns to same type
df=df.astype(str)
print(df.dtypes)
#change type for one or multiple columns
df=df.astype({"fee":int,"discount":float})
print(df.dtypes)
#convert data type for all columns in a list
df=pd.DataFrame(tech)
df.dtypes
cols=["fee","discount"]
df[cols]=df[cols].astype("float")
df.dtypes
#ignores error
#the courses having datatype as an object if we have to convert it into int
#it gives error so to neglect that 
df=df.astype({"courses":int},errors='ignore')
df.dtypes
#generates error
#this will be generate the error
df=df.astype({"courses":int},errors='raise')
#convert feed column to numeric type
df=df.astype(str)
print(df.dtypes)
df['discount']=pd.to_numeric(df['discount'])
df.dtypes

#create dataframes from dictionary
import pandas as pd
tech={
      'courses':["spark","pyspark","hadoop"],
      'fee':[2000,4000,5000],
      'Duration':["30days","40days","50days"],
      'Discount':[1000,7000,7660]
      }
df=pd.DataFrame(tech)
df
#convert dataframe to csv
df.to_csv('data_file.csv')
#create dataframe from csv file
df=pd.read_csv('data_file.csv')

#pandas dataframe - basic operation
#create dataframe with none\null values
import pandas as pd
import numpy as np
tech={
      'courses':["spark","pyspark","java","hadoop"],
      'fee':[2000,4000,np.nan,5000],
      'Duration':["30days","40days","50days","60days"],
      'Discount':[1000,7000,7660,8000]
      }
row_labels=['r0','r1','r2','r3']
df=pd.DataFrame(tech,index=row_labels)
print(df)



