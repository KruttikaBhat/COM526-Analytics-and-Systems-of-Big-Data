import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
import seaborn as sns
import matplotlib.pyplot as plt


def modelAccuracy(X_test,y_test,y_pred):
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
    print("Number of mislabeled points out of a total %d points : %d"\
          % (X_test.shape[0], (y_test != y_pred).sum()))
    print(classification_report(y_test, y_pred))
    cf_matrix=confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:")
    print(cf_matrix)
    plt.figure()
    sns.heatmap(cf_matrix, annot=True)
    plt.show()

def decisionTree(X_train, X_test, y_train, y_test):
    # change max depth as desired
    clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)
    # Train Decision Tree Classifer
    clf = clf.fit(X_train,y_train)
    #Predict the response for test dataset
    y_pred = clf.predict(X_test)
    return y_pred

def Bayes(X_train, X_test, y_train, y_test):
    gnb = GaussianNB()
    y_pred = gnb.fit(X_train, y_train).predict(X_test)
    return y_pred


# load dataset
data = pd.read_csv("diabetes.csv")
print(data.head())

#Assign feature and target columns
feature_cols = ['Pregnancies', 'Insulin', 'BMI', 'Age','SkinThickness','Glucose','BloodPressure','DiabetesPedigreeFunction']
X = data[feature_cols] # Features
y = data.Outcome # Target variable
print(X,y)

#to get iris dataset
#X, y = load_iris(return_X_y=True)

#change test size as required
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test

#To do Decision tree
y_pred=decisionTree(X_train, X_test, y_train, y_test)

#To do Naive Bayes
y_pred = Bayes(X_train, X_test, y_train, y_test)

modelAccuracy(X_test,y_test,y_pred)
