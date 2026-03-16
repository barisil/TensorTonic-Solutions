def weighted_moving_average(values, weights):
    """
    Compute the weighted moving average using the given weights.
    """
    window_size = len(weights)
    down = sum(weights)
    WMA = list()
    
    if len(values) < len(weights) :
        return 0
    if min(weights) < 0 :
        return 0
    for i in range(len(values) - window_size + 1) :
        up = 0
        for j in range(window_size) :
            up += weights[j] * values[i+j]
        result = up / down   
        WMA.append(result)
    return WMA
            