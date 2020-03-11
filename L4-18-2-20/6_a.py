#Hash based

from itertools import chain
import numpy as np
from collections import defaultdict

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
min_Support=2
unique_items=list(map(str,sorted(list(set(chain(*transactions))))))

C=[]
L=[]
level=0
#if(level==0)
while(level==0 or len(L[level-1])>1):
    print(level)
    if level==1:
        #do hashmap here
        Hash=defaultdict(list)
        to_add=[]
        for i in transactions:
            for j in i:
                for k in i[i.index(j)+1:]:
                    if j in L[level-1] and k in L[level-1]:
                        index=(10*(unique_items.index(j)+1)+unique_items.index(k)+1)%7
                        Hash[index].append(j+'-'+k)
        #print(list(set().union(*Hash.values())))
        for i in Hash:
            if len(Hash[i])>=min_Support and len(set(Hash[i]))==1:
                to_add.append(Hash[i][0])
            if len(Hash[i])>=min_Support and len(set(Hash[i]))!=1:
                for j in set(Hash[i]):
                    if Hash[i].count(j)>=min_Support:
                        to_add.append(j)
        C.append(to_add)
        L.append(to_add)
        print(C)

    else:
        if (level==0):
            C.append(dict.fromkeys(unique_items,0))
        if level>1:
            C.append(dict.fromkeys(['-'.join([x,list(y.split('-'))[-1]]) for x in L[level-1] for y in L[level-1] if list(x.split('-'))[:-1]==list(y.split('-'))[:-1] and list(x.split('-'))[-1]<list(y.split('-'))[-1]],0))


        for i in C[level]:
            for j in transactions:
                if (level<1 and i in j) or (level>=1 and set(list(i.split('-'))).issubset(set(j))):
                    C[level][i]=C[level][i]+1

        L.append([i for i in C[level] if C[level][i]>=min_Support])


    level=level+1
    print(C[level-1],L[level-1], len(L[level-1]),level)

print("Frequent item sets")
print(sum(L,[]))




#partitioning


#sampling
