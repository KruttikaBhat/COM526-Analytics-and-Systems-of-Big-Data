#Apriori which will differentiate ab from ba
from itertools import chain
transactions = [[1, 2, 5],
                [2, 4],
                [2, 3],
                [1, 2, 4],
                [1, 3],
                [2, 3],
                [1, 3],
                [2, 1, 3, 5],
                [2, 1, 3],
                [4,5]]

transactions=[ list(map(str,x)) for x in transactions ]
min_Support=2
C=[]
L=[]
level=0
#if(level==0)
while(level==0 or len(L[level-1])>1):
    print(level)
    if(level==0):
        C.append(dict.fromkeys(list(set(chain(*transactions))),0))
    if level==1:
        C.append(dict.fromkeys([''.join([x,y]) for x in L[level-1] for y in L[level-1] if x!=y],0))
    if level>1:
        C.append(dict.fromkeys([''.join([x,y[-1]]) for x in L[level-1] for y in L[level-1] if x[:-1] in y[:-1] and x[-1]!=y[-1]],0))

    for i in C[level]:
        for j in transactions:
            if (level<1 and i in j):
                C[level][i]=C[level][i]+1
            if (level>=1 and set(list(i)).issubset(set(j))):
                count=0
                elements=list(i)
                #print(elements,j)
                for k in j:
                    #print(elements[count],k)
                    if elements[count]==k:
                        count=count+1
                        if(count==len(elements)):
                            C[level][i]=C[level][i]+1
                            break



    L.append([i for i in C[level] if C[level][i]>=min_Support])
    level=level+1
    print(C[level-1],L[level-1], len(L[level-1]),level)

print("Frequent item sets")
print(sum(L,[]))
