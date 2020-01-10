#!/usr/bin/python3


"""
    starter code for the evaluation mini-project
    start by copying your trained/tested POI identifier from
    that you built in the validation mini-project

    the second step toward building your POI identifier!

    start by loading/formatting the data

"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
# sort_keys = '../tools/python2_lesson14_keys.pkl'
labels, features = targetFeatureSplit(data)



### your code goes here

# training-testing split
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features,
labels, random_state=42, test_size=0.3)

### POI identifier based on decision tree /  it's all yours from here forward!
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)
print ("accuracy: ", clf.score(features_test, labels_test))

predictions = clf.predict(features_test)
print ("predictions:", predictions)
print ("actuals:", labels_test)

from sklearn import metrics
print ("precision:", metrics.precision_score(labels_test, predictions))
print ("recall:", metrics.recall_score(labels_test, predictions))
