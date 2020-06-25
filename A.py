"""
Uncomment print statements to see outputs in terminal. Code was run in jupyter notebook. To get exact same figures
and tables, copy the lines of code to jupyter notebook and execute one by one. Don't include print() function to display
values and tables in jupyter notebook.
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#preprocessing
data=pd.read_csv("stateDownload")

#print(data)
#Check column names
#print(data.columns)
#Check the data types of each column
#print(data.dtypes)

#Add Genus column
data['Genus']=data['Scientific Name with Author'].str.split().str.get(0)
"""
#Now see general measures on data
print(data.describe())
print(data.info())
#Check the number and percentage of null values
print(data.isnull().sum())
print(data.isnull().sum()/len(data))

#Is it possible to remove all rows which have a null
print(data.dropna().describe()) #not an option-> Each row has some null value

#Now check for dropping rows only if specific column(s) is null
print(data.dropna(subset=['Synonym Symbol']).describe())
print(data.dropna(subset=['National Common Name']).describe())
print(data.dropna(subset=['Synonym Symbol','National Common Name'],how='all').describe())

#check the rows which have both column as null
print(data[data['Synonym Symbol'].isnull() & data['National Common Name'].isnull()])
#check if there are any repetitions
print(data.loc[data['Symbol']=='APFL'])
print(data[data['Symbol'].str.contains('MER')])
print(data[data['Symbol'].str.contains('ARON')])
print(data[data['Symbol'].str.contains('VIPR')])
"""
#replace null values with string 'NA'
data=data.fillna('NA')
"""
print(data)

#check for duplicates
print(data['Symbol'].value_counts())
print(data['Synonym Symbol'].value_counts())
print(data['Scientific Name with Author'].value_counts())
print(data['National Common Name'].value_counts())
print(data['Family'].value_counts())
print(data['Genus'].value_counts())
"""
#check the duplicate rows
#print(data.loc[data['Scientific Name with Author']=='Sarracenia purpurea L. ssp. purpurea var. purpurea'])

#combine the 2 rows
indexes=data.loc[data['Scientific Name with Author']=='Sarracenia purpurea L. ssp. purpurea var. purpurea'].index
data.loc[indexes[0],'Synonym Symbol']=data.loc[indexes[1],'Synonym Symbol']

#print(data.loc[data['Scientific Name with Author']=='Sarracenia purpurea L. ssp. purpurea var. purpurea'])
#print(indexes)
data=data.drop(indexes[1])
#check if the row got dropped
#print(data.describe())
#print(data.loc[data['Scientific Name with Author']=='Sarracenia purpurea L. ssp. purpurea var. purpurea'])


"""
#Uncomment for descriptive analytics part
#Descriptive Analytics
#Symbol
Symbol_List=list(set(data['Symbol']))
arr=[]
for i in Symbol_List:
    arr.append([i,data[data['Symbol']==i].Symbol.value_counts().sum()])

arr=sorted(arr, key = lambda x: x[1],reverse=True)
#for i in arr:
#    print(arr.index(i),i)

#helps to check the index for plotting the graphs
Symbol=pd.DataFrame(arr)
#print(Symbol[Symbol[1]==1]) #change condition to >20 to get index value to plot bar graph

plt.figure()
plt.grid(axis='y', alpha=0.4)
plt.bar(np.array(arr)[:14,0], np.array(arr)[:14,1].astype(np.int))
plt.xticks(rotation='vertical')
plt.savefig('Figures/Descriptive/Symbol_Bar')
plt.close()

plt.figure()
input=list(map(int,np.array(arr)[:,1]))
n, bins, patches = plt.hist(x=input, bins=np.arange(min(input),max(input)+1,1), color='#0504aa')
plt.grid(axis='y', alpha=0.4)
plt.xlabel('Count')
plt.ylabel('Frequency of Count')
maxfreq = n.max()
plt.ylim(ymax=maxfreq+100)
plt.savefig('Figures/Descriptive/Symbol_Hist')
plt.close()

#National Common Name
Name_List=list(set(data['National Common Name']))
arr_name=[]
for i in Name_List:
    arr_name.append([i,data[data['National Common Name']==i]['National Common Name'].value_counts().sum()])
arr_name=sorted(arr_name, key = lambda x: x[1],reverse=True)
arr_name=np.array(arr_name)[1:,:]
#for i in arr_name:
#    print(i)

Name=pd.DataFrame(arr_name)
#print(Name[Name[1].astype(int)==1]) #change condition to >20 to get index value to plot bar graph

plt.figure()
plt.grid(axis='y', alpha=0.4)
plt.bar(np.array(arr_name)[:7,0], np.array(arr_name)[:7,1].astype(np.int))
plt.xticks(rotation='vertical')
plt.savefig('Figures/Descriptive/NCN_Bar')
plt.close()

plt.figure()
input=list(map(int,np.array(arr_name)[:,1]))
n, bins, patches = plt.hist(x=input, bins=np.arange(min(input),max(input)+1,1), color='#0504aa')
plt.grid(axis='y', alpha=0.4)
plt.xlabel('Count')
plt.ylabel('Frequency of Count')
maxfreq = n.max()
plt.ylim(ymax=maxfreq+100)
plt.savefig('Figures/Descriptive/NCN_Hist')
plt.close()

#Family
Family_List=list(set(data['Family']))
arr_family=[]
for i in Family_List:
    arr_family.append([i,data[data['Family']==i]['Family'].value_counts().sum()])
arr_family=sorted(arr_family, key = lambda x: x[1],reverse=True)

#for i in arr_family:
#    print(i)

