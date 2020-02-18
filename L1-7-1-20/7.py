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
print("Class average:",avg)
grade=[]
for i in total:
    if i>=90:
        grade.append("S")
        fre["S"]=fre["S"]+1
    elif i>=80:
        grade.append("A")
        fre["A"]=fre["A"]+1
    elif i>=70:
        grade.append("B")
        fre["B"]=fre["B"]+1
    elif i>=60:
        grade.append("C")
        fre["C"]=fre["C"]+1
    elif i>=50:
        grade.append("D")
        fre["D"]=fre["D"]+1
    elif i>=avg/2:
        grade.append("E")
        fre["E"]=fre["E"]+1
    else:
        grade.append("U")
        fre["U"]=fre["U"]+1

print("Grade \t Count")
for i in fre:
    print(i+"\t"+str(fre[i]))
