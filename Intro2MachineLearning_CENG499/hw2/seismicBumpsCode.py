# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 17:08:54 2018

@author: Yekta
"""
#Data importing
import pickle
data = pickle.load(open('/Users/Yekta/Desktop/ODTU2/499/Hw2/seismic-bumps.pkl','rb'))
train_x = data ['train_x']
train_y = data ['train_y']
test_x = data ['test_x']
test_y = data ['test_y']

zeros=0 #In order to see how unbalanced the samples, there are 2 outputs 1s and 0s
ones=0

#To see how unbalanced the set is
for i in range(0,1722):
        train_x[i].append(train_y[i])
        
for i in range(0,1722):
        if train_x[i][18] == 0:
            zeros += 1
        else:
            ones += 1
            
#1609 0s but 113 1s
         
#Up sampling
from sklearn.utils import resample

trainMajor=[]
trainMinor=[]
for i in range(0,1722):
        if train_x[i][18] == 0:
            trainMajor.append(train_x[i])
        else:
            trainMinor.append(train_x[i])

trainMinorSampled=resample(trainMinor,replace=True,n_samples=1609) #Now the sample size of 1s and 2s are the same

for i in range(0,1609):
    trainMajor.append(trainMinorSampled[i])

def init_list_of_objects(size):
    list_of_objects = list()
    for i in range(0,size):
        list_of_objects.append(list())
    return list_of_objects

X=init_list_of_objects(3218)
Y=[]
dum=[]
import copy

for i in range(0,3218):
    Y.append(trainMajor[i][18])

for i in range(0,3218):
    for k in range(0,18):
        dum.append(trainMajor[i][k])
    X[i]=copy.deepcopy(dum)
    dum.clear()
    
#Free the memory
del i,k,dum,ones,zeros,train_x,train_y,trainMajor,trainMinor,trainMinorSampled

# Splitting the dataset into the Training set and Crossvalidation set
from sklearn.cross_validation import train_test_split
train_x, cross_x, train_y, cross_y = train_test_split(X, Y, test_size = 0.25, random_state = 0)
    
#Feature scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
train_x = scaler.fit_transform(train_x) #fit_transform In order to take mean and varianca into consideration
cross_x = scaler.transform(cross_x)
test_x = scaler.transform(test_x)


#SVM fitting
from sklearn.svm import SVC
SV = SVC(kernel = 'rbf', random_state = 0) #linear, poly, rbf, sigmoid,
SV.fit(train_x, train_y)

#Prediction of cross validations to find best algorithm
pred_y = SV.predict(cross_x)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(cross_y, pred_y)


####Prediction for test only for the best algorithm####
predFinal_y = SV.predict(test_x)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(test_y, predFinal_y)

