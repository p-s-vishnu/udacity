#!/usr/bin/python

from initialize import initialize
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier

features_train, labels_train, features_test, labels_test = makeTerrainData()
initialize()

# Train the classifier
clf = AdaBoostClassifier()
clf.fit(features_train, labels_train)
print clf.score(features_test, labels_test)

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