Family=pd.DataFrame(arr_family)
#print(Family[Family[1].astype(int)<3]) #change condition to >20 to get index value to plot bar graph

plt.figure()
plt.grid(axis='y', alpha=0.4)
plt.bar(np.arange(1,len(arr_family)+1), np.array(arr_family)[:,1].astype(np.int))
plt.xlabel('index of family name')
plt.ylabel('No. of rows')
plt.savefig('Figures/Descriptive/Family_Bar')
plt.close()

plt.figure()
input=list(map(int,np.array(arr_family)[:,1]))
n, bins, patches = plt.hist(x=input, bins=np.arange(min(input),max(input)+10,100), color='#0504aa')
plt.grid(axis='y', alpha=0.4)
plt.xlabel('No. of rows')
plt.ylabel('Frequency')
maxfreq = n.max()
plt.ylim(ymax=maxfreq+10)
plt.savefig('Figures/Descriptive/Family_Hist')
plt.close()

plt.figure()
sns.set_style("whitegrid")
ax = sns.swarmplot(x=input)
plt.xlabel("No. of rows")
plt.savefig('Figures/Descriptive/Family_Swarm')
plt.close()

plt.figure()
sns.set_style("whitegrid")
ax = sns.boxplot(x=input)
plt.xlabel("No. of rows")
plt.savefig('Figures/Descriptive/Family_Box')
plt.close()

for i in Family_List:
    plt.figure()
    data[data['Family']==i]['Symbol'].value_counts().plot.pie()
    plt.savefig('Figures/Descriptive/Family/'+i)
    plt.close()

#Genus
Genus_List=list(set(data['Genus']))
arr_genus=[]
for i in Genus_List:
    arr_genus.append([i,data[data['Genus']==i]['Genus'].value_counts().sum()])
arr_genus=sorted(arr_genus, key = lambda x: x[1],reverse=True)

#for i in arr_genus:
#    print(i)

Genus=pd.DataFrame(arr_genus)
#print(Genus[Genus[1].astype(int)<6])

plt.figure()
plt.grid(axis='y', alpha=0.4)
plt.bar(np.array(arr_genus)[:6,0], np.array(arr_genus)[:6,1].astype(np.int))
plt.xticks(rotation='vertical')
plt.savefig('Figures/Descriptive/Genus_Bar')
plt.close()

plt.figure()
input=list(map(int,np.array(arr_genus)[:,1]))
n, bins, patches = plt.hist(x=input, bins=np.arange(min(input),max(input)+1,5), color='#0504aa')
plt.grid(axis='y', alpha=0.4)
plt.xlabel('No. or rows')
plt.ylabel('Frequency')
maxfreq = n.max()
plt.ylim(ymax=maxfreq+100)
plt.savefig('Figures/Descriptive/Genus_Hist')
plt.close()

plt.figure()
sns.set_style("whitegrid")
#ax = sns.boxplot(x=input,color="green")
ax = sns.swarmplot(x=input)
plt.xlabel("No. of rows")
plt.savefig('Figures/Descriptive/Genus_Swarm')
plt.close()

plt.figure()
sns.set_style("whitegrid")
ax = sns.boxplot(x=input)
plt.xlabel("No. of rows")
plt.savefig('Figures/Descriptive/Genus_Box')
plt.close()
"""



"""
#Uncomment for predictive analytics part
#Predictive Analytics

#Encoding
encoded_data=data.copy()
#print(encoded_data.head())
for col in encoded_data.head():
    encoded_data[col]=encoded_data[col].astype('category')
    encoded_data[col] = encoded_data[col].cat.codes
print(encoded_data)
print(encoded_data.describe())
print(encoded_data.info())
corr=encoded_data.corr()
print(corr)


plt.figure()
sns.heatmap(corr, xticklabels=corr.columns,yticklabels=corr.columns, annot=True)
plt.savefig('Figures/Predictive/Corr_HeatMap')
plt.close()

plt.figure()
plt.scatter(encoded_data['Scientific Name with Author'],encoded_data['Symbol'])
plt.xlabel('Scientific Name with Author')
plt.ylabel('Symbol')
plt.savefig('Figures/Predictive/Scatter1')
plt.close()

plt.figure()
plt.scatter(encoded_data['Scientific Name with Author'],encoded_data['Synonym Symbol'])
plt.xlabel('Scientific Name with Author')
plt.ylabel('Synonym Symbol')
plt.savefig('Figures/Predictive/Scatter2')
plt.close()

plt.figure()
plt.scatter(encoded_data['Synonym Symbol'],encoded_data['Symbol'])
plt.xlabel('Synonym Symbol')
plt.ylabel('Symbol')
plt.savefig('Figures/Predictive/Scatter3')
plt.close()

#Uncomment to get classifiers
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.naive_bayes import GaussianNB

def modelAccuracy(X_test,y_test,y_pred):
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

def decisionTree(X_train, X_test, y_train, y_test):
    # Create Decision Tree classifer object
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

def doBoth(X_train, X_test, y_train, y_test):
    y_pred=decisionTree(X_train, X_test, y_train, y_test)
    print('Decision Tree:')
    modelAccuracy(X_test,y_test,y_pred)

    y_pred = Bayes(X_train, X_test, y_train, y_test)
    print('Naive Bayes')
    modelAccuracy(X_test,y_test,y_pred)

#Modify the feature and target columns and train test split as desired
feature_cols = ['Symbol', 'Synonym Symbol']
X = encoded_data[feature_cols] # Features
y = encoded_data['Genus'] # Target variable
#print(X,y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test
doBoth(X_train, X_test, y_train, y_test)
"""
