# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 08:38:58 2024

@author: sai
"""
# decorators are the most important interview asked questions
import pandas as pd
F1 = pd.read_csv('c:/1 - python/buzzers.csv')

#check for working directory
import os
with open('c:/1 - python/buzzers.csv')as raw_data:
    print(raw_data.read())

#reading csv data as lists
import csv
with open('c:/1 - python/buzzers.csv')as raw_data: 
    for line in csv.reader(raw_data):
        print(line) 

#reading csv data as dictionaries
#make and habit of reading csv reading
import csv
with open('buzzers.csv')as raw_data:
    for line in csv.DictReader(raw_data):
        print(line) 
        
import csv       
with open('buzzers.csv')as data:
    flights={}
    for line in data:
        k,v=line.split(',')
        flights[k]=v
flights    

#pre-requisite to decorators
def plus_one(number):
    number1=number + 1 
    return number1
plus_one(5)
#defining functions inside other functions
def plus_one(number):
    def add_one(number):
        number1=number+1
        return number1
    # here function inside function object will be created instead of giving values
    result = add_one(number)
    return result
plus_one(4)

#passing functions as arguments
#to other function
def plus_one(number):
    result1=number + 1 
    return result1
def function_call(function):
    result=function(5)
    return result
function_call(plus_one)

#function returning other function
def hello_function():
    def say_hi():
        return "khushi"
    return say_hi
#here hello is an object which is called in function  
hello=hello_function()
hello()

#need for decorators
import time 
def calc_square(numbers):
    start=time.time()
    result = []
    for number in numbers:
        result.append(number*number)
    end=time.time()
    total_time=(end-start)*1000
    print(f"total time for execution square is {total_time}")
    return result
def calc_cube(numbers):
    start=time.time()
    result = []
    for number in numbers:
        result.append(number*number*number)
    end=time.time()
    total_time=(end-start)*1000
    print(f"total time for execution cube is {total_time}")
    return result
array=range(1,1000)
out_square = calc_square(array)
out_cube = calc_cube(array)

        
        
        