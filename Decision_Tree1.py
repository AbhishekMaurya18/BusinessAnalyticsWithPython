# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 20:35:08 2020

@author: Abhishek Maurya
"""


# Importing the libraries
import pandas as pd


dataset = pd.read_csv('C:/Users/DELL/Downloads/Purchase_History.csv')
dataset.head(0)
pd.get_dummies(dataset["Gender"])
S_Dummy = pd.get_dummies(dataset["Gender"],drop_first=True)
S_Dummy.head(5)
#Now, lets concatenate these dummy var columns in our dataset.
dataset = pd.concat([dataset,S_Dummy],axis=1)

#dropping the columns whose dummy var have been created
dataset.drop(["Gender",],axis=1,inplace=True)
dataset.head(5)

# Importing the dataset
X = dataset.iloc[:, [1,2,4]].values
y = dataset.iloc[:, 3].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 2)

"""
# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
"""

# Fitting Decision Tree Classification to the Training set
from sklearn.tree import DecisionTreeClassifier
#classifier = DecisionTreeClassifier(criterion = 'entropy')

#If desired we can supply extra parameters to decision trees fxn, but 
#it may or may not give better accuracy.                                    
classifier = DecisionTreeClassifier(criterion = 'entropy',max_depth = 3, min_samples_leaf=5)

classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
print(75/80)
#Accuracy = 93.75%

"""
#Rescaling my independent variables:
X_test = sc.inverse_transform(X_test)
"""

# Decision Tree visualization-----------------
from sklearn import tree

#Simple Decision Tree
#tree.plot_tree(classifier)
#image is quite blurred

#Lets try to make decision tree more interpretable by adding 'class names' and filling colors.
#cn=['0','1']
#tree.plot_tree(classifier,class_names=cn,filled = True)
#Although the Decision tree shows class name & leafs are colred but still its view is blurred.

#Lets create a blank chart of desired size using matplotlib library and place our Decision tree there.
import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=300)
cn=['0','1']
tree.plot_tree(classifier,class_names=cn,filled = True)

#if you want save figure, use savefig method in returned figure object.
fig.savefig('imagename2.png')