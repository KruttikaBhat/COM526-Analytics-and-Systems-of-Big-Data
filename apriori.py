"""
Outputs stored in ARM folder.
"""
import pandas as pd
from apyori import apriori

#assign values and file name as desired
f=open('ARM/Apriori/Asteraceae/7.txt','w+')
support=2
confidence=0.5
#replace with data_1 or data_2 as desired
data_check=pd.read_csv('data_1.csv')

#converts dataframe to list of lists to get transactions
size=len(data_check.index)
transactions=[]
for i in range(size):
    list=[]
    for col in data_check.columns:
        if ~(data_check.isnull().loc[i,col]):
            list.append(str(data_check.loc[i,col]))

    transactions.append(list)
print(len(transactions))


#uncomment for apriori
itemsets=apriori(transactions,min_support=support/len(transactions),min_confidence=confidence)
count=1
total=0
ng=0
ns=0
gs=0
length=[0]*3

for item in itemsets:
    #result1.append(''.join([str(x) for x in i]))

    pair = item[0]
    items = [x for x in pair]

    length[len(items)-1]=length[len(items)-1]+1

    f.write('\nItemset : '+str(count)+"\n")
    for i in items:
        f.write(str(i)+" ")
    f.write("\n\nSupport: " + str(item[1]))
    f.write("\nConfidence: " + str(item[2][0][2]))
    f.write("\nLift: " + str(item[2][0][3]))
    f.write("\n=====================================\n")



    if(len(items)>1):
        if((items[0][0]=='N' and items[1][0]=='G')or (items[1][0]=='N' and items[0][0]=='G')):
            ng=ng+1
        if((items[0][0]=='N' and items[1][0]=='S')or (items[1][0]=='N' and items[0][0]=='S')):
            ns=ns+1
        if((items[0][0]=='G' and items[1][0]=='S')or (items[1][0]=='G' and items[0][0]=='S')):
            gs=gs+1

    count=count+1
    total=total+1

print("Total items:"+str(total))
print("1. Items of size 1:"+str(length[0]))
print("2. Items of size 2:"+str(length[1]))
print('\ti)Symbol and National Common Name: '+str(ns))
print('\tii)National Common Name and Genus : '+str(ng))
print('\tiii)Symbol and Genus : '+str(gs))
print("Items of size 3:"+str(length[2]))
