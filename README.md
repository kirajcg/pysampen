# vectorized-sample-entropy
Version 0.0.3

Vectorized implementations of sample entropy (SampEn) and approximate entropy (ApEn)

Dependencies: numpy>=1.11.2

To import: 
```python
from vectorizedsampleentropy import vectsampen as vse
from vectorizedsampleentropy import vectapen as vae
```

Functions: 
```python
vectsampen.condprob(L, m, r) # Calculates conditional probability A/B
vectsampen.sampen(L, m, r)   # Calculates sample entropy
vectsampen.qse(L, m, r)      # Calculates quadratic sample entropy
vectapen.apen(L, m, r)       # Calculates approximate entropy
```

Usage examples: 
```python
from vectorizedsampleentropy import vectsampen as vse
import numpy as np

L = np.random.normal(0, 1, 1000)
r = 0.2*np.std(L)
m = 1
vse.sampen(L, m, r)
```
