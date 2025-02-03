# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 08:40:05 2024

@author: sai
"""


#1.Write a Python function that takes two lists and returns True if they have at least one common
member.
def have_common_member(list1,list2):
    return any(item in list1 for item in list2)
list1=[1,2,3,4,5]
list2=[5,6,7,8,9]
print(have_common_member(list1,list2))

#2. Use list comprehension to construct a new list but add 6 to each item.
a=[1,2,3,4,5]
new_list=[x+6 for x in a]
print(new_list)

#3.Write a Python program to reverse a string.
def reverse_string(string):
    retrun string[::-1]
original_string = "Hello, World!"
reversed_string = reverse_string(original_string)
print("Original string:", original_string)
print("Reversed string:", reversed_string)

4. Write a Python program to iterate over dictionaries using for loops.
my_dict = {'apple': 3, 'banana': 5, 'orange': 2}

# Iterate over the dictionary
for key, value in my_dict.items():
    print(key, "", value)

#5. Using dict comprehension and a conditional argument create a dictionary from the current dictionary where only the key:value pairs with value above 2000 are taken to the new dictionary.
my_dict={}
6. Open the file data.txt using file operations.
#7. Define a array ,data = array([11, 22, 33, 44, 55]) find 0 th index 4 th index data
arr=[1,2,3,4,5,6,7]
print(arr[0])
print(arr[4])

#8. Write a Python program to filter a list of integers using Lambda.
"""Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]"""
def original_list=[1,2,3,4,5,6,7,8,9,10]:
    if(original_list is %2==0):
        print("even_list is:")
        
    
    


#9. Write a Pandas program to create the specified columns and rows from a given data frame.
"""name': ['Anna', 'Dinu', Ramu', 'Ganu', 'Emily', 'Mahesh', 'Jayesh', ‘venkat', 'Ajay', 'Dhanesh']
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19]
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1]
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']"""
import pandas as pd
import numpy as np
data={
      'name':['Anna', 'Dinu', 'Ramu', 'Ganu', 'Emily', 'Mahesh', 'Jayesh', 'venkat', 'Ajay', 'Dhanesh'],
      'score':[12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
      'attempts':[1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
      'qualify':['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],
      }
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df=pd.DataFrame(data,index=labels)
print(df)
column_name=["name","score","attempt","qualify"]
row_label=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df=pd.DataFrame(data,columns=column_name,index=row_label)
print(df)
df.dtypes

#10. Define a array data = array([11, 22, 33, 44, 55]) and slice it from 1 to 4
array=[11,22,33,44,55]
print(array[1:4])





