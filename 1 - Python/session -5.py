# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 08:25:46 2024

@author: sai
"""
# this type of questions are asked in first round of interview
#usecases:
"""write python coding using logical operator if eelif .
so as to check height as well as so as to allow  for rolller coster
also ask user age and charge ticket accordingly"""
print("welcome to the roller coaster")
height=int(input("please enter your height is cm:"))
if height>=120:
    print("you are eligible for roller coster")
    age=int(input("enter your age in years"))
    bill=0
    if age<12:
        print("child's ticket is 5$")
        bill=5
    elif age>12 and age<18:
        print("adult ticket is 15$")
        bill=15
    elif age>18 and age<25:
        print("senior ticket is 20$")
        bill=20
    want_photo=input("do you want photo y or n:")
    if want_photo=='y':
        bill+=5
        print(f"you need to pay the{bill} in $")
    want_popcorn=input(" do you want popcorn y or n:")    
    if want_popcorn=='y':
        bill+=10
        print(f" you need to pay the{bill} in $")
    want_colddrink=input("do you want cold drink y or n:")
    if want_colddrink=='y':
        bill+=5
        print(f" you need to pay the{bill} in $")
    else:
        print(f"you need to pay the {bill} in $")
else:
    print("you are not eligible") 

""" calculate bmi""" 
height=float(input("enter your height in m:"))
weight=float(input("enter your weight in kg:"))
BMI=round((weight/(height*height)),2)
if BMI<18.5:
    print(f"you are under weight and your bmi is:{BMI}")   
elif BMI>18.5 and BMI<25:
    print(f"you are normal weight and your BMI is:{BMI}")
elif BMI>25 and BMI<30:
    print(f" you are over weight and your BMI is:{BMI}")  
elif BMI>30 and BMI<35:
    print(f"you are obsese and your BMI is:{BMI}")
elif BMI>35:
    print(f"you are clinically abese and your BMI is:{BMI}")    
else:
    print(f"you are clinically abese and your BMI is:{BMI}")

# write a program to find out is duplicate elements from list
#to check the duplicate we have to comapre the numbers present in list
# here the output will come false beacuse there is no duplicate in list like no repeated values is there
# if the list is unsorted and has duplicate values then we have to apply the another logic
# but if it is unsorted and has duplicated values but they are close to each other or one after each other then  by this logic the output is correct
lst1=[1,2,3,5,6,7]    
def is_duplicate(lst1):
    for i in range(len(lst1)-1):
        #compare current number with next number
        if(lst1[i]==lst1[i+1]):
            return True
    return False
print(is_duplicate(lst1))  
# so for sorting we have to use
lst1=[6,7,8,6,5] 
lst1.sort()
lst1
def is_duplicate(lst1):
    for i in range(len(lst1)-1):
        #compare current number with next number
        if(lst1[i]==lst1[i+1]):
            return True
    return False
print(is_duplicate(lst1))

#for leap year
def is_leap_year(year):
    if((year>0) and (year%4==0) and (year%100!=0) or (year%400==0)):
        return True
    return False
is_leap_year(2024)


#write a program to display mario pyramid
#most asked question in interview
# for simple square 
for i in range(4):
    for j in range(4):
        print("*",end=" ")
    print()
# for straight pyramid
for i in range(4):
    for j in range(i+1):
        print("*",end=" ")
    print()    
# for reverse pyramid
for i in range(4):
    for j in range(4-i):
        print("*",end=" ")
    print()    

# to find minimum value and maximum value
# python already has minimum function
lst=[23,45,2,1,5,7,8,12]
def min_max(lst):
    min=lst[0]
    for i in lst:
        if i<min:
            min=i
    print("the minimum value",min)
    
    max=lst[0]
    for i in lst:
        if i>max:
            max=i
    print("the maximum value",max)
min_max(lst)       

# write a program  to find out  where it is palindrome 
str=input("enter the string")
rev=str[::-1]
if(str==rev):
    print("it is plaindrome")
else:
   print("it is not palindrome")   
  
#for password and login
users=["manager","admin","employee","staff"]   
for user in users:
    if user=="admin":
        print(" are you want to login")
    elif user=="manager":
        print("hello manager")
    elif user=="employee":
        print("hello employee")
    elif user=="staff":
        print("hello staff")
    else:
        print("hello")
# taking input from user
#while taking input from user we do not have to take for loop
user=input("enter your post")
if user=="admin":
        print(" are you want to login")
elif user=="manager":
        print("hello manager")
elif user=="employee":
        print("hello employee")
elif user=="staff":
        print("hello staff")
else:
        print("hello")

#for making password
import string
#pick the adjectives
adjectives =["red","yellow","sleppy","slow","blue","orange"]
#pick the noun
nouns=["apple","dinosaur","ball","toaster","goat","duck"]
import random
adjective = random.choice(adjectives)
noun = random.choice(nouns)
number = random.randrange(0,100)
#select a special characater
special_char = random.choice(string.punctuation)
# create the new secure password
password=adjective + noun + str(number) + special_char
print("your new password is:", password)
#another one?
#you can use a while loop to generate
#another
print("welcome to password picker!")
while True:
    adjective = random.choice(adjective)
    noun = random.choice(nouns)
    #making noun capital
    noun=noun.upper()
    n=random.choice(nouns)
    number = random.randrange(0,100)
    #select a special characater
    special_char = random.choice(string.punctuation)
    # create the new secure password
    password=adjective + noun + str(number) + special_char
    print("your new password is:", password)
    response = input("would you like to generate another password? types y or n:")
    if response =='n':
        break
    
#adding upper letter
#making noun capital
#homework making dimond
  
           
        
 
            
        








