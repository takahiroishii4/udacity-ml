#!/usr/bin/python3

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from time import time

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
# plt.show()
#################################################################################


### your code here!  name your classifier object clf if you want the
### visualization code (prettyPicture) to show you the decision boundary

# K-nearest neighbors
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=11, algorithm='auto', weights='distance')

t0 = time()
clf = clf.fit(features_train, labels_train)
print ("training time[KNN]:", round(time()-t0, 3), "s")

t0 = time()
pred = clf.predict(features_test)
print ("prediction time[KNN]:", round(time()-t0, 3), "s")

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
print("accuracy_score: ", round(acc, 4))


# Random forest
from sklearn.ensemble import RandomForestClassifier
clf2 = RandomForestClassifier(n_estimators = 100, criterion = "entropy", max_depth = 5)

t0 = time()
clf2.fit(features_train, labels_train)
print ("training time[RF]:", round(time()-t0, 3), "s")

t0 = time()
pred2 = clf2.predict(features_test)
print ("prediction time[RF]:", round(time()-t0, 3), "s")
acc2 = accuracy_score(pred2, labels_test)
print("accuracy_score: ", round(acc2, 4))


# Adaboost
from sklearn.ensemble import AdaBoostClassifier
clf3 = AdaBoostClassifier(n_estimators = 100)

t0 = time()
clf3.fit(features_train, labels_train)
print ("training time[Ada]:", round(time()-t0, 3), "s")

t0 = time()
pred3 = clf3.predict(features_test)
print ("prediction time[Ada]:", round(time()-t0, 3), "s")
acc3 = accuracy_score(pred3, labels_test)
print("accuracy_score: ", round(acc2, 4))


try:
    prettyPicture(clf3, features_test, labels_test)
    plt.show()
    exit()
except NameError:
    print("NameError")
    pass
