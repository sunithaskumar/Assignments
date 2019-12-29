#!/usr/bin/env python
# coding: utf-8

# In[22]:


# Task1 Q1 : Write a function to compute 5/0 and use try/except to catch the exceptions. 

def zero_divide():
    try:
        result = 5 / 0
        print("result is : ", result)
    except ZeroDivisionError:
        print("The divisor is zero")
  

zero_divide() 
  


# In[43]:


# Task1 Q2: Implement a Python program to generate all sentences where subject is in ["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in ["Baseball","cricket"]. 
 
# Hint: Subject,Verb and Object should be declared in the program as shown below. 
# subjects=["Americans ","Indians"] verbs=["play","watch"] objects=["Baseball","Cricket"] 
# Output should come as below: 
# Americans  play Baseball. 
# Americans  play Cricket. 
# Americans  watch Baseball. 
# Americans  watch Cricket. 
# Indians play Baseball. 
# Indians play Cricket. 
# Indians watch Baseball. 
# Indians watch Cricket. 

# define the function
def sentence_implement():
    subjects = ["Americans","Indians"]
    verbs = ["play","watch"]
    objects = ["baseball","cricket"]

    for i in subjects:
    
        for j in verbs:
               
            for k in objects:
                print(i, j, k, end = ".")
                print()

def sentence_list():
    subjects = ["Americans","Indians"]
    verbs = ["play","watch"]
    objects = ["baseball","cricket"]
    
    sentence_list = [(sub+" "+ vb + " " + ob) for sub in subjects for vb in verbs for ob in objects]
    for sentence in sentence_list:
        print (sentence+ ".")
                
# Call the function                
sentence_implement()  
print("###############################")
print()

print("This output is using the call to list comprehension function")
print()
sentence_list()
    


# In[45]:


# Task2 Q1: Write a function so that the columns of the output matrix are powers of the input vector.  
# The order of the powers is determined by the increasing boolean argument. 
# Specifically, when increasing is False, the i-th output column is the input vector raised element-wise to the power of N - i - 1. 

import numpy as np
x = np.array([1,2,3,4])
N = 4
np.vander(x,N, increasing = True)
np.column_stack([x**(N-i-1) for i in range(N)])


# In[ ]:




