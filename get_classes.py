"""
Generates data_1.csv and data_2.csv
"""

import pandas as pd

data=pd.read_csv("stateDownload")
#print(data)
#Add Genus column
data['Genus']=data['Scientific Name with Author'].str.split().str.get(0)

#remove the duplicate row
indexes=data.loc[data['Scientific Name with Author']=='Sarracenia purpurea L. ssp. purpurea var. purpurea'].index
data.loc[indexes[0],'Synonym Symbol']=data.loc[indexes[1],'Synonym Symbol']
#print(data.loc[data['Scientific Name with Author']=='Sarracenia purpurea L. ssp. purpurea var. purpurea'])
data=data.drop(indexes[1])
#print(data.loc[data['Scientific Name with Author']=='Sarracenia purpurea L. ssp. purpurea var. purpurea'])

#remove 2 columns
data = data.reset_index(drop=True)
del data['Scientific Name with Author']
del data['Synonym Symbol']

#Get the rows of first family
data_1=data[data['Family']=='Asteraceae']
del data_1['Family']
data_1 = data_1.reset_index(drop=True)

#append column heading to beginning of each value
data_1['Symbol']='Symbol_'+data_1['Symbol'].astype('str')
data_1['National Common Name'] = data_1['National Common Name'].str.replace(' ', '_')
#Since this column had null values, add extra step
for i in range(len(data_1.index)):
    if ~(data_1.isnull().loc[i,'National Common Name']):
        data_1.loc[i,'National Common Name'] = 'NCN_'+data_1.loc[i,'National Common Name']
data_1['Genus']='Genus_'+data_1['Genus'].astype('str')

data_1.to_csv('data_1.csv')
#Get the rows of second family
data_2=data[data['Family']=='Poaceae']
del data_2['Family']
data_2 = data_2.reset_index(drop=True)

#append column heading to beginning of each value
data_2['Symbol']='Symbol_'+data_2['Symbol'].astype('str')
data_2['National Common Name'] = data_2['National Common Name'].str.replace(' ', '_')
for i in range(len(data_2.index)):
    if ~(data_2.isnull().loc[i,'National Common Name']):
        data_2.loc[i,'National Common Name'] = 'NCN_'+data_2.loc[i,'National Common Name']
data_2['Genus']='Genus_'+data_2['Genus'].astype('str')

data_2.to_csv('data_2.csv')
