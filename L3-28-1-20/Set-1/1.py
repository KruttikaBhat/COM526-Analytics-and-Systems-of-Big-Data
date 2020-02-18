import numpy as np

age=[13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33,33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]

#Min-max normalization
mx=1
mn=0
val=25
X_std = (val - age[0]) / (age[-1] - age[0])
X_scaled = X_std * (mx - mn) + mn
print("Min-max normalization: "+str(X_scaled))

#X_scaled = scale * X + min - X.min(axis=0) * scale
#where scale = (max - min) / (X.max(axis=0) - X.min(axis=0))

#z-score normalization
mean=np.mean(age)
dev=12.94
print("Z score normalization: "+str((val-mean)/dev))

#decimal scaling
power=len(str(age[-1]))
print("Decimal scaling: "+str(val/pow(10,power)))
