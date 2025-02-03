# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 08:22:40 2024

@author: sai
"""
#dataframe query()
import pandas as pd
tech={
      'courses':["spark","pyspark","hadoop"],
      'fee':[2000,4000,5000],
      'Duration':["30days","40days","50days"],
      'Discount':[1000,7000,7660]
      }
df=pd.DataFrame(tech)
df
#quick examples of get the number of rows in dataframe
#most asked question in interview
rows_count=len(df.index)
rows_count
rows_count=len(df.axes[0])
rows_count
columns_count=len(df.axes[1])
columns_count
df=pd.Dataframe(tech)
row_count=df.shape[0] #return number of rows
row_count
col_count=df.shape[1] # return number of columns
print(row_count)
print(col_count)


#using dataframe.apply() to apply function and column
#here we have added the +3 number to each and every number
import pandas as pd
import numpy as np
data={"A":[1,2,3],
      "B":[4,5,6],
      "C":[7,8,9]
      }
df= pd.DataFrame(data)
print(df)
def add_3(x):
    return x+3
    return x+3 
df2 = df.apply(add_3)
df2

#if we have to add only to A column
#df=pd.DataFrame(data)
#print(df)
def add_3(x):
    return x+3 
df2=df.apply(add_3)
df2
df2=((df.A).apply(add_3)) 
df2

#using apply function single column
def add_4(x):
    return x+4 
df["B"] = df["B"].apply(add_4)
df["B"]

#apply to multiple columns
df[['A','B']]=df[['A','B']].apply(add_4)
df

#apply a lambda function to each column
df2=df.apply(lambda x : x + 10)
df2

#apply lambda function to single column
#using dataframe.apply() and lambda function
df["A"]=df["A"].apply(lambda x :x-2)
print(df)

#using pandas.dataframe.transform()
def add_2(x):
    return x+2 
df=df.transform(add_2)
print(df)

#using pandas.DataFrame.map() to single column
df['A']=df['A'].map(lambda A:A/2)
print(df)

#using numpy function on single column
#using dataframe.apply() & [] operator
df=pd.DataFrame(data)
import numpy as np 
df['A']=df['A'].apply(np.square)
print(df)

#using numpy.sqaure () method
#using numpy.sqaure() and [] operator
df['A']=np.square(df['A'])
print(df)

#pandas groupby() with example 
import pandas as pd 
tech=({
      'courses':["spark","pyspark","hadoop","python","pandas","hadoop","spark","python","NA"],
      'fee':[22000,25000,23000,24000,26000,25000,25000,22000,1500],
      'Duration':["30days","40days","50days","55days","60days","35days","30days","50days","40days"],
      'Discount':[1000,2300,1000,1200,2500,None,1400,1600,0]
      })
df=pd.DataFrame(tech)
print(df)
#use groupby() to compute the sum
# as the above dictionary we have repeated values so to combine that we use groupby()
df2=df.groupby(['courses']).sum()
print(df2)
#group by multiple columns
df2=df.groupby(['courses','Discount']).sum()
print(df2)

#ADD Index to the grouped data
# add row index to the group by reult
df2 = df.groupby(['courses','Duration']).sum().reset_index()
df2

import numpy as np 
tech={
      'courses':["spark","pyspark","hadoop","python","pandas","hadoop","spark","python","NA"],
      'fee':[22000,25000,23000,24000,26000,25000,25000,22000,1500],
      'Duration':["30days","40days","50days","55days","60days","35days","30days","50days","40days"],
      'Discount':[1000,2300,1000,1200,2500,None,1400,1600,0]
      }
df.columns
column_headers = list(df.columns.values)
print("the column header:",column_headers)
#using list(df) to get column header as a list
column_header=list(df.columns)
column_headers
column_header

#16-04-2024 session15
#pandas shuffle dataframe rows
# this technique is used in optimization
import pandas as pd
tech={
      'courses':["spark","pyspark","hadoop","python","pandas","hadoop","spark","python","NA"],
      'fee':[22000,25000,23000,24000,26000,25000,25000,22000,1500],
      'Duration':["30days","40days","50days","55days","60days","35days","30days","50days","40days"],
      'Discount':[1000,2300,1000,1200,2500,None,1400,1600,0]
      }
df=pd.DataFrame(tech)
print(df)
#pandas shuffle dataframe rows
#shuffle the dataframe rows and return all rows
df1=df.sample(frac=1) #for shuffling the function is used as sample and frac=1 means 100% if we have to do only 50% then use frac=0.5
print(df1)
# as after the shuffling everthing got shuffle so keeping that again in manner we use reset index because index also get shuffle
#create a new index starting from zero
df1=df.sample(frac=1).reset_index
print(df1)
#drop shuffle index
df1=df.sample(frac=1).reset_index(drop=True)
print(df1)


#JOINS
import pandas as pd
technologies={
    'courses':["spark","pyspark","python","pandas"],
    'fee':[2000,4000,5000,6000],
    'Duration':['30days','50days','35days','40days'],
    }
index_labels=['r1','r2','r3','r4']
df1=pd.DataFrame(technologies,index=index_labels)

technologies2={
    'courses':["spark","java","python","go"],
    'discount':[2000,2300,1200,2000]
    }
index_labels2=['r1','r6','r3','r5']
df2=pd.DataFrame(technologies2,index=index_labels2)
#pandas join
#combining two or more than two tables
#all the values present in the table will combine which are not same values there will be null values
df3=df1.join(df2,lsuffix="_left",rsuffix="_right")
print(df3)

#pandas inner join dataframes
#only same values will be displayed other will not 
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='inner')
print(df3)

#pandas left join dataframe
#left side column will display every value but in right side only same value which is present in left will be displayed other will be null
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='left')
print(df3)

#pandas right join dataframes
#rigtht side column will display every value but in left side only same value which is present in right will be displayed other will be null
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='right')
print(df3)

#using pandas.merge()
#it is same as join only join display each and every value which are not same there are null values in join but using merege only same values will be displayed no null values
df3=pd.merge(df1,df2)
print(df3)

#using datframe.merge()
df3=df1.merge(df2)
print(df3)

#use pandas.concat() to concate two dataframes
import pandas as pd
df=pd.DataFrame({'courses':["spark","pyspark","python","pandas"],
                 'fee':[20000,25000,22000,24000]})
df1=pd.DataFrame({'courses':["pandas","hadoop","hyperian","java"],
                  'fee':[2500,25200,24500,24900]})
#using pandas.concat()to connect two dataframes
data=[df,df1]
df2=pd.concat(data)
df2

#concatenate multiple dataframes using  pandas.concat()
import pandas as pd
df=pd.DataFrame({'courses':["spark","pyspark","python","pandas"],
                 'fee':[20000,25000,22000,24000]})
df1=pd.DataFrame({'courses':["pandas","hadoop","hyperian","java"],
                  'fee':[2500,25200,24500,24900]})
df2=pd.DataFrame({'Duration':['30day','40days','35days','60days','55days'],
                  'discount':[1000,2300,2500,2000,3000]})

df3=pd.concat([df,df1,df2])
print(df3)


import pandas as pd
#read excel file
df = pd.read_excel('c:/1 - python/give filename.xlsx')
print(df)
#to convert series data into array and then to list
#convert column to list
import pandas as pd
tech={
      'courses':["spark","pyspark","hadoop"],
      'fee':[2000,4000,5000],
      'Duration':["30days","40days","50days"],
      'Discount':[1000,7000,7660]
      }
df=pd.DataFrame(tech)
df
col_list=df.courses.values
print(col_list)
col_list=df.courses.values.tolist()
print(col_list)
#using series.values.tolist()
col_list=df["courses"].values.tolist()
print(col_list)

#using list fumction()
col_list=list(df["courses"])
print(col_list)

import numpy as np
#to convert to numpy array
col_list=df['courses'].to_numpy
print(col_list)