# k-means clustering
from numpy import unique
from numpy import where
from sklearn.cluster import KMeans
from matplotlib import pyplot
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Database/Grouped_by_type.csv', header=0)

X = dataset.iloc[:, 1:9].values

#Divide data into strict and non-strict science
print(X) # 
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