import matplotlib.pyplot as plt
from scipy.stats import pearsonr

temp=[98,87,90,85,95,75]
customers=[15,12,10,10,16,7]

corr, _ = pearsonr(temp, customers)
print('Pearsons correlation: %.3f' % corr)
