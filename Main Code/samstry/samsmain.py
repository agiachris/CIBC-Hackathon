import parse
import numpy as np
import sklearn
import matplotlib.pyplot as plt
import matplotlib
from sklearn import cluster, datasets
if __name__ == "__main__":
    dataset = parse.Normalize('/home/samuel/Desktop/CIBCData', 100)
    subset = parse.Trim(dataset)
    x = np.r_[subset]
    k_means = cluster.KMeans(n_clusters=3)
    k_means.fit(x)
    print(k_means.labels_[::10])



