# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 08:16:50 2024

@author: sai
"""

#python program to print odd numbers in given range
# for odd we have to use != operator 
start, end = 4,19
# iterating each number in list
for num in range(start, end + 1):
    #checking condition
    if num % 2 != 0:
        print(num, end = " ")
       
# python program to print even number in given range
# for even we have to use == operator
start, end =4,19
for num in range(start, end + 1):
         if num % 2 == 0:
           print(num, end = " ")  
           
           
#if we are assigning value all together we have to run it all together
#for eg below code we have to run all together not only print(x) it will give you error
x,y,z = 5,6,7
print(x) 
print(y)
print(z)
#this will give you error  
x,y,z = 5
print(x)
print(y)
print(z)        

#global variables
#if we write  variable outside of the function then it is global variable
x="awesome"
def my_function():
      print("python is " +x)
my_function()  

#global and local variable
''' when there is an global variable and local variable we have to give priority to local variable
as if in down code there is gloable as well as loacl'''
x="awesome"
def my_function():
    x="fanstastic"
    print("python is "+x)
my_function()
print("python is "+x)   

#getting data types 
x=5
print(type(x))
x=range(6)
print(type(x))
#dictionary
#key value pair
x={"name":"ram","age":34}
print(type(x))

#string
""" this will give you error because one is string and the
other is integer to solve this we have to use type casting"""
str1="hello"
str2=2
str3=str1+str2
#if you want multiple strings
x="""this is python.it is very powerful"""
print(x)

#string slicing
"""slicing:application if you want to fetch the adress
of the client but only the imp part of the address will be fetch it
then convert it itno the numeric form there the slicing is used"""
x="""this is python.it is very powerful"""
print(x[2:8])
#slicing from start
x="""this is python.it is very powerful"""
print(x[:3])
#slicing from end
x="""this is python.it is very powerful"""
print(x[4:])
#negative indexing
#it will not show the -2 till -3 it will be shown beacuse it is in reversing order
x="powerful"
print(x[-5:-2])
#modify string
# if the string is in small letter we can make it to capital
x="powerful"
print(x.upper())
#to make it small
x=x.upper()
print(x.lower())

# here in down code the white space will be removed from left side
x=" this is python"
print(x.strip())
# to make correct the text 
x="hello world"
print(x.replace("hello","gello"))   
# split the space between two words 
""" if we we want only one space between them then only one space you have to give
if we want , is the delimiter which is spliting two strings we have to use ,"""
x="hello world"
print(x.split(" "))
# one more example
x="hello ,world"
print(x.split(","))

#reversings of string and gap between
x="hello world"
string1=x[::-2]
string2=x[::-1]
print(string2)
print(string1)


#to find location of any word
x="this is python and it is very powerful"
print(x.find("and"))

#string concateness
x="hello"
y="word"
print(x+y)
#to add white space 
print(x+" "+y)

#how to concatinate string with integer we have to use f operator
x=20
y="my name is khushi"
print(x+y)
#the above code will give you error because integer and string cannot mix like this so for that
#we have to use f operator 
print(f"my name is khushi and my age is {x}")
#example
quantity = 3 
item_no = 54
price=60
print(f"I want {quantity} pieces and item number is {item_no} its price is {price}")
#EXAMPLE using format method
my_order="i want {} pieces and item number is {} its price is {}"
print(my_order.format(quantity,item_no,price))
#example
#format method
quantity = 3 
item_no = 54
price=60
my_order="i want {0} pieces and item number is {1} its price is {2}"
print(my_order.format(quantity,item_no,price))

#the escape character allows you to use double quotes when
text="this is fun fair and it has got big \"round rigo\""
print(text)

# operator precedence
# RULE FOR MATHEMATICAL OPERATION
"""
P:PARANTHESIS
E:EXPONENTIAL
M:MULTIPLICATION
D:DIVSION
A:ADDITION
S:SUBSTRACTION
"""
print(3*3+3/3-3)

#PYTHON list
#it is mutable
# it has mixing
#repeated
#list is always in square bracket[]
lst=["cherry","banana","apple"]
print(lst)
#list items are indexed,the first item has index[0],the second item has index[1],the third item has index[2]
print(lst[0])
print(lst[2])

#append() adds an element at the end of the list
lst=["cheery","banana","apple"]
lst.append("mango")
print(lst)

#to remove all the items from the list
lst=["cheery","banana","apple"]
lst.clear()
print(lst)

#copy() method
lst=["cherry","banana","apple"]
lst2=lst.copy()
print(lst2)

# count() return the number of times the value is define
lst=["cheery","cheery","banana"]
lst.count("cheery")

#extend() add the elements cars to the fruits
lst=[1,2,3]
lst1=[4,5,6]
lst.extend(lst1)
print(lst)

#insert() method to add the element at the loaction you want
lst=["cheery","cheery","banana"]
lst.insert(1,"mango")
print(lst)

#pop() to remove the element at the specified position index is used
lst=["cheery","cheery","banana"]
lst.pop(2)
print(lst)

#remove() removes the item with the specified value
lst=["cheery","cheery","banana"]
lst.remove("cheery")
print(lst)

#reverse():it reverse  the list
lst=["cheery","cheery","apple"] 
lst.reverse()
print(lst)

#sort(): sort the list by alhabethical order
# it will see the first letter and if two words are having same letter it will see second letter
lst=["cheery","cheery","apple"] 
lst.sort()
print(lst)

#PYTHON TUPLE
#tuple is immutable so data cannot be changed
# mixed data types
#to change the data of the tuple we need to convert the tuple into list
#in adharcard the data is not allowed to change so it can be used there
tup=["cheery","cheery","banana"]
print(tup)
print(tup[2])

x=("cherry","cherry","apple")
x[1]="kiwi"
#it will give the error as tuple is immutable
#convert the tuple into the list
y=list(x)
y[1]="kiwi"
#convert list to tuple
x=tuple(y)
print(x)

x=("apple","banana","cherry")
print(x[1])
#to join the two tuples use the + operator
tuple1=("a","b","c")
tuple2=(1,2,3)
tup1=tuple1+tuple2
print(tup1)

#PYTHON DICTIONARY
#dictionary:it is in the form of key:value pair
# where brand is key and maruti is value
dict1={"brand":"maruti","model":"2345","year":2011}
print(dict1)
# here we are getting model in model whatever is present will be displayed with help of get
dict1.get("model")
# so here are the keys like brand,model,year
dict1.keys()
#the number of key:value pair are
print(len(dict1))
print(type(dict1))
#if you are applying the dictionary for large data suppose student data so many rollno,name,class will be required for this we can use this as colname as name and value as "abc"
dict2={"brand":["maruti","toyoto","mahendra"],"model":["a","b","c"],"year":["2011","2013","2022"]}
print(dict2)
print(len(dict2))
dict2.get("model")
dict2.keys()



 
