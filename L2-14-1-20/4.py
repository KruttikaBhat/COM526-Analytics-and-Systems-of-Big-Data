import matplotlib.pyplot as plt
from scipy.stats import pearsonr

fuel=[3.6, 6.7, 9.8, 11.2, 14.7]
mass=[0.45, 0.91, 1.36, 1.81,2.27]

plt.scatter(mass,fuel)
plt.xlabel("Mass (metric tons)")
plt.ylabel("Fuel used(L)")
plt.show()

corr, _ = pearsonr(mass, fuel)
print('Pearsons correlation: %.3f' % corr)
