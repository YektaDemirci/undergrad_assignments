# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 12:06:41 2018

@author: Yekta
"""
#Data importing
import pickle
data = pickle.load(open('/Users/Yekta/Desktop/ODTU2/499/Hw2/phishing.pkl','rb'))
train_x = data ['train_x']
train_y = data ['train_y']
test_x = data ['test_x']
test_y = data ['test_y']

zeros=0 #In order to see how unbalanced the samples, there are 2 outputs 1s and 0s
ones=0
minus=0

#To see how unbalanced the set is
for i in range(0,901):
        train_x[i].append(train_y[i])
        
for i in range(0,901):
        if train_x[i][9] == 0:
            zeros += 1
        elif train_x[i][9] ==1:
            ones += 1
        else:
            minus += 1
#468 -1s, 365 1s, 68 0s.
            
#Up sampling
from sklearn.utils import resample

trainMajor1=[]
trainMajor2=[]
trainMinor=[]

for i in range(0,901):
        if train_x[i][9] == -1:
            trainMajor1.append(train_x[i])
        elif train_x[i][9]==1:
            trainMajor2.append(train_x[i])
        else:
            trainMinor.append(train_x[i])

trainMinorSampled=resample(trainMinor,replace=True,n_samples=468) #Now the sample size of 0s and -1s are the same

for i in range(0,468):
    trainMajor1.append(trainMinorSampled[i])
for i in range(0,365):
    trainMajor1.append(trainMajor2[i])

def init_list_of_objects(size):
    list_of_objects = list()
    for i in range(0,size):
        list_of_objects.append(list())
    return list_of_objects

X=init_list_of_objects(1301)
Y=[]
dum=[]
import copy

for i in range(0,1301):
    Y.append(trainMajor1[i][9])

for i in range(0,1301):
    for k in range(0,9):
        dum.append(trainMajor1[i][k])
    X[i]=copy.deepcopy(dum)
    dum.clear()
    
#Free the memory
del i,k,dum,ones,zeros,train_x,train_y,trainMajor1,trainMajor2,trainMinor,trainMinorSampled,minus

# Splitting the dataset into the Training set and Crossvalidation set
from sklearn.cross_validation import train_test_split
train_x, cross_x, train_y, cross_y = train_test_split(X, Y, test_size = 0.33, random_state = 0)
    
#SVM fitting (linear, poly, rbf, sigmoid)
from sklearn.svm import SVC
SV = SVC(kernel = 'poly', random_state = 0) 
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

