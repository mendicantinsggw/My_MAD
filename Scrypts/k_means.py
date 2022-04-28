# k-means clustering
from numpy import unique
from numpy import where
from sklearn.cluster import KMeans
from matplotlib import pyplot
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Database/Grouped_by_type.csv', header=0)

X = dataset.iloc[:, 1:9].values

"""
# Use head() function to return the first 5 rows:
dataset.head()
# Assign values to the X and y variables:
X = dataset.iloc[:, 1:9].values
print("X___________")
print(X)

# define dataset
#X, _ = make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1, random_state=4)
print(X)
# define the model
model = KMeans(n_clusters=8)
# fit the model
model.fit(X)
# assign a cluster to each example
yhat = model.predict(X)
# retrieve unique clusters
clusters = unique(yhat)
# create scatter plot for samples from each cluster
for cluster in clusters:
    # get row indexes for samples with this cluster
    row_ix = where(yhat == cluster)
    # create scatter of these samples
    pyplot.scatter(X[row_ix, 0], X[row_ix, 1], X[row_ix, 2])
# show the plot
pyplot.show()
"""
#We always can divide on strict sience and non strict
print(X)
plt.scatter(X[:, 0], X[:, 1], s=50)
plt.show()

# compute K-Means
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.show()