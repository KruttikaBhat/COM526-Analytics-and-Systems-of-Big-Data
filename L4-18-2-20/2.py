"""
Transaction reduction
index, list of items of each index, count of each index
generate candidate set -> Take cross product of L(i-1) and apply the common k-1 rule to get the items. Get the frequency of each item
generate Li set -> prune the items which don't have the minimum support, prune the databse to remove indexes which will
not have enough items for the C(i+1), only prune out single items itself in the first level based on antimonotone property
but not for next levels since it's hard to say for multiple item itemsets
"""
from itertools import chain
import time
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

#chess_data=[i.strip().split() for i in open("chess.dat").readlines()]
#print(len(chess_data))
#transactions=chess_data
min_Support=3
C=[]
L=[]
level=0
copy_transactions=transactions
count=0
start=time.time()
while(level==0 or len(L[level-1])>1):
    print(level)
    if(level==0):
        C.append(dict.fromkeys(list(set(chain(*copy_transactions))),0))
    if level==1:
        C.append(dict.fromkeys(['-'.join([x,y]) for x in L[level-1] for y in L[level-1] if x<y],0))
    if level>1:
        C.append(dict.fromkeys(['-'.join([x,list(y.split('-'))[-1]]) for x in L[level-1] for y in L[level-1] if list(x.split('-'))[:-1]==list(y.split('-'))[:-1] and list(x.split('-'))[-1]<list(y.split('-'))[-1]],0))

    for i in C[level]:
        for j in copy_transactions:
            if (level<1 and i in j) or (level>=1 and set(list(i.split('-'))).issubset(set(j))):
                C[level][i]=C[level][i]+1


    L.append([i for i in C[level] if C[level][i]>=min_Support])
    if(level==0):
        for i in copy_transactions:
            copy_transactions[copy_transactions.index(i)]=list(set(i)-set(list(set(C[level].keys()) - set(L[level]))))

    print(C[level],L[level])
    copy_transactions=list(j for j in copy_transactions if len(j)>level+1)
    print(copy_transactions)
    level=level+1
end=time.time()



print("Frequent item sets")
print(sum(L,[]))
print(end-start)
