# -*- coding: utf-8 -*-

from . import np

class VectApEn(object):
    """
    VectApEn
    Version 0.0.1
    """

    def __init__(self):
        pass
    
    def apen(self, L, m, r):
        """        
        Calculates approximate entropy (ApEn) of a time series.
        
        Input
            L: Time series
            m: Template length
            r: Tolerance level
             
        Output: 
            ApEn
        """
        N = len(L)
    
        B = np.zeros(N-m)
        A = np.zeros(N-m)
    
        # Divide time series and save all templates of length m
        xmi = [L[i:i+m] for i in range(N-m)]
        xmj = [L[i:i+m] for i in range(N-m+1)]
        
        # Compute each B_i
        seq = range(len(xmi))
        for i in seq:
            B[i] = np.sum(np.abs(xmi[i]-xmj).max(axis=1) <= r)
        
        # Similar method to compute each A_i
        m += 1
        xm = [L[i:i+m] for i in range(N-m+1)]
        
        seq = range(len(xm))
        for i in seq: 
            A[i] = np.sum(np.abs(xm[i]-xm).max(axis=1) <= r)
            
        # Compute and return ApEn
        m -= 1
        ApEn = -np.sum(np.log(np.divide(A,B)))/(N-m)
        return ApEn
