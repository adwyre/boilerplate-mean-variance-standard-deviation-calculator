import numpy as np

def calculate(list):
    new_array = np.reshape(list,(3,3))
    #Mean
    mean_1 = np.mean(new_array, axis=0)
    mean_2 = np.mean(new_array, axis=1)
    mean_all = np.mean(new_array)
    #Variance
    var_1 = np.var(new_array, axis=0)
    var_2 = np.var(new_array, axis=1)
    var_all = np.var(new_array)
    #Standard Deviation
    std_1 = np.std(new_array, axis=0)
    std_2 = np.std(new_array, axis=1)
    std_all = np.std(new_array)
    #Max
    max_1 = np.max(new_array, axis=0)
    max_2 = np.max(new_array, axis=1)
    max_all = np.max(new_array)
    #Min
    min_1 = np.min(new_array, axis=0)
    min_2 = np.min(new_array, axis=1)
    min_all = np.min(new_array)
    #Sum
    sum_1 = np.sum(new_array, axis=0)
    sum_2 = np.sum(new_array, axis=1)
    sum_all = np.sum(new_array)
    
    calculations = {
        'mean': [mean_1, mean_2, mean_all],
        'variance': [var_1, var_2, var_all],
        'standard deviation': [std_1, std_2, std_all],
        'max': [max_1, max_2, max_all],
        'min': [min_1, min_2, min_all],
        'sum': [sum_1, sum_2, sum_all]
    }
    return calculations



    return calculations
