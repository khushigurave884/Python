# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 22:36:13 2024

@author: sai
"""
# 1 mailing address
'''write a program that displays your name and complete
mailing address formatted in the manner that you
would usually see it on the outside of an envelope.
your program does not need to read any input from user'''

x='khushi gurave'
print(x)
y='manmohan traders'
print(y)
z=int(input('rahata ,42307'))
print(z)

#2 Area of room
'''Write a program that asks the user to enter the width and length of a room. Once
the values have been read, your program should compute and display the area of the
room. The length and the width will be entered as floating point numbers. Include
units in your prompt and output message; either feet or meters, depending on which
unit you are more comfortable working with.'''

width =float(input("enter the width of the room(in meters):"))
length =float(input("enter the length of the room(in meters):"))
area = width*length
print("the area of square is",area,"square meters")

#3 Area of field
'''Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.
Hint: There are 43,560 square feet in an acre.'''

width=int(input("enter the width of farmers field(in feet):"))
length=int(input("enter the length of farmers field (in feet):"))
area=length*width
area_acres=area/43560
print("area of farners field",area_acres,"  acre")

#4 Bottle Deposits
'''In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and always displays exactly two decimal places'''

one_less=int(input("enter the number of conatiners holding the capacity of one litre or less than one liter:"))
one_more=int(input("enter the number of conatiners holding the capacity of more than one litre:"))
refund = round((one_less * 0.10) + (one_more * 0.25),2)
print(f"The refund you will get is ${refund}")

#5Tax and Tip
'''The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the values
are displayed using two decimal places.'''

meal=float(input("enter the cost of meal:"))
local_tax_rate = 0.07
tax_amount=local_tax_rate * meal
tip_rate = 0.18
tip_amount=tip_rate * meal
total_cost= meal + tax_amount + tip_rate
print(f"tax amount you will get is ${tax_amount}")
print(f"tip amount you will get is ${tip_amount}")
print(f"total cost you will get is ${total_cost}")

#6Height Units
'''Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters'''

feet=float(input("enter the number of feet:"))
inches=float(input("enter the number of inches:"))
feet_in_cm = feet*30.48
inches_in_cm = inches*2.54
total_height_cm = feet_in_cm + inches_in_cm
print(f" total height in centimeter is {total_height_cm}")











