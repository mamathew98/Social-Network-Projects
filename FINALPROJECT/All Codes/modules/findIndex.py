import numpy as np


def findIndex(arr, val):
    index = np.where(arr == val)
    print(index)
    return index[0]
