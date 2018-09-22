import numpy as np
from sklearn.mixture import GMM

def Number(rawData):
    bicArray = []
    # aicArray = []
    n_components = np.arange(1, 20)
    # models = [GMM(n, covariance_type='full', random_state=0).fit(rawData) for n in n_components]
    print ("In CRIT")
    for m in range(21):
        bicArray.append(GMM(m, covariance_type='full', random_state=0).fit(rawData))
        # bicArray.append(m.bic(rawData))
        #aicArray.append(m.aic(rawData))
    print("OH MA NAME")
    return min(bicArray)