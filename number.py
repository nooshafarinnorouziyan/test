import numpy as np

def is_sorted(arr, ascending=True):
    arr = np.array(arr)
    if not ascending:
       arr = -arr  # invert the array for descending order
    return np.all(arr[:-1] <= arr[1:])
