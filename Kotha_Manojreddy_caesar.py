#!/usr/bin/env python
# coding: utf-8

# # 1.1 Caeser_cipher

# In[13]:


message = input("Enter the message:")
    #shift = int(input("Enter the shift value :"))
def decoder(message,shift):
 
    new_message= ""
    for characters in message:
        if characters >= "a" and characters <= "z":
            pos = ord(characters) - ord("a")
            pos = (pos - shift) % 26
            new_char = chr(pos + ord("a"))
            new_message = new_message + new_char
        elif characters >="A" and characters <= "Z":
            pos = ord(characters) - ord("A")
            pos = (pos - shift) % 26
            new_char = chr(pos + ord("A"))
            new_message = new_message + new_char
        else:
            new_message = new_message + characters
        
    print("The decoded message for shift value :",j,":", new_message)
for j in range(0,26):
    decoder(message,j)# if we want to get  decoded message manually by entering ,we can swap j to shift and can enter value manually


# ## Answers
#   ### 1.2.shift value that decodes the message is :7

# ### 1.3.message is written in : latin
#    #### "Factum fieri infectum non potest"

# ### 1.4. meaning of the sentence in English is : "it is impossible for a deed to be undone"

# In[ ]:


#Ihave taken reference of example provided in class to complete the assignment

