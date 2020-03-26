# -*- coding: utf-8 -*-
"""cancer detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BsQIEz1Y8goWfB3GaJNmn3MgsptBQr66
"""



import numpy as np
import pandas as pd

data=pd.read_csv('Breast_cancer_data.csv')

data.head()

features=data.iloc[:,:-1]
labels=data.iloc[:,-1]

print(labels)

from sklearn.model_selection import train_test_split

features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.1,random_state=45)

features_test.shape

from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

dec_model=DecisionTreeClassifier(criterion="entropy")

k_model=KNeighborsClassifier(n_neighbors=5)

dec_model.fit(features_train,labels_train)
k_model.fit(features_train,labels_train)

labels_pred_dec=dec_model.predict(features_test)
labels_pred_k=k_model.predict(features_test)

labels_pred_k

from sklearn.metrics import accuracy_score

print("The accuracy of the knn model is",accuracy_score(labels_test,labels_pred_k))
print("The accuracy of the decision tree model is",accuracy_score(labels_test,labels_pred_dec))

import pickle

pickle.dump(k_model, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))

print(model.predict(features_test))
