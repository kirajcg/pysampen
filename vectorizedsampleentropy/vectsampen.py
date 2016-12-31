# -*- coding: utf-8 -*-

from . import np

class VectSampEn(object):    
    """
    VectSampEn
    Version 0.0.1
    """
    
    def __init__(self):
        pass
    
    def condprob(self, L, m, r):
        """ 
        Calculates the conditional probability A/B of a time series 
        
        Input: 
            L: Time series
            m: Template length
            r: Tolerance level
            
        Output: 
            Conditional probability
        """
        N = len(L)
        B = 0.0
        A = 0.0
    
        # Split time series and save all templates of length m
        xmi = [L[i:i+m] for i in range(N-m)]
        xmj = [L[i:i+m] for i in range(N-m+1)]
        
        # Save all matches minus the self-match, compute B
        seq = range(len(xmi))
        for i in seq:
            Bi = np.sum(np.abs(xmi[i]-xmj).max(axis=1) <= r)-1
            B += Bi
            
        # Similar for computing A
        m += 1
        xm = [L[i:i+m] for i in range(N-m+1)]
        
        seq = range(len(xm))
        for i in seq: 
            Ai = np.sum(np.abs(xm[i]-xm).max(axis=1) <= r)-1
            A += Ai
        
        # Return conditional probability
        return A/B
        
    def sampen(self, L, m, r):
        """ 
        Calculates sample entropy (SampEn) of a time series 
        
        Input: 
            L: Time series
            m: Template length
            r: Tolerance level
            
        Output: 
            SampEn
        """
        N = len(L)
        B = 0.0
        A = 0.0
    
        # Split time series and save all templates of length m
        xmi = [L[i:i+m] for i in range(N-m)]
        xmj = [L[i:i+m] for i in range(N-m+1)]
        
        # Save all matches minus the self-match, compute B
        seq = range(len(xmi))
        for i in seq:
            Bi = np.sum(np.abs(xmi[i]-xmj).max(axis=1) <= r)-1
            B += Bi
            
        # Similar for computing A
        m += 1
        xm = [L[i:i+m] for i in range(N-m+1)]
        
        seq = range(len(xm))
        for i in seq: 
            Ai = np.sum(np.abs(xm[i]-xm).max(axis=1) <= r)-1
            A += Ai
        
        # Return SampEn
        return -np.log(A/B)
        
    def qse(self, L, m, r):
        """ 
        Calculates quadratic sample entropy (QSE) of a time series 
        
        Input: 
            L: Time series
            m: Template length
            r: Tolerance level
            
        Output: 
            QSE
        """
        N = len(L)
        B = 0.0
        A = 0.0
    
        # Split time series and save all templates of length m
        xmi = [L[i:i+m] for i in range(N-m)]
        xmj = [L[i:i+m] for i in range(N-m+1)]
        
        # Save all matches minus the self-match, compute B
        seq = range(len(xmi))
        for i in seq:
            Bi = np.sum(np.abs(xmi[i]-xmj).max(axis=1) <= r)-1
            B += Bi
            
        # Similar for computing A
        m += 1
        xm = [L[i:i+m] for i in range(N-m+1)]
        
        seq = range(len(xm))
        for i in seq: 
            Ai = np.sum(np.abs(xm[i]-xm).max(axis=1) <= r)-1
            A += Ai
            
        # return QSE
        return -np.log(A/B)+np.log(2*r)