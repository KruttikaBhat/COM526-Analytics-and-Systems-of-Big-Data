import random
import numpy as np

input=[]
y=[]
size=20
print("X\tY")
for i in range(size):
    input.append(random.randint(6,500))
    y.append((2*input[i])+3)
    print(str(input[i])+"\t"+str(y[i]))
print("Standard Deviation: %f"%np.std(y))
