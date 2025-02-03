# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 08:15:26 2024

@author: sai
"""

'''whenever you dont want float while division use
use double forward slash it will give you integer'''
print(100//20)
print(type(100//20))

'''but when you want only remainder part of division
use modulus operation %'''
print('modulus division 100 % 3:',100 % 13)
print('modulus division 3 % 2:',3 % 2)

#power operator examole raise to
a=5
b=3
print(a**b)

#assigment operator
'''actually refered to as compound operator as they 
combine together numeric (such as add)'''
x=0
x
x += 1 #has the same behaviour as x = x+1
x

#none value
#python has a special type
#the nontype,with a single value,none.
# is operator gives boolean true or false
winner=None
print(winner is None)
#alternatively you can also write
print(winner is not None)

winner=None
print('winner:',winner)
print('winner is None:',winner is None)
print('winner is not None:',winner is not None)
print(type(winner))

#IF indentation is not used it will give error so we have to choose indentation
# if statement
#to select use shift and down arrow
num = int(input('enter a number:'))
if num>0:
    print(num)
    
#else in an if statement
num = int(input("enter the number:"))
if num<0:
    print('it  is negative')
else:
    print('it is positive')

# use of elif
#if we want more conditions use elif
savings=float(input('enter how much you have in savings:'))
if savings ==0:
    print("sorry no saving")
elif savings < 500:
    print("well done")
elif savings < 1000:
    print("thats a tidy sum")
elif savings < 10000:
    print('welcome sir')
else:
    print('thank you')    
    
#while loop
""" while loop exists in almost all programing
languages and is used to iterative(or repeat)
one or more code statement
as long as the test condition (expression) is true """

# we use while condition till the condition is not false it will run

count = 1
print("starting") 
while count<=10:
    print(count)
    count+=1

#for loop
#loop over a set of values in a range
# which ever last number we give in range the output will come minus one than that
print('print out values in a range')
for i in range(2,10):
          print(i)
          print('done')

###################
print('only print code if all iteration completed')
num = int(input('enter a number to check for:'))
for i in range(0,16):
          if i== num:
              break
          print(i)
print('done')

# now use an 'anonymous' loop variable
# we use this loop to avoid space complexity
# no memory is allocated for anonymous variable
# here if we dont use end='' the space will be more after using that space is less
for _ in range(0,10):
           print('.',end='')
           print()
           
# if we dont use print() then the space will show horizontal  
for _ in range(0,10):
            print('.',end='')
            
           
           
    
    
    
    
    
    
    