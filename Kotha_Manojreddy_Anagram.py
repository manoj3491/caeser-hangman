#!/usr/bin/env python
# coding: utf-8

# # Anagram

# In[5]:


def anagramCheck(str1, str2): 
    if len(str1)!= len(str2):
        return 0

    if sorted(str1)==sorted(str2):
        return 1
 
    return 0
str1 = input('enter the string 1:')
str2 = input('enter the string 2:')
 
if anagramCheck(str1, str2):
    print("The two strings are anagram of each other")
else:
    print("The two strings are not anagram of each other")


# In[ ]:





# In[ ]:




