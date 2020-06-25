import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

#data point coordinates
x=[2,2,8,5,7,6,1,4]
y=[10,5,4,8,5,4,2,9]


#K Means

#c1 and c2 represent the indices of the clustered points. Change accordingly to get the centroids and k1 and k2 distances
c1=[1,2,3,4]
c2=[5,6,7,8]

x1list=[]
y1list=[]
for i in c1:
	x1list.append(x[i-1])
	y1list.append(y[i-1])
k1=[np.mean(x1list),np.mean(y1list)] #k1 values
print(k1)

x2list=[]
y2list=[]
for i in c2:
	x2list.append(x[i-1])
	y2list.append(y[i-1])
k2=[np.mean(x2list),np.mean(y2list)] #k2 values

(print(k2))


#get k1 and k2 distances
k=k1
for i,j in zip(x,y):
    val=math.sqrt( ((i-k[0])**2) + ((j-k[1])**2) )
    print("{:.2f}".format(val))
print("k2 distances")

k=k2
for i,j in zip(x,y):
	val=math.sqrt( ((i-k[0])**2) + ((j-k[1])**2) )
	print("{:.2f}".format(val))



"""
#K medoids

# Maually change the values for k1 and k2
k1=[4,5]
k2=[7,3]

k=k1

vals=[]
list=[]
for i,j in zip(x,y):
	val= math.sqrt( ((i-k[0])**2) + ((j-k[1])**2) )
	print("{:.2f}".format(val))
	list.append(val)
vals.append(list)
list=[]

print("k2")
k=k2
for i,j in zip(x,y):
	val= math.sqrt( ((i-k[0])**2) + ((j-k[1])**2) )
	print("{:.2f}".format(val))
	list.append(val)

vals.append(list)
cost=[]
for i in range(10):
	cost.append(min(np.array(vals)[:,i]))

print("Cost= {:.2f}".format(sum(cost)))
"""

"""
#Agglomerative

#manually change x and y for each step of the trace
proximity=[]
for i,j in zip(x,y):
	list=[]
	for m,n in zip(x,y):
		list.append(math.sqrt( ((i-m)**2) + ((j-n)**2) ))
	proximity.append(list)

for i in proximity:
	print(i)

#make sure x and y have their initial values before running this part. It will construct the dendrogram given the set of datapoints.
X = []
for i,j in zip(x,y):
	X.append([i,j])
# generate the linkage matrix
Z = linkage(X, 'ward')

# calculate full dendrogram
plt.figure(figsize=(25, 10))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance')
dendrogram(
    Z,
    leaf_rotation=90.,  # rotates the x axis labels
    leaf_font_size=8.,  # font size for the x axis labels
)
plt.show()
"""

"""
#Divisive

from sklearn.cluster import KMeans

#First split
X=[]
for i,j in zip(x,y):
	X.append([i,j])

km = KMeans(n_clusters = 2)
km=km.fit(X)
print(km.labels_) #This will give the clusters


#c1 and c2 are serial numbers of the data points for clusters 1 and 2 resp
#Change the index values based on the cluster you want to split
c1=[3,4,5] #first cluster
c2=[2,8,9] #second cluster

x1list=[]
y1list=[]
for i in c2: #change to c1 or c2 based on which cluster you want to apply k means to
	x1list.append(x[i])
	y1list.append(y[i])
X=[]
for i,j in zip(x1list,y1list):
	X.append([i,j])

km = KMeans(n_clusters = 2)
km=km.fit(X)
print(km.labels_) #This will give the clusters
"""
