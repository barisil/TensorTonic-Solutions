def rolling_std(values, window_size):
    """
    Compute the rolling population standard deviation.
    """
    results = []
    for i in range(len(values) - window_size + 1 ) :
        window = values[i:i+window_size]
        mean = sum(window) / window_size
        var = sum((x - mean)**2 for x in window) / window_size
        std = var ** 0.5
        results.append(std)
    
        

    return results