# k-means clustering
from numpy import unique
from numpy import where
from sklearn.cluster import KMeans
from matplotlib import pyplot
import pandas as pd
import matplotlib.pyplot as plt

# get data from file
dataset = pd.read_csv('Database/Grouped_by_type.csv', header=0)

X = dataset.iloc[:, 1:].values # get data without labels

# Divide data into strict and non-strict science
# X - strict science
# Y - non-strict science
print(X) # output data for each region
plt.scatter(X[:, 0], X[:, 1], s=50)
plt.show()
# each dot is different region

# compute K-Means
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.show()
# regions on the chart are grouped into 4 groups, which is shown by their color
