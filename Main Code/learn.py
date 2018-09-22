# Required Libraries
import matplotlib.pyplot as plt
# GMM Machine Learning Algorithm
from sklearn.mixture import GaussianMixture

def Learn(X, n):
    gmm = GaussianMixture(n_components=n, covariance_type='full', random_state=0).fit(X)
    labels = gmm.predict(X)
    plt.scatter(X[:, 0], X[:, 2], c=labels, s=40, cmap='viridis');
    plt.scatter(X[:, 1], X[:, 2], c=labels, s=40, cmap='viridis');