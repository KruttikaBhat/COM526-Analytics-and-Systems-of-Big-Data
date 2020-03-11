#Transaction reduction with vertical transaction database
import numpy as np
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
C=[]
L=[]
level=0


while(len(copy_vertical)):
    print(len(copy_vertical))
    if(level==0):
        C.append(dict.fromkeys(list(str(i+1) for i in range(copy_vertical.shape[1])),0))
    if level==1:
        C.append(dict.fromkeys([''.join([x,y]) for x in L[level-1] for y in L[level-1] if x<y],0))
    if level>1:
        C.append(dict.fromkeys([''.join([x,y[-1]]) for x in L[level-1] for y in L[level-1] if x[:-1]==y[:-1] and x[-1]<y[-1]],0))
    print(C[level])
    for i in C[level]:
        for x in copy_vertical[:,[j-1 for j in list(map(int, list(i)))]]:
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
