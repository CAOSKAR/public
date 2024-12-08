import numpy as np

def comparr(arr1,arr2):
    a = np.array(arr1)
    b = np.array(arr2)
    return np.setdiff1d(a,b)