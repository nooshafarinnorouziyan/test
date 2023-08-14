import numpy as np
def is_sorted(arr):
    arr = np.array(arr)
    return np.all(arr[:-1]<=arr[1:])