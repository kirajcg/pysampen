# -*- coding: utf-8 -*-

from . import np


class VectApEn(object):
    """
    VectApEn
    Version 0.0.3
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
    
        # Divide time series and save all templates of length m
        xmi = np.array([L[i:i+m] for i in range(N-m)])
        xmj = np.array([L[i:i+m] for i in range(N-m+1)])
        
        # Compute each B_i            
        B = [np.sum(np.abs(xmii-xmj).max(axis=1) <= r) for xmii in xmi]
        
        # Similar method to compute each A_i
        m += 1
        xm = np.array([L[i:i+m] for i in range(N-m+1)])
        
        A = [np.sum(np.abs(xmi-xm).max(axis=1) <= r) for xmi in xm]
            
        # Compute and return ApEn
        m -= 1
        ApEn = -np.sum(np.log(np.divide(A,B)))/(N-m)
        return ApEn


_inst = VectApEn()
apen = _inst.apen