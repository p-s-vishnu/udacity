import numpy as np

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    Y = np.float_(Y)
    P = np.float_(P)
    
    positive_entropy = Y * np.log(P)
    negative_entropy = (1 - Y) * np.log(1 - P)
    
    return -np.sum(positive_entropy + negative_entropy)