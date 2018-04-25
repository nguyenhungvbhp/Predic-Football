import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import scale
from sklearn.preprocessing import MinMaxScaler
import csv
import numpy as np
from numpy import genfromtxt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

dirTrain = "/Users/manhhung/Documents/BKHN/ML/workspace/pre_football/football-results-prediction-ml/data_train/datatrain1.csv"

my_data = genfromtxt(dirTrain, delimiter=',')
# print(my_data.shape)
l = len(my_data[1])
X = my_data[:, : l - 1]
Y = my_data[:, -1]
X = X[:,2:]
print(X.shape)

# print(type(X[0,0]))

#
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        print(str(X[i,j]) + str(type(X[i,j])))
# max = 1
# min = 0
# X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
# X_scaled = X_std * (max - min) + min
# print(X)
# # print(X[0])
# scaler = MinMaxScaler()


# scaler.fit(X)
# scaler = scaler.fit(X)
# X  = scale(X)
# print(X[0])

# X0 = X[Y == 0,:]
# print '\nSamples from class 0:\n', X0[:5,:]
#
# X1 = X[Y == 1,:]
# print '\nSamples from class 1:\n', X1[:5,:]
#
# X2 = X[Y == -1,:]
# print '\nSamples from class 2:\n', X2[:5,:]


test_size = int(len(Y) * 0.2)

X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=test_size)


print "Training size: %d" % len(y_train)
print "Test size    : %d" % len(y_test)


def knn(n_n, p):
    clf = KNeighborsClassifier(n_neighbors=n_n, p=p, weights = 'distance')
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print "Accuracy of " + str(n_n) + "NN: %.2f %%" % (100 * accuracy_score(y_test, y_pred))
    return 100 * accuracy_score(y_test, y_pred)

def random_forest():
    clf = RandomForestClassifier(n_estimators=10)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print "(Accuracy of random forest   " + "%.2f)"% (100 * accuracy_score(y_test, y_pred))
    return 100 * accuracy_score(y_test, y_pred)

def svm():
    clf = SVC(C = 1.0)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print "(Accuracy of SVM   " + "%.2f)"% (100 * accuracy_score(y_test, y_pred))
    return 100 * accuracy_score(y_test, y_pred)

def naive_bayes():
    clf = GaussianNB()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print "(Accuracy of naive bayes  " + "%.2f)"% (100 * accuracy_score(y_test, y_pred))
    return 100 * accuracy_score(y_test, y_pred)


def runKNN():
    arrNN = range(2, 20)
    result = 0
    for i in arrNN:
        k = knn(i, 2)
        if k > result:
            result = k

    print(result)


# random_forest()
naive_bayes()
svm()
runKNN()
