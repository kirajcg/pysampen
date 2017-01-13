# vectorized-sample-entropy
Version 0.0.3

Vectorized implementations of sample entropy (SampEn) and approximate entropy (ApEn)

Dependencies: numpy>=1.11.2

To import: 
```python
import vectorizedsampleentropy as vse
```

Functions: 
```python
condprob(L, m, r) # Calculates conditional probability A/B
sampen(L, m, r)   # Calculates sample entropy
qse(L, m, r)      # Calculates quadratic sample entropy
apen(L, m, r)     # Calculates approximate entropy
```

Usage examples: 
```python
import vectorizedsampleentropy as vse
import numpy as np

L = np.random.normal(0, 1, 1000)
r = 0.2*np.std(L)
m = 1
vse.sampen(L, m, r)
```
