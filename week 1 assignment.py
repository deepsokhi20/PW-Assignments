#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#quetion1
string_a = 'Name'
list_b = [1,2,3,4,"pwskills", "tony stark", True]
float_c = 98.78
tuple_d = ('cherry', 'grapes', 'pineapple')


# #question2
# 1. string
# 2. string
# 3. list
# 4. int

# #Question3
# 1. / = it divides the two numbers and give the result in decimal or a float value
# 2. % = it gives the remainder.
# 3. // = it divides two numbers and give the result of int type.
# 4. ** = this operator solves any power of a number

# In[1]:


#question4
l = [2,3,4,5,6, "iron man", "spider man", 45.78, True, False]
for i in l:
    print(i)
    print(type(i))


# In[5]:


#question6
range(26)
print(list(range(26)))


# In[11]:


l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
for i in l:
    if i% 3 == 0:
        print('element is divisible by 3', i)
else:
    print("element is not divisible by 3", i)


# #question7
# 1. mutable data types are the data type in which we can insert or delete the element but in immutable we can neither add nor delete the data once declared.
# 

# In[13]:


#list is a mutable data type
list1= [2,3,4,5,'pwskills']
list1.append('ironman')
print(list1)


# In[14]:


#tuples are immutable data type
tuples= ('chrerry','grapes')
tuples.append('pineapple')


# In[16]:


#question 5
A = 20
B = 2
c= 0
while A>=0:
    prev_A = A
    A = A - B
    c+=1
c-=1
if prev_A==0:
    print("Divisible by", c,"times")
else:
    print("not divisible")


# In[ ]:




