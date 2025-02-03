# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 08:16:40 2024

@author: sai
"""

#exception are basically run time error
#two types of exception 
#EXECPTIONAL HANDLING
try:
    numerator=50
    denom=int(input("enter the denominator"))
    print(numerator/denom)
    print("division performed sucessfully")
except ZeroDivisionError:
    print("denominator as zero is not allowed")
except ValueError:
    print("only intgers should be entered") 
    
#handling excpetion without naming them
try:
    numerator=50
    denom=int(input("enter the denominator"))
    quotient=(numerator/denom)
    print("division performed sucessfully")
except ValueError:
    print("only integers should be entered")
except:
    print("opps some exception raised")

#handling exception using try except else
try:
    numerator=50
    denom=int(input("enter the denominator"))
    quotient=(numerator/denom)
    print("division performed sucessfully")
except ZeroDivisionError:
    print("denominator as zero is not allowed")
except ValueError:
    print("only integers should be entered")
else:
    print("the result of division operation is",quotient)

#handling exception using try except else finally
try:
    numerator=50
    denom=int(input("enter the denominator"))
    quotient=(numerator/denom)
    print("division performed sucessfully")
except ZeroDivisionError:
    print("denominator as zero is not allowed")
except ValueError:
    print("only integers should be entered")
else:
    print("the result of division operation is",quotient) 
finally:
    print("over and out")# there is no need of giving finally we can write only print also but out of the loop

#OBJECT ORIENTED PROGRAMING IN PYTHON
#CLASS:
# a class is a collection of properties(data) and methods(procedure or functions) that operate on data
#creating object of a class
#object=classname();
#data abstraction declare the circle class have created a new data type
# can define variables(object)of that type
#properties:name,gender,occupation
#methos:speaks,sleep,do work
class human:
    def _init_(self,n,o):
        
        
    
    
    