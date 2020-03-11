#ECLAT algorithm
import numpy as np
import itertools

class itemset:
    def __init__(self,item,tids):
        self.item=item
        self.tids=tids

transactions = [[1, 2, 5],
                [2, 4],
                [2, 3],
                [1, 2, 4],
                [1, 3],
                [2, 3],
                [1, 3],
                [1, 2, 3, 5],
                [1, 2, 3],
                [4,5]]


vertical=[]
support=[]
for i in range(len(transactions)):
    vertical.append([0]*5)
    for j in transactions[i]:
        vertical[i][j-1]=1
    #print(vertical)
    support.append(sum(vertical[i]))

#print(vertical,support)
copy_vertical=np.array(vertical)
min_Support=2

print(copy_vertical)

unique_items=list(map(str,sorted(list(set(itertools.chain(*transactions))))))
print(unique_items)

C=[]
level=0
L=[]

while len(L) or level==0:
    if level==0:
        for i in range(len(copy_vertical.transpose())):
            to_add=[]
            for j in range(len(copy_vertical.transpose()[i])):
                if copy_vertical.transpose()[i][j]==1:
                    to_add.append(j)
            print(to_add)
            if len(to_add)>=min_Support:
                L.append(itemset(unique_items[i],to_add))
    else:
        L=[]
        for k1 in C[level-1]:
            for k2 in C[level-1]:
                if k1.item[:-1]==k2.item[:-1] and k1.item[-1]<k2.item[-1]:
                    to_add=sorted(list(set(k1.tids) & set(k2.tids)))
                    print(k1.item,k2.item,k1.tids,k2.tids,to_add)
                    if len(to_add)>=min_Support:
                        L.append(itemset(''.join([k1.item,k2.item[-1]]),to_add))


    C.append(L)
    for i in C[level]:
        print(i.item,i.tids)
    level=level+1

for i in C:
    for j in i:
        print(j.item, len(j.tids))
