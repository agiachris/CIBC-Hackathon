import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture

def Learn(X, n, state):
    gmm = GaussianMixture(n_components=n, covariance_type='spherical', random_state=0).fit(X)
    labels = gmm.predict(X)
    plt.scatter(X[:, 1], X[:, 4], c=labels, s=1, cmap='viridis');
    plt.xlabel("Provider Type")
    plt.ylabel("Dollar Amount of Claim")
    plt.title(state)
    plt.show()
    return gmm.score_samples(X)