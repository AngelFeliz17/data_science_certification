import numpy as np

def calculate(list):

    if list.size < 9 :
        raise ValueError("List must contain nine numbers.")

    col_mean = np.mean(list, axis=0)
    row_mean = np.mean(list, axis=1)
    mean = np.mean(list)

    col_var = np.var(list, axis=1)
    row_var = np.var(list, axis=0)
    var = np.var(list)

    col_std = np.std(list, axis=1)
    row_std = np.std(list, axis=0)
    std = np.std(list)

    col_max = np.max(list, axis=1)
    row_max = np.max(list, axis=0)
    max = np.max(list)

    col_min = np.min(list, axis=1)
    row_min = np.min(list, axis=0)
    min = np.min(list)

    col_sum = np.sum(list, axis=1)
    row_sum = np.sum(list, axis=0)
    sum = np.sum(list)

    calculations = {
        'mean': [col_mean, row_mean, mean],
        'variance': [col_var, row_var, var],
        'standard deviation': [col_std, row_std, std],
        'max': [col_max, row_max, max],
        'min': [col_min, row_min, min],
        'sum': [col_sum, row_sum, sum]
    }

    return calculations