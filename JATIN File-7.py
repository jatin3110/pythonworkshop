#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Q1. Write a program to multiply two numbers using functions.
def mul(a,b):
    c= a*b
    return(c)
a= int(input("num1 \n"))
b=int(input("num2 \n"))
c= mul(a,b)
print(c)


# In[8]:


#Q2. Write a program to add two numbers using functions.
def add(a,b):
    c=a+b
    return(c)

a= int(input("num1:\n"))
b= int(input("num2: \n"))
c= add(a,b)
print(c)


# In[1]:


#Q3. Calculate factorial of a number using fuctions.
def fact(n):
    fact=1
    for i in range(n,0,-1):
        fact= fact*i
    return(fact)

n= int(input("enter a number: \n"))
b= fact(n)
print(b)


# In[1]:


#Q4. Create a sequence of fibonacci using functions.
def fib(m):
    a=0
    b=1
    for i in range(m):
        sum=a+b
        print(sum)
        a=b
        b=sum
v= int(input("enter limit: \n"))
fib(v)


# In[6]:


#Q5. Write a program to swap two numebrs using functions.
a= int(input("value of first number:\n"))
b= int(input("value of second number:\n"))
print("a is:\n",a)
print("b is: \n",b)
temp=a
a=b
b=temp
print("after swapping")
print("value of a is:\n",a)
print("value of b is:\n", b)



# In[10]:


#Q6.Write a function to find the HCF of some given numbers.
def hcf(x,y):
    if(x<y):
        small= x
    else:
        small= y
    for i in range(1, small+1):
        if(x%i==0 and y%1==0):
            hcf=i
    return hcf

a= 22
b=44
print("hcf is:\n", hcf(a,b))
    


# In[14]:


#Q7. Write a function to find the ASCII value of the character.
a= int(input("enter value:\n "))
print(chr(a))


# In[31]:


#Q8. Write a program that demonstrates the (built in function) mathematical functions.
import math
a=5.7
b=6
print(math.ceil(a))
print(math.floor(a))
print(math.fabs(a))
print(math.factorial(b))
print(math.copysign(b,a))
print(math.gcd(6,8))


# In[36]:


#Q9. Write a program that demonstrates the (built in function) Date & Time functions.
import time
print(time.time())
print(time.gmtime())
print(time.asctime())
print(time.ctime())


# In[44]:


#Q10. Write a program that demonstrates default arguments.
def greet(name, msg = "Good morning!"):
   
   print("Hello",name + ', ' + msg)

greet("Kate")
greet("Bruce","How do you do?")


# In[45]:


#Q11.  Write a program that demonstrates keyword arguments.
def keyw(**abc):  
    for key, value in abc.items(): 
        print ("%s == %s" %(key, value)) 
  

keyw(first ='hello', mid ='and', last='bye')     


# In[4]:


#Q12.  Write a program that demonstrates default arguments.   
def defaultArg(name, line=' I am Mahika.'):
    print (name,line)
defaultArg('hello')


# In[7]:


#Q13.  Write a program that demonstrates variable-length arguments.
def arg(*args):
    result = args[0]
    for num in args:
        if num < result:
            result = num
    return result

arg(4, 8, 6, 7, 3)


# In[ ]:




