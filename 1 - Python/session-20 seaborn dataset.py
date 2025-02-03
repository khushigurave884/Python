# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 08:37:05 2024

@author: sai
"""

#CREATING GRAPH BY MAKING DATASET
import seaborn as sns
import pandas as pd
sales=pd.read_excel('c:/1 - python/sales.xlsx')
sales.head()
sales.columns

cars=pd.read_csv('c:/1 - python/cars.csv')
cars.columns
sns.relplot(x='HP',y='MPG',data=cars)
sns.relplot(x='HP',y='MPG',data=cars,kind='line')#line plot

#to plot the boxplot with this dataset
sns.catplot(x='HP',y='MPG',data=cars,kind='box')
#
sns.catplot(x=)



#multiple correlation regression analysis
import pandas as pd
import numpy as np
import seaborn as sns
cars=pd.read_csv('c:/1 - python/cars.csv')
#Exploratry data analysis
#1.measure the central tendency
#2.measure the dispersion
#3.third moment business decision
#4.fourth moment business decision
#5.probability distribution
#6.graphical representation(Histogram,Boxplot)
cars.describe()
#plotting the boxplot 
#graphical representation
import matplotlib.pyplot as plt
import numpy as np
plt.bar(height=cars.HP,x=np.arange(1,82,1))
#DATA IS RIGHT SKEWED
sns.distplot(cars.HP)
#boxploat
plt.boxplot(cars.HP)
#there are several outliers in hp columns
#similar oerations are expected for other three columns
sns.distplot(cars.MPG)
#data is slghtly left skewed
plt.boxplot(cars.MPG)
#there are no outliers
sns.displot(cars.VOL)
#dats is slightly right distributes
plt.boxplot(cars.VOL)
sns.displot(cars.SP)
#data is slightly right distributed
plt.boxplot(cars.WT)
#there are several outliers
#now  let us plot join plot,joint plot is to show sactter
#histogram
import seaborn as sns
sns.jointplot(x=cars['HP'],y=cars['MPG'])

#now let us plot count plot
plt.figure(1,figsize=(16,10))
sns.countplot(cars['HP'])
#count plot shows how many times the each value occured
#92 hp value occured 7 times