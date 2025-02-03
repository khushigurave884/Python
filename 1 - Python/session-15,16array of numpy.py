# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 08:21:29 2024
 
@author: sai
"""

#NUM PY
#numpy is used for image processing
#INTERVIEW QUESTION
#while a python list can contain different data types within a single list,all of the elements in numpy array should be homogenous
#difference between list and array:
#list is hetrogenous data
#array is homogenous data

#array in numpy
#create ndarray
import numpy as np
arr=np.array([10,20,30])
print(arr)#here the output will be [10 20 30] in array there is no comma between in it as like list have

#[] this is one dimensional array
#[[]] this is two dimensional array
#create a multi dimensional array
arr=np.array([[10,20,30],[40,50,60]])
print(arr)

# want three dimensional array
# means 3 square bracket will give three diemsnioanl array
# to specify the dimensional how many dimensional we want use ndmin
arr=np.array([10,20,30,40],ndmin=3) # instead of three we can write 5 also to see the 5 dimensional array
print(arr) 

#change the data type
# array to complex
arr=np.array([10,20,30],dtype=complex)
print(arr) 

# to find out the dimensions of an array
arr=np.array([[1,2,3,4],[7,8,6,7],[9,10,11,12]])
print(arr.ndim)
print(arr)

#finding the size of an each item present in array



#get the shape and size of the array
# to calculate size see the row and items of column
# here answer will be 8 beacuse rows are 2 and items in each row is 4 so 2*4 will be 8
arr=np.array([[10,20,30,40],[50,60,70,80]])
print("size of array is:",arr.size)

#creation of an array
arr=np.array([10,20,30])
print("array:",arr)


#creating array from list with type float
arr=np.array([[10,20,40],[30,40,50]],dtype='float')
print("array created using list:\n",arr)

#create a squence of integers using arrange()
#create a sequence of integers
#from 0 to 20 with steps of 3
arr=np.arange(0,20,3)
print("a sequential array with steps of 3:\n",arr)

#acess single element using index
arr=np.arange(11)
print(arr)
#only specific number
print(arr[2])#output will be 2
print(arr[-2])#output value will be 9

#indexing for multidimensional array
arr=np.array([[10,20,30,40,50],[20,30,50,10,30]])
print(arr)
print(arr.shape)
print(arr[1,1])#here output will be 3o as it is in the second list and the indexing starts from 0,1 so at 1 position the value is 10 
print(arr[0,4])#output 50
print(arr[1,-1])#output will be 50

#acess array elements using slicing
arr=np.array([0,1,2,3,4,5,6,7,8,9])
x=arr[1:8:2]#output starting from 1 then one number gap till 7 beacuse before 8 so 1 3 5 7 will be output
print(x)
#example
x=arr[-2:3:-1]# it will start from back and -2 till 3 and no gap
print(x)
#example
x=arr[-2:10]
print(x)

#slicing in multi dimensional array
multi_arr=np.array([[10,20,10,40],[40,50,70,90],[60,10,70,80],[30,90,40,30]])
multi_arr
multi_arr[1,2]
multi_arr[1,:]#to get the value at row 1 and column
multi_arr[:,1]#-acess the value at all rows and column
x=multi_arr[:3,::2]#columns from 0 to 3
print(x)

# 19-04-2024
#integer array indexing
arr = np.arange(35).reshape(5,7) # this will display the number from 0 to 34 within 4 rows and 7 columns
print(arr)

#Boolean array indexing
# this advanced
import numpy as np
arr = np.arange(12).reshape(3,4)
print(arr)
rows = np.array([False,True,True])# as we4 have three rows we have put the three condition that is false true true means the first row that is 0th rw will be deleted beacuse there is false written
rows
wanted_rows=arr[rows, :]
print(wanted_rows)
#for example
arr = np.arange(12).reshape(3,4)
print(arr)
rows = np.array([True,False,True])
rows
wanted_rows=arr[rows, :]
print(wanted_rows)


#numpy.asarray()
#using numpy.asarray()
#the function calls the numpy.array() function
# use asarray()
list=[20,40,60]
array=np.asarray(list)
print("array",array)
print(type(array))

# numpy array properties
#1 ndarray.shape
#2 ndarray.ndim
#3 ndarray.itemsize
#4 ndarray.size
#5 ndarray.dtype


#ndarray.shape
#to get the shape of a python numpy array use numpy
#shape
array=np.array([[1,2,3],[4,5,6]])
array
print(array.shape)

#resize the array
# this is to reshape the shape
array=np.array([[1,2,3],[4,5,6]])
array.shape=(3,2)
print(array)
#numpy also provides a numpy.reshape() function
#numpy usage
array=np.array([[1,2,3],[4,5,6]])
new_array=array.reshape(3,2)
print(new_array)

#ARITHMATIC OPERATIONS
#apply arithmatic operations on numpy arrays

#add()
arr1=np.arange(16).reshape(4,4)
arr2=np.array([1,2,3,4])

add_arr=np.add(arr1,arr2)
print(f"adding two arrays:\n{add_arr}")

#substraction
arr1=np.arange(16).reshape(4,4)
arr2=np.array([1,2,3,4])
sub_arr=np.subtract(arr1,arr2)
print(f"adding two arrays:\n{sub_arr}")

#multiple()
mul_arr=np.multiply(arr1,arr2)
print(f"multiple two arrays:\n{mul_arr}")

#divide()
div_arr=np.divide(arr1,arr2)
print(f"dividing two arrays:\n{div_arr}")

#numpy.reciprocol()
# this function returns the reciprocal of argument
#element-wise for elements with abosulte values
#larger thna 1 the resukt is always 0 because of thw way
# to perform reciprocal operations
arr1=np.array([50,3,5,1,200])
rep_arr1=np.reciprocal(arr1)
print(f"after applying reciprocal function to array:\n{rep_arr1}")

#numpy.power()
#this numpy power() function treats elements in the fitst input array
#to perform power operation
arr1=np.array([3,10,5])
pow_arr1=np.power(arr1,3)
print(f"after applying power function to array:\n{pow_arr1}")
#applying power function
arr2=np.array([3,2,1])
print("my second array:\n",arr2)
pow_arr2=np.power(arr1,arr2)
print(f"after applying power function to array:\n{pow_arr2}")

#numpy.mod()
# this function returns the remanider of
# the division of the corresponding elements
# in the input array the function
# numpy.remainder() also produces the same result
# to perform mod function
#on numpy array
import numpy as np
arr1=np.array([7,20,13])
arr2=np.array([3,5,2])
arr1 
arr1.dtype
#mod()
mod_arr=np.mod(arr1,arr2)
print(f"after applying mod function to array:\n{mod_arr}")

#create an empty array
from numpy import empty
a=empty([3,3])
print(a)

#create zero array
from numpy import zeros
a=zeros([3,5])
print(a)

import numpy as np
np.__version__

#create one array
#will use this numpy in eigen values and eigen vectors
from numpy import ones 
a=ones([5])
print(a)

#create array with vstack
#vstack means converting 1 array into second array
from numpy import array
from numpy import vstack
#create first array
a1=array([1,2,3])
print(a1)
#create second array
a2=array([4,5,6])
print(a2)
#vertical stack
a3=vstack((a1, a2))
print(a3)
print(a3.shape)

#create array with hstack
from numpy import array 
from numpy import hstack
#create first array
a1=array([1,2,3])
print(a1)
#create second array
a2=array([4,5,6])
print(a2)
#create horizontal stack
a3=hstack((a1, a2))
print(a3)
print(a3.shape)

#index array out of bonds
from numpy import array
#define array
data=array([11,22,33,44,55])
#index data
print(data[5])
#index 5 is out of bounds for axis[0]

##########################
#TO BE A GOOD DATA SCIENTIST WWHICH EVER ERROR IS THERE Solve THAT ERROR BY YOURSELF AND CREATE A FILE WHERE WRITE THE ERROR AND SOLUTION OF ERROR
#HOLYPYTHON
#HACKERRANK
###########################

#INDEX ROW OF TWO-DIMENSIONAL ARRAY
from numpy import array
#define  array
data=array([[11,22],[33,44],[55,66]])
#index data
print(data[0,])
# 0 th row and all columns 
# o/p[11 22]

#slicee a one dimensional array
from numpy import array
#define array
data=array([[11,22],[33,44],[55,66]])
print(data[1:4])

#negative slicing of a one dimensional array
from numpy import array
#define array
data=array([[11,22],[33,44],[55,66]])
print(data[-2:])

#split input and output data
from numpy import array
#define array
data=array([
    [11,22,33],
    [44,55,66],
    [77,88,99]])
#seprate data
x,y=data[:,:-1],data[:,1]
x
y
#x
# in x all rows and columns upto -1,-1 2 will be printed
"""Out[17]: 
array([[11, 22],
       [44, 55],
       [77, 88]])"""
#y
# in y all rows and -1 columns will be printed
#Out[18]: array([22, 55, 88])

    
# broadcast scalar to one dimnesional array
from numpy import array
#define array
a=array([1,2,3])
print(a)
#define scalar
b=2 
print(b)
c=a+b
print(c)

# vector l1 norm
""" the l1 norm is calculated as the num of the absolute vector values,
where the absolute value of a scalar uses
the notation |a1|,
in effect the norm
is a calculation of the manhattan distance
from the origin of the vector space 
||v||1 = |a1|+|a2|+|a3|"""
from numpy import array
from numpy.linalg import norm # linag is linear algebra
#define vector
a=array([1,2,3])
print(a)
#calculate norm
l1=norm(a,1)
print(l1)


#vector l2 norm
""" the notation for the l2 norm of a vector
x is ||x||power of 2
to calulate the l2 norm of a vector,take the square root of the
sum of the squared vector values
another name for l2 norm of a vector is euclidean distance
this is often used for calculation the error in machine learnng models"""
from numpy import array
from numpy.linalg import norm # linag is linear algebra
#define vector
a=array([1,2,3])
print(a)
#claculating norm
l2=norm(a)
print(l2)

#triangular matrices
#used in image processing
from numpy import array
from numpy import tril # triangular lower matrix
from numpy import triu # triangular upper matrix
#define square matrix
M=array([
    [1,2,3],
    [1,2,3,],
    [1,2,3]])
print(M)
#lower triangular matrix
lower=tril(M)
print(lower) # if we write only lower and not print(lower) then in output it will come comma
#upper traingular matrix
upper=triu(M)
print(upper)

#diagonal matrix
from numpy import array
from numpy import diag 
#define sqaure matrix
M=array([
    [4,2,3],
    [1,5,3,],
    [1,2,6]])
print(M)
#extract diagonal vector
d=diag(M)
print(d)
#create diagonal matrix from vector
d=diag(d)
print(d)

#identity matrix 
from numpy import identity
I=identity(3)
print(I)

#orthogonal matrix
"""the matrix is said to be an orthogonal matrix if the product
of a matrix and its transpose gives an identity value"""

from numpy import array
from numpy.linalg import inv
#define orthogonal matrix
Q=array([
    [1,0],
    [0,-1]])
print(Q)
#inverse equivalence
v=inv(Q)
print(Q.T)
print(v)
#identity equivalence
I=Q.dot(Q.T)
print(I)
