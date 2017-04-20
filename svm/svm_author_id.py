#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# features_train = features_train[:len(features_train)/100] 
# labels_train = labels_train[:len(labels_train)/100] 


#########################################################
### your code goes here ###
clf = SVC(kernel='rbf', C = 10000)
clf.fit(features_train, labels_train)

pred = clf.predict(features_test)

count = 0 #count for the number of test in class 1

for a in pred:
	if a==1:
		count += 1

print count

# print pred[10]
# print ""
# print pred[26]
# print ""
# print pred[50]

#####################################################################

#BOTH OF THE ABOVE AND BELOW ARE CORRECT FOR PREDICTING A PARTICULAR VALUE IN TEST SET

#####################################################################
# pred1 = clf.predict(features_test[10])
# pred2 = clf.predict(features_test[26])
# pred3 = clf.predict(features_test[50])

# print pred1
# print ""
# print pred2
# print ""
# print pred3


print accuracy_score(pred, labels_test)


#########################################################


