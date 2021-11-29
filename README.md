# pysampen
Version 0.1.0

Vectorized implementations of sample entropy (SampEn) and approximate entropy (ApEn)

Dependencies: numpy>=1.11.2

To import: 
```python
from pysampen import sampen
from pysampen import apen
```

Functions: 
```python
sampen.condprob(L, m, r) # Calculates conditional probability A/B
sampen.sampen(L, m, r)   # Calculates sample entropy
sampen.qse(L, m, r)      # Calculates quadratic sample entropy
apen.apen(L, m, r)       # Calculates approximate entropy
```

Usage examples: 
```python
from pysampen import sampen
import numpy as np

L = np.random.normal(0, 1, 1000)
r = 0.2*np.std(L)
m = 1
sampen.sampen(L, m, r)
```
