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

#DataFrame properties
df.shape
#(4,4)
df.size
#16
df.columns
df.columns.values
df.index
df.dtypes
df.info
#understanding business(objective)
#1understanding,objective
#2data dictionary
#3EDA(exploratory data analysis)
#4data processing
#model
#6Evaluation
#7deploy
#8monitoring and maintanince

#accessing one column contents
df['fee']
#accessing two columns content
df[['fee','Duration']]
#or
cols=[['fee','Duration']]
df[cols]
df[['fee','Duration']]

#select ceratin rows and assign it to another dataframe
df2=df[2:]
df2=df[:2]
df2
#df[rows,columns]
#df[: ; :]
#df[:7]
#accessing certain cell from column duration
df['Duration'][3]
#sustracting specific value from a column
df['fee']=df['fee']-500
df['fee']
#pandas to manipulate dataframe
#describe dataframe
#describe dataframe for all numeric columns
df.describe()
#it will show 5 number summary
#it describes about the mean,medium,standard deviation

#rename()-rename pandas dataframe columns
df=pd.DataFrame(tech,index=row_labels)
df.columns=['a','b','c','d']
df
#rename column names using rename() method
df=pd.DataFrame(tech,index=row_labels)
df.columns=['A','B','C','D']
df2=df.rename({'A':'c1','B':'c2'},axis=1)
df2=df.rename({'C':'c3','D':'c4'},axis='columns')
df2=df.rename(columns={'A':'c1','B':'c2'})
df2

#drop dataframe rows and columns
df=pd.DataFrame(tech,index=row_labels)
#drop rows by label
df1=df.drop(['r1','r2'])
df1
#delete rows by position/index
df1=df.drop(df.index[1])
df1
df1=df.drop(df.index[[1,3]])
df1
#delete rows by index range
df1=df.drop(df.index[2:])
df1
#when you have default indexes for rows
df=pd.DataFrame(tech)
df1=df.drop(0)
df1
df=pd.DataFrame(tech)
df1=df.drop([0,3],axis=0)
df1
df1=df.drop(range(0,2))#it will delete the 0 and 1
df1

#drop column by name
#drops "fee" column
import pandas as pd
tech={
      'courses':["spark","pyspark","hadoop"],
      'fee':[2000,4000,5000],
      'Duration':["30days","40days","50days"],
      'Discount':[1000,7000,7660]
      }
df=pd.DataFrame(tech)
df
df2=df.drop(["fee"],axis=1)
print(df2)

#droping of columns by index
print(df.drop(df.columns[1],axis=1))
df=pd.DataFrame(tech)
#using inplace=true
df.drop(df.columns[2],axis=1,inplace=True)
print(df)
#explicitly using parameter name 'labels'
df2=df.drop(labels=["fee"],axis=1)
#alternatively you can also use columns instead of labels
df2=df.drop(columns=["fee"],axis=1)

#drop two or more columns by labels name
df2=df.drop(["courses","fee"],axis=1)
print(df2)

#drop two or more columns by index
df=pd.DataFrame(tech)
df2=df.drop(df.columns[[0,1]],axis=1)
print(df2)

#drop columns from list of columns
df=pd.DataFrame(tech)
df.columns
liscol=["courses","fee"]
df2=df.drop(liscol,axis=1)
print(df2)

#remove columns from dataframe inplace
#first initialize the dataframe
df=pd.DataFrame(tech)
df.drop(df.columns[1],axis=1,inplace=True)
df

#interview question:iloc and loc diff also
#pandas select rows by index(position/labels)use of iloc
import pandas as pd 
import numpy as np
tech=({
      'courses':["spark","pyspark","java","hadoop"],
      'fee':[2000,4000,np.nan,5000],
      'Duration':["30days","40days","50days","60days"],
      'Discount':[1000,7000,7660,8000]
      })
row_labels=['r0','r1','r2','r3']
df=pd.DataFrame(tech,index=row_labels)
print(df)

#example

between 0 and 2 (exculding 2 ) should be returned
df=pd.DataFrame(tech,index=row_labels)
df2=df.iloc[:,0:2]
df2

#this line uses the slicing operator to get dataframe
#items by index
#the first slice [:] indicates to return all rows
#the second slice specifies that only columns 
#between0 and 2(exculding 2)should be returned
df2=df.iloc[0:2, :]
df2
#in this case the first slice[0:2]is
#requesting only rows 0 through lof the dataframe
#the second slice[:] indicates that akk columns are required
#slicing specific rows and columns using iloc attribute
df3=df.iloc[1:2,1:3]
df3
#another example
df3=df.iloc[:,1:3]
df3
# the second operator [1:3] yeilds columns 1 and 3 only
#select rows by integer index
df2 = df.iloc[2] # select rows by index
df2

df2=df.iloc[[2,3,6]] #select rows by index list
df2=df.iloc[1:5] # select rows by integer index range
df2=df.iloc[:1] #select first rows
df2=df.iloc[:3] #select first rows
df2=df.iloc[-1:] # select last row







































































































































































































































































































































































































































































































































































































































































































































































































































































