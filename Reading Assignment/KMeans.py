from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
import numpy as np

#load the data
X, y = load_iris(return_X_y=True)

#fit the data, consider 3 clusters
km = KMeans(n_clusters = 3, n_jobs = 4, random_state=21)
km=km.fit(X)
centers = km.cluster_centers_
print(centers)

new_labels = km.labels_

# Plot the identified clusters and compare with the answers
fig, axes = plt.subplots(1, 2, figsize=(16,8))

axes[0].scatter(X[:, 0], X[:, 1], c=y, cmap='gist_rainbow',edgecolor='k', s=150)
axes[1].scatter(X[:, 0], X[:, 1], c=new_labels, cmap='jet',edgecolor='k', s=150)

axes[0].set_xlabel('Sepal length', fontsize=18)
axes[0].set_ylabel('Sepal width', fontsize=18)
axes[1].set_xlabel('Sepal length', fontsize=18)
axes[1].set_ylabel('Sepal width', fontsize=18)

axes[0].tick_params(direction='in', length=10, width=5, colors='k', labelsize=20)
axes[1].tick_params(direction='in', length=10, width=5, colors='k', labelsize=20)

axes[0].set_title('Actual', fontsize=18)
axes[1].set_title('Predicted', fontsize=18)
plt.show()


# k-means cluster analysis for 1-15 clusters
clusters=range(1,15)
meandist=[]

"""
Loop through each cluster and fit the model to the train set.
Generate the predicted cluster and append the mean
distance by taking the sum divided by the shape.

Plot average distance from observations from the cluster centroid
to use the Elbow Method to identify number of clusters to choose
"""
for k in clusters:
    model=KMeans(n_clusters=k)
    model.fit(X)
    clusassign=model.predict(X)
    meandist.append(sum(np.min(cdist(X, model.cluster_centers_, 'euclidean'), axis=1))
    / X.shape[0])


plt.plot(clusters, meandist)
plt.xlabel('Number of clusters')
plt.ylabel('Average distance')
plt.title('Selecting k with the Elbow Method')
plt.show()
