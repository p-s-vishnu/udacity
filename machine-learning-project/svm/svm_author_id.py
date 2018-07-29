#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
from sklearn import svm
from sklearn.metrics import accuracy_score
sys.path.append("/Users/Focus/Documents/GitHub/udacity/machine-learning-project/tools/")
from email_preprocess import preprocess

# features_train and features_test are the features for the training
# and testing data sets, respectively
# labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
# your code goes here ###
clf = svm.SVC(C=10000, kernel='rbf')
# Slicing training set
# features_train = features_train[:len(features_train) / 100]
# labels_train = labels_train[:len(labels_train) / 100]

t0 = time()
clf.fit(features_train, labels_train)
t1 = time()
print 'training time:', round(t1 - t0, 3), 's'
pred = clf.predict(features_test)
score = accuracy_score(labels_test, pred)
print 'accuracy:', score
t2 = time()
print 'testing time:', round(t2 - t1, 3), 's'
print 'test samples size:', len(pred)
# 0 is for Sara
# 1 is for Chris
names = {
    0: 'Sara',
    1: 'Chris'
}

# Given it is a zero indexed list
# hence prediction for 10th
# print '10th prediction:', names[pred[10]]

# prediction for 26th
# print '26th prediction:', names[pred[26]]

# prediction for 50th
# print '50th prediction:', names[pred[50]]
print 'Total number of Chris(1) mail', sum(pred)
#########################################################
