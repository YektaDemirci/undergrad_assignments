"""
nbapredict1617.py
METU CENG499 Project
Author : Yekta Demirci (yektademirci@hotmail.com), İlayda Beyreli(ilaydabeyreli@gmail.com)
         Burak Kaan Bilgehan(), Cemal Erat()
Date(dd/mm/yyy): 19/05/2018
Description :
"""
import numpy as np
import pandas as pd
import matplotlib

from keras.models import model_from_json
import sys

data = pd.read_csv('data_20162017.txt', sep=" ", header=None)
data.head()

train_data = data[:1230]
test_data = data[1230:]

train_x = train_data.iloc[:, 1:21].values
train_y = train_data.iloc[:, 21:].values

test_x = test_data.iloc[:, 1:21].values
test_y = test_data.iloc[:, 21:].values

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
train_x = sc.fit_transform(train_x)
test_x = sc.transform(test_x)

# Applying PCA
from sklearn.decomposition import PCA
pca = PCA(n_components = 10)
train_x = pca.fit_transform(train_x)
test_x = pca.transform(test_x)
explained_variance = pca.explained_variance_ratio_

from keras.models import Sequential
from keras.layers import Dense
classifier = Sequential()

classifier.add(Dense(output_dim = 4, init = 'uniform', activation ='tanh', input_dim = 10))
classifier.add(Dense(output_dim = 1, init = 'uniform', activation = 'sigmoid'))

classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# # Training the classifier and save model
# classifier.fit(train_x, train_y, batch_size = 5, epochs = 100)
#
# model_json = classifier.to_json()
# with open("model1617.json", "w") as json_file:
#     json_file.write(model_json)
# # serialize weights to HDF5
# classifier.save_weights("model16117.h5")
# print("Model saved to disk.")

# load json and create model
json_file = open('model1617.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
classifier = model_from_json(loaded_model_json)
# load weights into new model
classifier.load_weights("model1617.h5")
print("Model loaded from disk.")

y_pred = classifier.predict(test_x)
y_pred = (y_pred > 0.5)

from sklearn import metrics
cm = metrics.confusion_matrix(test_y, y_pred)
acc = metrics.accuracy_score(test_y, y_pred)

# # Printing the outputs of test
# for x in range(len(test_x)):
#     print("predicted: ", y_pred[x], "actual: ", test_y[x])

print(" the final accuracy : %.2f" % acc)
print("The confusion matrix is as follows : ", cm)
