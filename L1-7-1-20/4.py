import numpy as np
from scipy import stats

input=[167.65, 167, 172, 175, 165, 167, 168, 167, 167.3, 170, 167.5, 170, 167, 169, 172]
[mean,mode,median,stnd]=[np.mean(input),stats.mode(input)[0][0],np.median(input),np.std(input)]
print("Mean: ",mean)
print("Median: ",median)
print("Mode: ",mode)
print("Standard Dev: ",stnd)
print("Measure of skewness:",(mean-mode)/stnd)
