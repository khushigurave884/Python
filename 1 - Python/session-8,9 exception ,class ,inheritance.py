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
#constructor dont return the value but function does
class human:
    def __init__(self,n,o):
        self.name=n
        self.occupation=o
    def do_work(self):
        if self.occupation=="tennis player":
            print(self.name,"plays tennis")
        elif self.occupation=="actor":
            print(self.name,"shoots film")
    def speaks(self):
        print(self.name,"says how are you?")
tom=human("tom_crusie","actor")
tom.do_work()
tom.speaks() 
maria=human("maria_sharapova","tennis player")
maria.do_work() 
maria.speaks()     
        
#INHERITANCE
#single inheritance
#base class and from that derive class is created
class vehicle:
    def general_usage(self):#here self is the refrence
        print("general use: transporation")
class car(vehicle):
    def __init__(self):
        print("i am car")
        self.wheels=4
        self.has_roof=True
    def specific_usage(self):
        self.general_usage()
        print("specific use:commute to work,vacation with family")
class motorcycle(vehicle):
    def __inhit__(self):
        print("i am motor cycle")
        self.wheels=2
        self.has_roof=False
    def specific_usage(self):
        self.general_usage()
        print("specific use:local communication,racing")
c=car()
m=motorcycle()
c.specific_usage()
m.specific_usage() 

#multiple inheritance
class father():
    def skills(self):#this is not constructor
        print("i like gardening,programming")
class mother():
    def skills(self):# this is not constructor
        print("i like cooking,art")
class child(father,mother):
    def  skills(self):
        father.skills(self)#here we have called the classes
        mother.skills(self)
        print("i like sports")
c=child()
c.skills()        


      
        
        

        
    
    
   
    
   