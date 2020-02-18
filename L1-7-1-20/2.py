import numpy as np

marks=[]
size=18
print("Roll Number\t Marks")
for i in range(1,size+1):
    if i%2==0:
        marks.append(25+((i+8)%10))

    else:
        marks.append(25+((i+7)%10))
    print("CSE20D"+str(i).zfill(2)+"\t"+str(marks[i-1]))

print("Mean:%f, Median:%f" % (np.mean(marks), np.median(marks)))
