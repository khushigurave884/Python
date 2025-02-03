# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 08:20:21 2024

@author: sai
"""
lst=[]
for num in range(0,20):
    lst.append()
print(lst)
    
#import ask in interview
# what is list comrehension 
#list compreshion
#reduce space complexity so response will be good
#making multiple line code in less line
lst=[num for num in range(0,20)]
print(lst)
#one more example
names=["dada","mama","kaka"]
lst=[name.capitalize() for name in names]
print(lst)
#list comrehension with if statement
def is_even(num):
    return num%2==0
lst=[num for num in range(10) if is_even(num)]
print(lst)
#for loop inside for loop in list comrehension
lst=[f"{x}{y}" for x in range(3)for y in range(3)]
print(lst)

#Dictionary comprehension
#in dictionary compreshenion
# the logic will be writeen in left hand side and the statement will be writeen in right and side
dict={x:x*x for x in range(3)}
print(dict)

#generator
#it is another way of creating iterators
#it uses the key word yeild
#yeild is used instead of retrun
# it can also return the one value at a time
# to return one value at a time next is used
#implemented using function
gen=(x for x in range(3))
print(gen)
for num in gen:
    print(num)
#for one value at a time
gen=(x
     for x in range(3)
     )
next(gen)
next(gen)

#function which returns multiple values
def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(6):
    print(num)  
# now instead of using for loop we can write generator also
def range_even(end):
    for num in range(0,end,2):
        yield num
gen=range_even(6)
next(gen)
next(gen)
next(gen)

#chanining generators
#when we are writng password then there is hide option where star comes* so to  generate a star that we are using
def length(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:        
      yield ele*'*'
passwords=["khushi","gurave","884"]
for password in hide(length(passwords)):
    print(password)      
""" ele* appears to be placeholder for an element from an iterable
the (*) is likely just a charcater used to represent a placeholder
or a wildcard for instance,if you are iterating over a list of element
ele* could symbolize any element in that list
its a generic representation
that does not correspond to any specific syntax in python or itertolls"""

#genrating an password and hide that password
import random
noun=input("enter the name:")
adjective=input("enter the adjective:")
number=random.randrange(0,100)
password=adjective + noun+str(number)
print("your entered password is:", password)
def length(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:        
      yield ele*'*'
for i in hide(length(password)):
    print(i,end="") 
  
#enumerate
#in interview it is asked
#printing list with index
# the belowcode is in simple form
#this program will give index and list output
lst=["milk","egg","bread"]
for index in range(len(lst)):
# here index+1 is like it will start from 1 index
    print(f'{index+1} {lst[index]}')
#the below code is using enumerate
lst=["milk","egg","bread"]
for index,item in enumerate(lst,start=1):
    print(f'{index} {item}')
    
#use of zip function
name=["dada","mama","kaka"]
info=[980,4053,9785]
# here we have used nm,inf instead of this we can use i and j also beacuse it is i and j in for loop
for nm,inf in zip(name,info):
    print(nm,inf)    
# use of zip_longest
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[9850,5678,3214]
for nm,inf in zip_longest(name,info):
    print(nm,inf)
    #here output comes null in front of baba beacuse we have not inserted values so if we want instead of null something diff we can do below code
#use of fill value instead of none
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[9850,5678,3214]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)
    
#use of all() this is used when we have to find if in list there is zero value present all not
lst=[2,3,-6,8,9]
if all(lst):
    print("all values are true")
else:
    print("there are zero values")
#another one example 
lst=[2,3,-6,0,8,9]
if all(lst):
    print("all values are true")
else: 
    print("there is zero value")
    
# use of any
#this is opposite to all
# if we have to find in a list non zero value then any is used
lst=[0,0,0,9,0]
if any(lst):
    print("it has some values")
else:
    print("all values are null in the list")
    
#count()
#it is used in image processing
# in this it counts the index
from itertools import count
counter=count()
print(next(counter))
print(next(counter))
print(next(counter)) 
#lets start from 1
from itertools import count
counter=count(start=1)
print(next(counter))
print(next(counter))
print(next(counter)) 

#cycle()
#suppose you have repeated tasks then you will use this
#continuesly it will repeat
import itertools
instructions=("eat","code","sleep")
for instruction in itertools.cycle(instructions):
    print(instruction)

#repeat()
# this is used to repeat any thing for number of times
from itertools import repeat
#here msg means i
for msg in repeat('khushi gurave',times=3):
    print(msg)  
    
#combination
from itertools import combinations
players=['john','jani','janardhan'] 
for i in combinations(players,2):
    print(i)
 
#permutations    
from itertools import permutations
players=['john','jani','janardhan'] 
for i in permutations(players,2):
       print(i)

#product()
#this all are the features of itertools
# in product it will display all output with each and every element
from itertools import product
team_a=['rohit','pandya','bumrah']
team_b=['virat','manish','sami']
for pair in product(team_a,team_b):
    print(pair)

#asked in interview
#shallow copies:
#deep copies
#assignment opertion
# this will only create a new variable with the same reference
list_a=[1,2,3,4,5]
list_b=list_a
list_a[0]=-10
print(list_a)
print(list_b)

# shallow copy
#one level deep modifying one level1 does not affect
#use copy.copy() or object specific copy functions/c
import copy
list_a=[1,2,3,4,5]
list_b=copy.copy(list_a)
# not affects the other list
list_b[0]=-10
print(list_a)
print(list_b)
#but with nested objects modifying on level 2 or deep
import copy
list_a=[[1,2,3,4,5,],[6,7,8,9,10]]
list_b= copy.copy(list_a)
#affects the other!
list_a[0][0]=-10
print(list_a)
print(list_b)

#deep copies
#full independent clones use copy.deepcopy()
import copy
list_a=[[1,2,3,4,5,],[6,7,8,9,10]]
list_b=copy.deepcopy(list_a)
# not affects the other
list_a[0][0]=-10
print(list_a)
print(list_b)
  
       
      
      