"""
Outputs stored in ARM folder.
"""
import pandas as pd
import pyfpgrowth

#assign values and file name as desired
f=open('ARM/FPGrowth/Poaceae/1.txt','w+')
support=2
confidence=0.5

#replace with data_1 or data_2 as desired
data_check=pd.read_csv('data_2.csv')

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

patterns = pyfpgrowth.find_frequent_patterns(transactions, support)
count=1
ng=0
ns=0
gs=0
length=[0]*3

"""
#Uncomment to get the items for fpgrowth and comment the next section
for k,v in patterns.items():

    f.write('\n\nItemset : '+str(count)+"\n")
    for i in k:
        f.write(str(i)+" ")
    f.write("\nSupport: "+str(v/len(data_check))+"\n")
    f.write("=="*20)
    length[len(k)-1]=length[len(k)-1]+1
    if(len(k)==2):
        if((k[0][0]=='N' and k[1][0]=='G')or (k[0][0]=='G' and k[1][0]=='N')):
            ng=ng+1
        if((k[0][0]=='N' and k[1][0]=='S')or (k[0][0]=='S' and k[1][0]=='N')):
            ns=ns+1
        if((k[0][0]=='G' and k[1][0]=='S')or (k[0][0]=='S' and k[1][0]=='G')):
            gs=gs+1

    count=count+1

"""

"""
#Uncomment to get the rules for fpgrowth and comment and the previous section
rules = pyfpgrowth.generate_association_rules(patterns, confidence)
for k,v in rules.items():

    f.write('\n\nItemset : '+str(count)+"\n")
    size=len(k)+len(v[0])
    length[size-1]=length[size-1]+1
    for i in k:
        f.write(str(i)+" ")
        if(len(k)==1):
            if((i[0]=='N' and v[0][0][0]=='G')or (i[0]=='G' and v[0][0][0]=='N')):
                ng=ng+1
            if((i[0]=='N' and v[0][0][0]=='S')or (i[0]=='S' and v[0][0][0]=='N')):
                ns=ns+1
            if((i[0]=='G' and v[0][0][0]=='S')or (i[0]=='S' and v[0][0][0]=='G')):
                gs=gs+1


    f.write(" -> "+str(v[0][0]))
    f.write("\nConfidence score: "+str(v[1])+"\n")
    f.write("=="*20)
    count=count+1

"""

print("Total items:"+str(count-1))
print("1. Items of size 1:"+str(length[0]))
print("2. Items of size 2:"+str(length[1]))
print('\ti)Symbol and National Common Name: '+str(ns))
print('\tii)National Common Name and Genus : '+str(ng))
print('\tiii)Symbol and Genus : '+str(gs))
print("Items of size 3:"+str(length[2]))
