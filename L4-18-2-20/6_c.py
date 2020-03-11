#Sampling
import random
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
C=[]
overall_L=[]
prevL=[]
sampling_size=3
iter=0

while (prevL!=overall_L or iter<=1) or (prevL==overall_L and iter<(len(transactions)/sampling_size)*10):
    #take a sample

    sample_indices=sorted(random.sample(range(len(transactions)-1), sampling_size))
    sample=[transactions[i] for i in sample_indices]
    #print(sample)
    prevL=overall_L
    level=0
    C=[]
    L=[]
    iter=iter+1

    while(level==0 or len(L[level-1])>1):
        #print(level)
        if(level==0):
            C.append(dict.fromkeys(list(set(chain(*sample))),0))
        if level==1:
            C.append(dict.fromkeys(['-'.join([x,y]) for x in L[level-1] for y in L[level-1] if x<y],0))
        if level>1:
            C.append(dict.fromkeys(['-'.join([x,list(y.split('-'))[-1]]) for x in L[level-1] for y in L[level-1] if list(x.split('-'))[:-1]==list(y.split('-'))[:-1] and list(x.split('-'))[-1]<list(y.split('-'))[-1]],0))

        for i in C[level]:
            for j in transactions:
                if (level<1 and i in j) or (level>=1 and set(list(i.split('-'))).issubset(set(j))):
                    C[level][i]=C[level][i]+1


        L.append([i for i in C[level] if C[level][i]>=min_Support])
        level=level+1
        #print(C[level-1],L[level-1], len(L[level-1]),level)

    for i in sum(L,[]):
        if i not in overall_L:
            overall_L.append(i)

    print(overall_L)


print("Frequent item sets")
print(overall_L)
