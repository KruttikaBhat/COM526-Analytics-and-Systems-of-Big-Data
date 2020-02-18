import matplotlib.pyplot as plt
import numpy as np

input=[7, 9, 27, 28, 55, 45, 34, 65, 54, 67, 34, 23, 24, 66, 53, 45, 44, 88, 22, 33, 55, 35, 33, 37, 47, 41,31, 30,
29, 12]

n, bins, patches = plt.hist(x=input, bins=np.arange(int(min(input)/10)*10-10,max(input)+10,5), color='#0504aa')
plt.grid(axis='y', alpha=0.4)
plt.xlabel('Value')
plt.ylabel('Frequency')
maxfreq = n.max()
# Set a clean upper y-axis limit.
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
plt.show()

#sort of normal
