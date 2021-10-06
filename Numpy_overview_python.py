#!/usr/bin/env python
# coding: utf-8

# # A Brief Overview: Numpy

# In[104]:


# Loading Numpy
import numpy as np


# ##### The Basics

# In[134]:


# initializing array
numpy_array = np.array([1,2,3])
print(numpy_array)
type(numpy_array)


# In[135]:


# two dimentional float value
b= np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)


# In[136]:


# get dimension
numpy_array.ndim


# In[137]:


b.ndim


# In[138]:


# get shape
numpy_array.shape


# In[129]:


b.shape


# In[143]:


# Accessing/Changing specific elements, rows, columns, etc
single_d = np.array([1,2,3,4,5])
print(single_d)


# In[147]:


# accessing 5th element of single_d
print(single_d[4])


# In[148]:


# Changing last elements value as 50
single_d[-1]=50;
print(single_d)


# In[146]:


# print the elements from 2nd index value to the end.
print(single[2:])


# In[154]:


two_d=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(two_d)


# In[155]:


# get specific element [row, column]

two_d[1,5] 
# or a[1,-2]


# In[156]:


# get a specific row
# first row
two_d[0,:]


# In[31]:


# get a specific column
a[:, 2]


# In[33]:


# getting little more fancy [startindex: endindex: stepsize]
a[0, 1:6:2]


# In[34]:


# mutating data
a[1,5] = 20


# In[38]:


# mutating column
a[:,2]=[99,99]


# In[39]:


a


# In[40]:


# 3-d example
b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])


# In[41]:


b


# In[42]:


b[0,1,1]


# In[157]:


# replacing
# b[:, 1, :]=[[9,9, 9]]
# indexing


# In[45]:


# initializing different types of array
np.zeros(5)


# In[46]:


np.zeros((2,3))


# In[48]:


# all 1
np.ones((4,5))


# In[49]:


# any other number
# first is shape
np.full((2,2),99)


# In[50]:


# for float
np.full((2,2),55)


# In[52]:


# random decimal number
np.random.rand(4,2)
# instead of passing tuples we pass desired shape


# In[53]:


# random integer value
np.random.randint(7)


# In[159]:


np.random.randint(7, size=(3,3))


# In[161]:


# 1-20
np.random.randint(1,20, size=(3,3))


# In[57]:


# identity matrix
np.identity(5)
# square matrix


# In[62]:


# repeating an array
arr=np.array([[1,2,3]])
r1=np.repeat(arr, 3, axis=0)
print(r1)


# In[67]:


# copying array, be careful
a= np.array([1,2,3])
b=a
b[0]=100
a
# while changing b, a also changes
# b variable points to same things as a does


# In[70]:


a= np.array([1,2,3])
b=a.copy()
b[0]=100
a


# In[162]:


# mathematics
# elements wise operation
simple_array= np.array([1,2,3,4])
simple_array + 2


# In[163]:


simple_array * 3


# In[75]:


a/2


# In[76]:


# take sin
np.sin(a)


# In[80]:


# statistics
stats = np.array([[1,2,3],[4,5,6]])
stats


# In[84]:


np.max(stats, axis = 0)
# column


# In[85]:


np.max(stats, axis = 1)
# row


# In[86]:


# sum
np.sum(stats)


# In[87]:


np.sum(stats, axis = 1)


# In[88]:


np.sum(stats, axis = 0)


# In[91]:


# reorganizing arays
before = np.array([[1,2,3,4],[5,6,7,8]])
before


# In[92]:


print(before.shape)


# In[93]:


after = before.reshape((8,1))


# In[94]:


after


# In[95]:


# vertucally stacking vectors
v1 = np.array([1,2,3,4])
v2= np.array([5,6,7,8])
np.vstack([v1,v2])


# In[100]:


# horixzontal stack
h1 = np.ones((2,4))
h2= np.zeros((2,2))
# h2 back off h1
np.hstack((h1,h2))


# In[ ]:




