import numpy as np
from sklearn.mixture import GaussianMixture

def Number(rawData):
    bicArray = []
    n_components = np.arange(1, 100)
    for i in range(len(n_components)):
        model = GaussianMixture(n_components=i+1, covariance_type='full', random_state=0).fit(rawData)
        bicArray.append(model.bic(rawData))
        # Possible Parameters: max_iter
    return bicArray.index(min(bicArray))