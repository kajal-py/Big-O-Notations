#!/usr/bin/env python
# coding: utf-8

# ## O(1) Constant
# 

# In[4]:


def func(values):
    print(values[1])
l=[1,[23]]         #always print 1st element of list
func(l)


# In[5]:


def func(lst):
    for val in lst:
        print(val)
l=[2,3,4,5]          #print all values in list, list of n values print n times, linear exmample
func(l)


# In[6]:


def fucn(lst):
    for item1 in lst:
        for item2 in lst:
            print(item1,item2)
l=[1,2,[3],4]          # n**2  print outs, not sutible for very large inputs, we need to be very aware of this, quadratic terms.
fucn(l)


# In[17]:


def comp(lst):
    
    print(lst[0])     #O(1)
    
    mid=len(lst)//2    #O(n/2)=O(1/2*n)      #use double slash to make it an int, for python3
    
    for val in lst[:mid]:
        print (val)
    for x in range(10):
        print("hello")    #O(10)
lst=[1,2,3,4,4,6,7,8,10]
comp(lst)


# In[18]:


#add all the O() to figure out entire big O, as n grows larger, constants become insignificant, becomes ineffective.
#O(1+n/2+10)==O(n)


# In[ ]:


#how much space an algorithm take?


# In[19]:


def create_lst(n):
    new_list=[]
    for num in range(n):
        new_list.append('new')
    return new_list


# In[23]:


create_lst(3)


# In[24]:


#space and time complexity
def j(num):                         #space complexity O(1)
    #TIME COMPLEXITY(O(N))
    for n in range(10):
        print("hello")


# In[25]:


j(10)


# In[ ]:


# big O for python data structures
#List= dynamic array, 

