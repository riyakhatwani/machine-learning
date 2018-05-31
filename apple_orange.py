
# coding: utf-8

# In[1]:


from sklearn import tree

features=[[110,0],[120,0],[130,1],[140,1]]

output=["apple","apple","orange","orange"]

algo=tree.DecisionTreeClassifier()
trained=algo.fit (features,output)

resoutput=trained.predict([[121,1]])

print(resoutput)

