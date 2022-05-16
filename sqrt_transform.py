import numpy as np

def sqrt_transform(x, inverse=False):
    """Square and Square Root Transformation Helper Function"""
    
    if not inverse:
        return np.sqrt(x)
    
    else:
        return x **2