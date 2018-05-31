
# coding: utf-8

# In[ ]:


import pyttsx 
while True :
 eng=pyttsx.init()
 msg=raw_input("enter")
 eng.say(msg,'')
 eng.runAndWait() 
    

