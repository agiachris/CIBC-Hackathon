import numpy as np
from sklearn.mixture import GMM


def Number(rawData)
        bicArray = []
        #aicArray = []
        n_components = np.arange(1, 20)
        models = [GMM(n, covariance_type='full', random_state=0).fit(rawData) for n in n_components]
        for m in models    
            bicArray.append(m.bic(rawData))
            #aicArray.append(m.aic(rawData))
        return min(bicArray)