# Required Libraries
import matplotlib.pyplot as plt
# GMM Machine Learning Algorithm
from sklearn.mixture import GMM

def Learn(X, n):
    gmm = GMM(n_components=n).fit(X)
    labels = gmm.predict(X)
    plt.scatter(X[:, 0], X[:, 2], c=labels, s=40, cmap='viridis');
    plt.scatter(X[:, 1], X[:, 2], c=labels, s=40, cmap='viridis');