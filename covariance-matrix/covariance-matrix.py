import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    X = np.asanyarray(X)
    dim = X.ndim
    a = X.shape[0] if dim >=1 else 0 
    if dim < 2 or a <= 1 :
        return None
    else :
        mean = np.mean(X,axis = 0)
        X_centered = X - mean
        a,b = X_centered.shape
        return np.dot(X_centered.T,X_centered) / (a-1)
    
    pass