#Transaction reduction with vertical transaction database
import numpy as np
import itertools
transactions = [[1, 2, 5],
                [2, 4],
                [2, 3],
                [1, 2, 4],
                [1, 3],
                [2, 3],
                [1, 3],
                [1, 2, 3, 5],
                [1, 2, 3]]

#first convert to vertical database format
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
C=[]
L=[]
level=0


while(len(copy_vertical)):
    print(len(copy_vertical))
    if(level==0):
        C.append(dict.fromkeys(unique_items,0))
    if level==1:
        C.append(dict.fromkeys(['-'.join([x,y]) for x in L[level-1] for y in L[level-1] if x<y],0))
    if level>1:
        C.append(dict.fromkeys(['-'.join([x,list(y.split('-'))[-1]]) for x in L[level-1] for y in L[level-1] if list(x.split('-'))[:-1]==list(y.split('-'))[:-1] and list(x.split('-'))[-1]<list(y.split('-'))[-1]],0))

    print(C[level])
    for i in C[level]:
        for x in copy_vertical[:,[unique_items.index(j) for j in list(i.split('-'))]]:
            if(sum(x)==level+1):
                C[level][i]=C[level][i]+1
    print(C[level])
    L.append([i for i in C[level] if C[level][i]>=min_Support])
    print(L[level])
    if(level==0):
        for i in list(set(C[level].keys() - set(L[level]))):
            print(i)
            copy_vertical[:,int(i)-1]=0
        support=list(sum(x) for x in copy_vertical)

    copy_vertical=np.delete(copy_vertical,list(x for x in range(len(support)) if support[x]<level+2),axis=0)
    support=list(sum(x) for x in copy_vertical)
    print(copy_vertical,support)
    level=level+1


print("Frequent item sets")
print(sum(L,[]))
