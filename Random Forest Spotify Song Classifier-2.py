#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

# Modelling
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, ConfusionMatrixDisplay
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from scipy.stats import randint

# Tree Visualisation
from sklearn.tree import export_graphviz
from IPython.display import Image
import graphviz

songs = pd.read_csv("/Users/Adam/Downloads/archive-2/genres_v2.csv")

import os
os.environ["PATH"] += os.pathsep + 'D:/Program Files (x86)/Graphviz2.38/bin/'
from sklearn.tree import export_graphviz


# In[2]:


X = songs.loc[:, 'danceability':'duration_ms']
Y = songs['genre']

X = X.drop('type', axis = 1)
X = X.drop('id', axis = 1)
X = X.drop('uri', axis = 1)
X = X.drop('track_href', axis = 1)
X = X.drop('analysis_url', axis = 1)


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.05)


# In[3]:


rf = RandomForestClassifier()
rf.fit(X_train, y_train)


# In[4]:


y_pred = rf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


# In[5]:



for i in range(3):
    tree = rf.estimators_[i]
    dot_data = export_graphviz(tree,
                               feature_names=X_train.columns,  
                               filled=True,  
                               max_depth=2, 
                               impurity=False, 
                               proportion=True)
    graph = graphviz.Source(dot_data)
    display(graph)


# In[6]:


param_dist = {'n_estimators': randint(50,500),
              'max_depth': randint(1,20)}

# Create a random forest classifier
rf = RandomForestClassifier()

# Use random search to find the best hyperparameters
rand_search = RandomizedSearchCV(rf, 
                                 param_distributions = param_dist, 
                                 n_iter=5, 
                                 cv=5)

# Fit the random search object to the data
rand_search.fit(X_train, y_train)


# In[7]:


y_pred2 = rand_search.predict(X_test)
accuracy2 = accuracy_score(y_test, y_pred2)
print("Accuracy:", accuracy2)


# In[8]:


best_rf = rand_search.best_estimator_

# Print the best hyperparameters
print('Best hyperparameters:',  rand_search.best_params_)


# In[9]:


y_pred = best_rf.predict(X_test)

# Create the confusion matrix
cm = confusion_matrix(y_test, y_pred)

ConfusionMatrixDisplay(confusion_matrix=cm).plot()


# In[ ]:





# In[10]:


feature_importances = pd.Series(best_rf.feature_importances_, index=X_train.columns).sort_values(ascending=False)

# Plot a simple bar chart
feature_importances.plot.bar()


# In[11]:


top50 = pd.read_csv("/Users/Adam/Downloads/spotify_top50_2021.csv")

val_x = top50.loc[:, 'danceability':'duration_ms']

predictions = best_rf.predict(val_x)

