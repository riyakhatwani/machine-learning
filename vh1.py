
# coding: utf-8

# In[14]:


import  matplotlib.pyplot as plt

x = range(100)[0::4]
y = range(100)[0::4]
#x1 = range(200)[100::4]
#y1 = range(200)[100::4]
plt.plot(x,y,color="r",label="anger")
#plt.plot(x1,y1,color="b",label="happiness")
plt.grid(True)
plt.legend()
plt.show()

