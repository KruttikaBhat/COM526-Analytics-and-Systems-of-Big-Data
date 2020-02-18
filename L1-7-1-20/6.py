import matplotlib.pyplot as plt
import numpy as np

activities={"Studying":33,"Sleeping":30,"Playing":18,"Hobbies":5,"Friends and Family":100-(33+30+18+5)}
plt.pie(activities.values(),labels=activities.keys(),autopct='%1.1f%%')
plt.show()
