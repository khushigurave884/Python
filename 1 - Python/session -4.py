# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 08:32:28 2024

@author: sai
"""
#inserting new element in dictionary
car = {
"brand": "ford",
"model": "mustang",
"year": 1964
}
x=car.keys()
print(x)
car["color"]="white"
car
x=car.keys()
print(x)

#removing element in dictionary
# in this pop method requries key value to remove the element
car ={
"brand": "ford",
"model": "mustang",
"year" : 1964
}
car.pop("model")
print(car)

#accesssing keys in the dictinoary
for x in car:
     print(x)
     
# accessing values in the dictionary
for x in car:
       print(car[x])     

#both if we want to acess both keys and values
for key, value in car.items():
               print("%s = %s" % (key,value)) # why s here because s is the string    

# coping dictionary
car = {
"brand": "ford",
"model": "mustang",
"year" : 1964
}
car2=car.copy() 
car2              
#another way to copy dictionary
thisdict ={
    "brand": "ford",
    "model": "mustang",
    "year" : 1964
    }
dict1=dict(thisdict)
dict1

#a dictionary can contain dictionaries
# this is called nested dictionaries
# dictionary inside dictionary
our_family={
    "child1":{
        "name":"ram",
        "dob" :"08-08-2004"
        },
    "child2":{
        "name":"sham",
        "dob" :"08-08-2003"
        }
    }
our_family

#clear():remove all elements from the car
car={
    "brand": "ford",
    "model": "mustrang",
    "year": 1924
    }
car.clear()
car

#create dictionary with 3 keys
x={'key1','key2','key3'}
y=0
thisdict=dict.fromkeys(x,y)
thisdict

#get():to get the value of dictionary
car = {
       "brand":"ford",
       "model": "mustang",
       "year": 1964
       }
car.get("model")

#items() return the dictionary key value
#it will generate tuple
car ={
      "brand":"ford",
      "model": "mustang",
      "year": 1964
      }
car.items()
car.keys()#this will show you the key

# values():display all the values in dictionary
car ={
      "brand":"ford",
      "model": "mustang",
      "year": "1964"
      }
car.values()

#update():insert an item to the dictionary
#everytime new elements will be inserted at last only
car ={
      "brand":"ford",
      "model": "mustang",
      "year": 1964
      }
car.update({"color":"white"})
car
# one more example where we are replacing the value ford with wmaruti
car ={
      "brand":"ford",
      "model": "mustang",
      "year": 1964
      }
car.update({"brand":"maruti"})
car

#use of break statement
#here first i will be apple then apple will be display then i will be banana and condition is given if i==banana then break so the execution will be stop
fruits=["apple","banana","orange"]
for i in fruits:
    print(i)
    if(i=="banana"):
        break
# another example  
fruits=["apple","banana","orange"]
for i in fruits:
    if(i=="banana"):
        break 
    print(i)# only apple will be dispayed

# continue: with the continue statement
#initally it will take x=0
fruit =["apple","banana","cheery"]
for x in fruits:
    if x == "banana":
        continue
 
    print(x)#here x will skip the banana and only apple and cheery will be displayed

#range()
for x in range(2,6):
    print(x)
    
for x in range(2,30,3):
    print(x)    

# nested loop
# nested is loop inside loop
# here first colors will be displayed and we that colors fruit will be displayed
colors=["green","yellow","red"]
fruits=["guava","banana","apple"]
for x in colors:
    for y in fruits:
        print(x,y)

#function without argument
def my_function():
    print("hello from a function")
my_function() 

# function with argument
def my_function(name):
    print("hello"+name)
my_function("ram")  

# function with two arguments are calles positional arguments
def my_function(name1,name2):
    print(name1+" "+name2)
my_function("hello","world")    

#arbitrary arguments denoted by *args
# if you dont know how many agruments will be passed into your function
#then add * before the parameter name the function definition
def my_function(*kids):
    print(kids[0]+" "+kids[2])
my_function("hello","world","india") 

#kwargs denoted by **
# it is an keyword used in parameter
# a keyword argument is where you provide a name to the variable as you pass it into the function
# rather than kwargs we can use any word but we have give **
#for example
def myfun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key ,value))
myfun(first="khushi",mid="milind",last="gurave") 

# the following example shows how to use a default parameter
# if uses the dafault value:
#means if we are providing the argument then the argument will be displayed
# but we dont provide the argument then the default paramter which in this program is norway that will be displayed
def my_function(country = "norway"):
    print("i am from " + country)
my_function("sweden")
my_function("india")
my_function()
my_function("brazil")

#passing a list as an argument
#you can send any data type of argument to a function
fruits=["orange","banana","guava"]
def my_function(fruits):
    for x in fruits:
        print(x)
my_function(fruits)        

#returing values in function
# to let a function return a value use the return statement
def my_function(x):
    return x*5
my_function(5)

# pass function
#it is basically the empty function
#this is mainly used for the abstraction in algorithm
def my_function1():
    pass

#Q factorial of a  number is the product of all integer
# from 1 to that number
''' means there will be agrument pass that will be supoose 3
then that 3 will be compared with if part that is if 3==1 if no 
then it will go to else part and 3-1 will be done that will be 2
then 2 will be compare with if part it will go process till if part not comes 
1==1'''
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
factorial(3) 
factorial(6)

#########
#for interview lamba function is asked,list comprension
# a lamba function is a small anonymous function
# a lambda function can take any number of agruments,but can only have one expression
def add(a):
    sum=a+10
    return sum
add(20)
#rather than writing this with the help of the lamba function we can write
add=lambda a:a+10
print(add(30))
#one more example
add=lambda a,b,c:a+b+c+20
print(add(20,30,40))
#one more example
add=lambda a,b:a+b
print(add(20,30))

# finding odd numbers from the list using lambda
#here filter means in list we have many numbers so to acess that many numbers filter is used
#the filter() method accepts two arguments in python
# a function and an iterable such as list
lst=[34,12,64,55,75,13,63]
odd_lst=list(filter(lambda x:(x%2!=0),lst))
print(odd_lst)
# for finding even numbers 
lst=[34,12,64,55,75,13,63]
even_lst=list(filter(lambda x:(x%2==0),lst))
print(even_lst)

#square root 
lst=[34,12,64,55,75,13,63]
sqr_lst=list(map(lambda x:(x**2),lst))
print(sqr_lst)

