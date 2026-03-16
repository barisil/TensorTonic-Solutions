import numpy as np 
def weighted_moving_average(values, weights):
    """
    Compute the weighted moving average using the given weights.
    """
    window_size = len(weights)
    down = sum(weights)
    WMA = list()
    
    if len(values) < window_size :
        return []
    if min(weights) <= 0 or window_size == 0 :
        return []
    
    for i in range(len(values) - window_size + 1) :
        window_sum = sum(weights[j] * values[i+j] for j in range(window_size))   
        WMA.append(window_sum/down)
    return WMA

    