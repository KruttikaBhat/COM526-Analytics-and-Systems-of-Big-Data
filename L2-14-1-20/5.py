import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

input=[35, 54, 60, 65, 66, 67, 69, 70, 72, 73, 75, 76, 54, 25, 15, 60, 65, 66, 67, 69, 70, 72, 130, 73, 75, 76]


sns.set_style("whitegrid")
ax = sns.boxplot(x=input,color="green")
ax = sns.swarmplot(x=input, color='grey')
plt.xlabel("no of chairs")

plt.show()
