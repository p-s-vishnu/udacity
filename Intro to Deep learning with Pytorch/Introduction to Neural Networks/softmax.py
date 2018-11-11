import numpy as np
from math import exp

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    denominator = sum([exp(i) for i in L])
    L_softmax   = [ exp(j)/denominator for j in L ]
    return L_softmax
    
    # L_exp = np.exp(L)
    # return np.divide(L_exp, L_exp.sum())