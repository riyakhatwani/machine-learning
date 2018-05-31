
# coding: utf-8

# In[1]:


#!usr/bin/python
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris=load_iris()
fl_name=iris.target_names
#print(fl_name)

y=iris.target
#print(y)
z=iris.DESCR
#print(z)
w=iris.feature_names
#print(w)
s=iris.data
#print(s)
plt.xlabel("setosa")
plt.ylabel("versicolor")
plt.title("IRIS")
x1=s [0:50]
y1=s [50:100]
z1=s [100:150]
plt.scatter(x1,y1,label="setosa",color="g",marker='*')

plt.scatter(y1,z1,label="vergi",color="r",marker='*')
plt.scatter(x1,z1,label="vergin",color="y",marker='*')
plt.legend()
plt.show()

