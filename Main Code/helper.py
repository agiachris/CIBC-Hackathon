# Required Libraries
import matplotlib.pyplot as plt
# GMM Machine Learning Algorithm
from sklearn.mixture import GMM

def Learn(n, X):
    gmm = GMM(n_components=n).fit(X)
    labels = gmm.predict(X)
    plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap='viridis');