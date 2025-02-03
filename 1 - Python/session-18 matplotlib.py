# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 08:43:20 2024

@author: sai
"""
#MATPLOTLIB
#SEABORN
#THERE IS PACKAGE CALLED MATPLOTLIB INSIDE THAT PYPLOT

#write a python program to draw a line with suitable label in the
import matplotlib.pyplot as plt
X=range(1,50)
Y=[value * 3 for value in X]
print("values of x:")
print(*range(1,50))
""" this is equivalant to i in range(1,50):
    print(i,end='')"""
print("values of y(thrice of x):")
print(Y)
#plot lines and/or markers to the axes
plt.plot(X,Y)
#set the  x axis label of the current axis
plt.xlabel('X-axis')
#set the  y axis label of the current axis
plt.ylabel('Y-axis')
#set a title
plt.title('draw a line')
#display the figure
plt.show()

#label in the x axis and y axis and a title
import matplotlib.pyplot as plt
#x axis values
x=[1,2,3]
#y asix values
y=[2,4,1]
#plot lines and/or markers to the axes
plt.plot(x,y)
#set the x axis label of the current axis
plt.xlabel('x - axis')
plt.ylabel('y-axis')
#set a tite
plt.title('sample graph!')
#display a figure
plt.show()

#write a python program to plot two or more lines
#on same plot with suitable legends of each line
import matplotlib.pyplot as plt
#line 1 points
x1=[10,20,30]
y1=[20,40,10]
#line 2 points
x2=[10,20,30]
y2=[40,10,30]
plt.plot(x1,y1,label="line 1")
plt.plot(x2,y2,label="line 2")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('two or more lines on same plot with suitable legend')
plt.legend()
plt.show()

#write a python program to plot two or more liens
#
import matplotlib.pyplot as plt
#line 1 points
x1=[10,20,30]
y1=[20,40,10]
#line 2 points
x2=[10,20,30]
y2=[40,10,30]
plt.plot(x1,y1,color="blue",linewidth=3,label='line1-width3')
plt.plot(x2,y2,color="red",linewidth=5,label='line1-width5')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('two or more lines with different widths and colours')
plt.legend()
plt.show()

#write a python program to plot two or more lines
#doted and dash lines
#
import matplotlib.pyplot as plt
#line 1 points
x1=[10,20,30]
y1=[20,40,10]
#line 2 points
x2=[10,20,30]
y2=[40,10,30]
plt.plot(x1,y1,color="blue",linewidth=3,label='line1-width3',linestyle='dotted')
plt.plot(x2,y2,color="red",linewidth=5,label='line1-width5',linestyle='dashed')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('two or more lines with different widths and colours')
plt.legend()
plt.show()

#markers
#markers might be circle,traingle etc
#marks telling you the trainend from which point to point
import matplotlib.pyplot as plt
#x axis values
x=[1,4,5,6,7]
#y axis values
y=[2,6,3,6,3]
#plotting the points
plt.plot(x,y,color='red',linestyle='dashdot',linewidth=3,marker='o',markerfacecolor='blue',markersize=12)
#set the y-limits of the current axes
plt.ylim(1,8)
#set the x-limits of the current axes
plt.xlim(1,8)
#naming the x-axis
plt.xlabel('x-axis')
#namin the y-axis
plt.ylabel('y-axis')
#giivng a title to my graph
plt.title('display marker')
#function to show the plot
plt.show()

#write a python programming to display
# a bar chart of the popularity of programming langauage '
import matplotlib.pyplot as plt
x=['java','python','php','javascript','c#','c++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos=[i for i, _ in enumerate(x)]
plt.bar(x_pos,popularity,color='blue')
plt.xlabel("langauages")
plt.ylabel("popuarity")
plt.title("popularity of programming langauage|n" + "worldwide,oct 2017 comapared to a year ago")
plt.xticks(x_pos,x)
#turn on the grid
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()

#for vertical bar chat
import matplotlib.pyplot as plt
x=['java','python','php','javascript','c#','c++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos=[i for i, _ in enumerate(x)]
plt.barh(x_pos,popularity,color='blue') #here if we are writing barh then 
plt.xlabel("langauages")
plt.ylabel("popuarity")
plt.title("popularity of programming langauage|n" + "worldwide,oct 2017 comapared to a year ago")
plt.yticks(x_pos,x)
#turn on the grid
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()

#same code only using uniform color
import matplotlib.pyplot as plt
x=['java','python','php','javascript','c#','c++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos=[i for i, _ in enumerate(x)] #here we are not mentioning color default is will give one colcor
plt.bar(x_pos,popularity)
plt.xlabel("langauages")
plt.ylabel("popuarity")
plt.title("popularity of programming langauage|n" + "worldwide,oct 2017 comapared to a year ago")
plt.xticks(x_pos,x)
#turn on the grid
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()


# same code only using different colors
import matplotlib.pyplot as plt
x=['java','python','php','javascript','c#','c++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos=[i for i, _ in enumerate(x)]
plt.bar(x_pos,popularity,color=['blue','red','yellow','pink','purple','black'])
plt.xlabel("langauages")
plt.ylabel("popuarity")
plt.title("popularity of programming langauage|n" + "worldwide,oct 2017 comapared to a year ago")
plt.xticks(x_pos,x)
#turn on the grid
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()

#HISTOGRAM 
#if the graph is having long line then that side is skwed it might be right or left
# this code will give the only bar graph not histogram beacuse the data is less
import matplotlib.pyplot as plt
blood_sugar=[113,85,90,150,149,88,93,115,135,80,77,82,229]
plt.hist(blood_sugar,rwidth=0.5,bins=4)
plt.hist(blood_sugar,rwidth=0.5,bins=4)
plt.xlabel("sugar levels")
plt.ylabel("number of patients")
plt.title("blood sugar chart")
plt.hist(blood_sugar,bins=[80,100,125,150],rwidth=0.95,color='blue')

#BOXPLOT
import matplotlib.pyplot as plt
import numpy as np
#creating dataset
np.random.seed(10)
data=np.random.normal(100,20,200)
fig=plt.figure(figsize=(10,7))
#creating plot
plt.boxplot(data)
#show plot
plt.show()



#to plot multiple boxplot 
#creating dataset
np.random.seed(10)
data_1=np.random.normal(100,10,200)
data_2=np.random.normal(90,20,200)
data_3=np.random.normal(80,30,200)
data_4=np.random.normal(70,40,200)
data=[data_1,data_2,data_3,data_4]
fig=plt.figure(figsize=(10,7))
#creating axes istance
ax=fig.add_axes([0,0,1,1])
#creating plot
bp=ax.boxplot(data)
#show plot
plt.show()