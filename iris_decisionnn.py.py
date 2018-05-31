
# coding: utf-8

# In[1]:


from sklearn.datasets import load_iris
from sklearn import tree
import numpy as np
iris=load_iris()
x= [0,50,100]
train_data=np.delete(iris.data,x,axis=0)
train_target=np.delete(iris.target,x)
print(train_data.size)
test_data=iris.data[x]
test_target=iris.target[x]
print(test_data)
clf=tree.DecisionTreeClassifier()
trained=clf.fit(train_data,train_target)
predicted=trained.predict(test_data)
print(predicted)
import graphviz
out_data=tree.export_graphviz(clf, 
                              out_file=None, 
                              feature_names=iris.feature_names, 
                              class_names=iris.target_names,filled=True,rounded=True,special_characters=True)
graphviz.files.Source(out_data)

