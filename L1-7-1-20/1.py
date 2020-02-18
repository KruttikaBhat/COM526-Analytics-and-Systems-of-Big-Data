import numpy as np

input=["blue","red","blue","green","blue",
        "blue","green","red","green","blue",
        "red","green","blue","red","red",
        "blue","green","orange","blue","green",
        "red","red","blue","green","red",
        "green","green","red","green","green",
        "blue","green","blue","red","blue",
        "blue","blue","orange","blue","green",
        "blue","green","green","red","orange",
        "blue","red","orange","blue","orange"]

colors=sorted(np.unique(input))
#print(colors, len(colors))
fre=dict(zip(colors,np.zeros((len(colors),), dtype=int)))

#print(fre)
for i in input:
    fre[i]=fre[i]+1

#print(fre)

print("Score \t Tally \t Frequency")

for i in fre:
    print(i,end ="\t")
    tally=""
    for j in range(1,fre[i]+1):
        if j%5==0:
            tally=tally+"\\"
        elif j%5==1:
            tally=tally+" |"
        else:
            tally=tally+"|"
    print(tally+"\t"+str(fre[i])+"\n")
