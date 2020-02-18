import numpy as np
import csv

input=[]
with open('marks.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        input.append(row)

#print(input)

total=[]

for i in np.array(input)[1:,1:]:
    #print(i)
    total.append(sum([int(j) for j in i]))
#print(total)

fre={"S":0,"A":0,"B":0,"C":0,"D":0,"E":0,"U":0}
avg=np.mean(total)
passing=avg/2
passing_mean=sum(1 for i in total if i>passing)
X=passing_mean-passing
maximum=max(total)
s=maximum-(0.1*(maximum-passing_mean))
Y=s-passing_mean
a=passing_mean+(Y*5/8)
b=passing_mean+(Y*2/8)
c=passing_mean-(X*2/8)
d=passing_mean-(X*5/8)



print("Class average:",avg)
grade=[]


for i in total:
    if i>=s:
        grade.append("S")
        fre["S"]=fre["S"]+1
    elif i>=a:
        grade.append("A")
        fre["A"]=fre["A"]+1
    elif i>=b:
        grade.append("B")
        fre["B"]=fre["B"]+1
    elif i>=c:
        grade.append("C")
        fre["C"]=fre["C"]+1
    elif i>=d:
        grade.append("D")
        fre["D"]=fre["D"]+1
    elif i>=passing:
        grade.append("E")
        fre["E"]=fre["E"]+1
    else:
        grade.append("U")
        fre["U"]=fre["U"]+1

print("Grade \t Count")
for i in fre:
    print(i+"\t"+str(fre[i]))
