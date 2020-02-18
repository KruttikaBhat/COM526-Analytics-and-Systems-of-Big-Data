import matplotlib.pyplot as plt
import numpy as np

grades={"S":31,"B":29,"C":25,"D":100-(31+29+25)}

f=plt.figure(1)
plt.pie(grades.values(),labels=grades.keys(),autopct='%1.1f%%')


f1=plt.figure(2)
plt.bar(np.arange(len(grades)), grades.values(), align='center', alpha=0.5)
plt.xticks(np.arange(len(grades)), grades.keys())
plt.ylabel('Number')
plt.title('Grade Distribution')
plt.show()
