#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Q!. . Write a Python script to concatenate following dictionaries to create a new one. 
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)


# In[14]:


#Q2.Write a Python script to print a dictionary where the keys are numbers between 1 and 15  and the values are square of keys.
a= dict()
for i in range(1,16):
    a[i]=i**2
print(a)


# In[17]:


#Q3. Write a Python script to concatenate following dictionaries to create a new one. 
a={1:10, 2:20}
b={3:30, 4:40}
c={}
c.update(a)
c.update(b)
print(c)


# In[ ]:




