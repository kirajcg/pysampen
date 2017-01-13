# -*- coding: utf-8 -*-

from . import np


class VectSampEn(object):    
    """
    VectSampEn
    Version 0.0.3
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
        xmi = np.array([L[i:i+m] for i in range(N-m)])
        xmj = np.array([L[i:i+m] for i in range(N-m+1)])
        
        # Save all matches minus the self-match, compute B
        B = np.sum([np.sum(np.abs(xmii-xmj).max(axis=1) <= r)-1 for xmii in xmi])
            
        # Similar for computing A
        m += 1
        xm = np.array([L[i:i+m] for i in range(N-m+1)])
        
        A = np.sum([np.sum(np.abs(xmi-xm).max(axis=1) <= r)-1 for xmi in xm])
         
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
        xmi = np.array([L[i:i+m] for i in range(N-m)])
        xmj = np.array([L[i:i+m] for i in range(N-m+1)])
        
        # Save all matches minus the self-match, compute B
        B = np.sum([np.sum(np.abs(xmii-xmj).max(axis=1) <= r)-1 for xmii in xmi])
            
        # Similar for computing A
        m += 1
        xm = np.array([L[i:i+m] for i in range(N-m+1)])
        
        A = np.sum([np.sum(np.abs(xmi-xm).max(axis=1) <= r)-1 for xmi in xm])
        
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
        xmi = np.array([L[i:i+m] for i in range(N-m)])
        xmj = np.array([L[i:i+m] for i in range(N-m+1)])
        
        # Save all matches minus the self-match, compute B
        B = np.sum([np.sum(np.abs(xmii-xmj).max(axis=1) <= r)-1 for xmii in xmi])
            
        # Similar for computing A
        m += 1
        xm = np.array([L[i:i+m] for i in range(N-m+1)])
        
        A = np.sum([np.sum(np.abs(xmi-xm).max(axis=1) <= r)-1 for xmi in xm])
            
        # return QSE
        return -np.log(A/B)+np.log(2*r)


_inst = VectSampEn()
condprob = _inst.condprob
sampen = _inst.sampen
qse = _inst.qse