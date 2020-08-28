"""
nbapredict.py
METU CENG499 Project
Author : Yekta Demirci (yektademirci@hotmail.com), İlayda Beyreli(ilaydabeyreli@gmail.com)
Date(dd/mm/yyy): 05/05/2018
Description :
"""
import numpy as np
import pandas as pd

from keras.models import model_from_json
import sys

data = pd.read_csv('data_20172018.txt', sep=" ", header=None)
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
x_train = sc.fit_transform(train_x)
# x_test = sc.transform(x_test)

# Applying PCA
from sklearn.decomposition import PCA
pca = PCA(n_components = 10)
x_train = pca.fit_transform(x_train)
x_test = pca.transform(x_test)
explained_variance = pca.explained_variance_ratio_
from keras.models import Sequential
from keras.layers import Dense
classifier = Sequential()


classifier.add(Dense(output_dim = 8, init = 'uniform', activation = 'tanh', input_dim = 10))
classifier.add(Dense(output_dim = 1, init = 'uniform', activation = 'sigmoid'))

# classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
#
#
#
# classifier.fit(x_train, train_y, batch_size = 5, nb_epoch = 100)
#
# model_json = classifier.to_json()
# with open("model1718.json", "w") as json_file:
#     json_file.write(model_json)
# # serialize weights to HDF5
# classifier.save_weights("model1718.h5")
# print("Saved model to disk")

# load json and create model
json_file = open('model1718.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
classifier = model_from_json(loaded_model_json)
# load weights into new model
classifier.load_weights("model1718.h5")
print("Loaded model from disk")

y_pred = classifier.predict(test_x)
y_pred = (y_pred > 0.5)

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
cm = confusion_matrix(test_y, y_pred)
acc = accuracy_score(test_y, y_pred)
print(acc)
# for x in range(len(test_x)):
#     print("predicted: ", y_pred[x], "actual: ", test_y[x])

