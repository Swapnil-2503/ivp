from sklearn.cluster import Birch
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Generate sample data
X, _ = make_blobs(n_samples=300, centers=4, random_state=42)

# Initialize the Birch clustering algorithm
birch = Birch(threshold=0.5, n_clusters=4)

# Fit the model to the data
birch.fit(X)

# Predict cluster labels
labels = birch.predict(X)

# Plot the results
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', edgecolors='k', s=30)
plt.title('Birch Clustering')
plt.show()
