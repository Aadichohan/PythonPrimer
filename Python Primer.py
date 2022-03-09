#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = "ABCD"
print(a)


# In[2]:


# Add Multi Lines in String
b = '''ABCD
XYZ'''
print(b)


# In[3]:


# Silly String with triple single quote
silly_string = ''' He Said, "Aren't can't shouldn't wouldn't"'''
print(silly_string)


# In[4]:


# Silly String with back slash
silly_string = 'He Said, "Aren\'t can\'t shouldn\'t wouldn\'t"'
print(silly_string)


# In[5]:


# Embedding VAlue in Strings
num = 100
str = "My points are %s "
print(str % num)


# In[6]:


# Embedding Multiple Values in Strings
eng = 100
math = 80
str = "I Sored in English %s  and Math %s"
print(str % (eng, math))


# In[8]:


# MUltiply String
print('a' * 4)


# In[10]:


# List
sabzi = ['Gobi','Aloo','Palak', 'Mirche']
print(sabzi)
# print specific index value
print(sabzi[1])


# In[15]:


# Store Number in List
num = [1,5,8,44]
print(num)
print(num[2])


# In[17]:


# Store String and Number in a List
num = [1,'ABD',5,'Ali',8,44]
print(num)
print(num[1])
print(num[2])


# In[18]:


# Add Item in List
num = [1,'ABD',5,'Ali',8,44]
print(num)
num.append('FF')
print(num)
print(num[2])


# In[19]:


# Delete Item from List
num = [1,'ABD',5,'Ali',8,44]
print(num)
num.append('FF')
del num[2]
print(num)


# In[20]:


# Combine 2  List
num1 = [1,'ABD',5,'Ali',8,44]
num2 = ['Ahmed','Qasim','Ashir']
print(num1 + num2)


# In[1]:


# Combine 2  List & add into 3rd variable
num1 = [1,'ABD',5,'Ali',8,44]
num2 = ['Ahmed','Qasim','Ashir']
num3 = num1 + num2
print(num3)


# In[2]:


# Can Multiply list element
num1 = [1,44]
print(num1 * 3)


# In[4]:


# Can not  Divide and Substract list element
num1 = [1,44]
print(num1 / 3)
print(num1 - 3)


# In[6]:


# Tuples are enclosed in () parenthesis and can not be updated
num = (1, 4, 5, 7)
print(num)
num[0] = 33
print(num)


# In[9]:


# Maps in Like a List & Tuples Diferrence is that it has a key Like Json Object
sportsManList = {
    'Ali' : 'Cricket',
    'Hamza' : 'Football',
    'Shaheer' : 'Tennis',
    'Aashir' : 'Hockey',
}
print(sportsManList)
# Update Value on Specific Key
sportsManList['Ali'] = 'Mobile Game'
print(sportsManList)
# Delete Value on Specific Key
del sportsManList['Ali']
print(sportsManList)


# In[ ]:




