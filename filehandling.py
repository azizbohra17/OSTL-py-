
# coding: utf-8

# In[2]:


file = open("loop.txt", "r")  
file.read() 


# In[4]:


file = open('loop.txt','a') 
file.write("This will add this line") 
file.close() 


# In[9]:


with open("loop.txt", "r") as file: 
    data = file.readlines() 
    for line in data: 
        word = line.split() 
        print (word) 
file.close()


# In[10]:


with open("loop.txt", "w") as f:  
    f.write("Hello World!!!")  


# In[11]:


file = open("loop.txt", "r")  
file.read() 

