#!/usr/bin/python3

"""
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors

    Sara has label 0
    Chris has label 1

"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

### make sure you use // when dividing for integer division


#########################################################
### your code goes here ###

from sklearn import svm
clf = svm.SVC(kernel='rbf', C=10000, gamma='auto')
# svm.LinearSVC is bilinear, and slightly different from SVC(kernel='linear')

# features_train = features_train[:len(features_train)//100]
# labels_train = labels_train[:len(labels_train)//100]

t0 = time()
clf.fit(features_train, labels_train)
print ("training time:", round(time()-t0, 3), "s")

t0 = time()
pred = clf.predict(features_test)
print ("prediction time:", round(time()-t0, 3), "s")

# print ('prediction[10]: ', pred[10])
count = 0
for p in pred:
    if p == 1:
        count+=1

print ("Chris Counter: ", count)


from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)

print("accuracy_score: " , acc)



#########################################################
