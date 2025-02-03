# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 09:47:32 2024

@author: sai
"""

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

#24-04-2024
from numpy import array
#define matrix
A=array([
    [1,2],
    [3,4],
    [5,6]])
print(A)
#calculate transpose
c=A.T
print(c)

#INVERSE MATRIX
from numpy import array
from numpy.linalg import inv
#define matrix
A=array([
    [1.0,2.0],
    [3.0,4.0]])
print(A)
#inverse matrix
B=inv(A)
print(B)
#multiply A and B
I=A.dot(B)
print(I)

#sparse matrix
from numpy import array
from scipy.sparse import csr_matrix
# create dense matrix
A=array([
    [1,0,0,1,0,0],
    [0,0,2,0,0,1],
    [0,0,0,2,0,0]])
print(A)
#convert to sparse matrix(csr method)
S=csr_matrix(A)
print(S)
#reconstruct dense matrix
B=S.todense()
print(B)