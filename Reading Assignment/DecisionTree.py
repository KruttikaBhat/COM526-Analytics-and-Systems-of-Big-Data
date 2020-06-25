from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

#load the data
X, y = load_iris(return_X_y=True)

#get training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% testing

#train the model and get the predicted values
clf = DecisionTreeClassifier(criterion="entropy", max_depth=2)
clf = clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)

#check performance
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("Number of mislabeled points out of a total %d points : %d" % (X_test.shape[0], (y_test != y_pred).sum()))
print(classification_report(y_test, y_pred))
cf_matrix=confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cf_matrix)

sns.heatmap(cf_matrix, annot=True)
plt.show()
