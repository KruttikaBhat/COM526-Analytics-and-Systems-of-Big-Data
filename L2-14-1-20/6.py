import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

mu, sigma = 0, 0.1
s = np.random.normal(mu, sigma, 1000)

f=plt.figure(1)
sns.set(style="whitegrid")
ax = sns.violinplot(s)
plt.xlabel("Standard-Normal Distribution")

f1=plt.figure(2)
mu, sigma = 3., 1. # mean and standard deviation
s = np.random.lognormal(mu, sigma, 1000)

ax = sns.violinplot(s)
plt.xlabel("Log distribution")
plt.show()
