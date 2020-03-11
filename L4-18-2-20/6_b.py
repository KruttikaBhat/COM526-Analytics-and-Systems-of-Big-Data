#partitioning

from itertools import chain
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
partition_size=2

index=0

C=[]
L=[]
level=0
#if(level==0)
while(level==0 or len(L[level-1])>1):
    print(level)

    if(level==0):
        C.append(dict.fromkeys(list(set(chain(*transactions))),0))
    if level==1:
        C.append(dict.fromkeys(['-'.join([x,y]) for x in L[level-1] for y in L[level-1] if x<y],0))
    if level>1:
        C.append(dict.fromkeys(['-'.join([x,list(y.split('-'))[-1]]) for x in L[level-1] for y in L[level-1] if list(x.split('-'))[:-1]==list(y.split('-'))[:-1] and list(x.split('-'))[-1]<list(y.split('-'))[-1]],0))


    temp=[]
    index=0
    while index<len(transactions):
        partition=transactions[index:index+partition_size]
        #print(partition)
        for i in C[level].copy():
            for j in partition:
                #print(i,j)
                if (level<1 and i in j) or (level>=1 and set(list(i.split('-'))).issubset(set(j))):
                    C[level][i]=C[level][i]+1
            if C[level][i]>=min_Support:
                temp.append(i)
                del C[level][i]
        #print(C[level])
        index=index+partition_size

    L.append(temp)
    level=level+1
    print(C[level-1],L[level-1], len(L[level-1]),level)

print("Frequent item sets")
print(sum(L,[]))
