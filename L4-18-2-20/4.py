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
                [1, 2, 3]]

transactions=[ list(map(str,x)) for x in transactions ]
unique_items=list(map(str,sorted(list(set(itertools.chain(*transactions))))))

vertical=[]
support=[]
for i in range(len(transactions)):
    vertical.append([0]*len(unique_items))
    for j in transactions[i]:
        vertical[i][unique_items.index(j)]=1
    #print(vertical)
    support.append(sum(vertical[i]))

#print(vertical,support)
copy_vertical=np.array(vertical)
min_Support=2

print(copy_vertical)

C=[]
level=0
L=[]

while level==0 or len(L):
    if level==0:
        for i in unique_items:
            to_add=[]
            for j in range(len(copy_vertical.transpose()[unique_items.index(i)])):
                if copy_vertical.transpose()[unique_items.index(i)][j]==1:
                    to_add.append(j)
            print(to_add)
            if len(to_add)>=min_Support:
                L.append(itemset(i,to_add))

    else:
        L=[]
        for k1 in C[level-1]:
            for k2 in C[level-1]:
                if list(k1.item.split('-'))[:-1]==list(k2.item.split('-'))[:-1] and list(k1.item.split('-'))[-1]<list(k2.item.split('-'))[-1]:
                    to_add=sorted(list(set(k1.tids) & set(k2.tids)))
                    print(k1.item,k2.item,k1.tids,k2.tids,to_add)
                    if len(to_add)>=min_Support:
                        L.append(itemset('-'.join([k1.item,list(k2.item.split('-'))[-1]]),to_add))


    C.append(L)
    for i in C[level]:
        print(i.item,i.tids)
    level=level+1

for i in C:
    for j in i:
        print(j.item, len(j.tids))
