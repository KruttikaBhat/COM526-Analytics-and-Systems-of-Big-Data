from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

#load the data
X, y = load_iris(return_X_y=True)

# generate the linkage matrix
Z = linkage(X, 'ward')

# max_d means max_distance
max_d = 7.08

plt.figure(figsize=(25, 10))
plt.title('Iris Hierarchical Clustering Dendrogram',fontsize=20)
plt.xlabel('Index',fontsize=20)
plt.ylabel('Distance',fontsize=20)
dendrogram(
    Z,
    truncate_mode='lastp',  # show only the last p merged clusters
    p=150,
    leaf_rotation=90.,      # rotates the x axis labels
    leaf_font_size=8.,      # font size for the x axis labels
)
plt.axhline(y=max_d, c='k')
plt.show()

plt.figure(figsize=(25, 10))
plt.title('Iris Hierarchical Clustering Dendrogram',fontsize=20)
plt.xlabel('Index',fontsize=20)
plt.ylabel('Distance',fontsize=20)
dendrogram(
    Z,
    truncate_mode='lastp',
    p=50,
    leaf_rotation=90.,
    leaf_font_size=8.,     
)
plt.axhline(y=max_d, c='k')
plt.show()
