# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 08:36:58 2024

@author: sai

# PYTHON IS CASE SENESITIVE LANGAUGAE
"""
print("hello world")
#variable
"""types of numbers 
there are three types used to reperesent
number in python 
these are integers (or integral) types floating 
point numbers and complex numbers"""
x=1
print(x)
print(type(x))

''' the input() function always returns a string
if we want to ask the user to input an integer number,
then ww will need to convert the string returend from the input()
function into an int.we can do this by wrapping the call to the input()
function in a call to the int() function'''

age = input('enter your age')
print(type(age))
print(age)

age1 =int(input('enter your age'))
print(age1)
print(type(age1))

age2 =int(input('enter your age'))
print(age2)
age=age1+age2#addition is done
print(age)
''' if we do not do type casting there will be concatination'''

#floating point numbers
exchange_rate = 1.83
print(exchange_rate)
print(type(exchange_rate))     

#converting to floats
#as with integers it is possible to convert other
# types such as an int or a string into a float
int_value = 100
string_value = '1.5'
float_value = float(int_value)
print('int value as a float:',float_value)
print(type(float_value))
float_value = float(string_value)
print('string value as a float:',float_value)
print(type(float_value))

#complex number
#it is real number+imaginary number
c1 = 1 
c2 = 2j
print('c1:',c1,',c2:',c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)

#boolean values
# a boolean type can only be one of true or false
all_ok = True
print(all_ok)
all_ok = False
print(all_ok)
print(type(all_ok))

#you can convert strig into booleans as long
#true or false (and nothing else)
status = bool(input('ok it is confirmed?:'))
print(status)
print(type(status))
'''here while running we have to put yes or no afterthe ok it is confirmed then 
then it will give you true status and if we do not put the input then it is coming false'''

#arithmatic operation
home = 10
away = 15
print(home + away)
print(type(home + away))
#multiplication
print(10*4)
print(type(10*4))
#substraction
goals_for = 10
goals_against = 7
print(goals_for -goals_against)
print(type(goals_for - goals_against))
#division
print(100/20)
print(type(100/20))

