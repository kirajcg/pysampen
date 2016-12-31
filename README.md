# vectorized-sample-entropy
Vectorized versions of sample entropy (SampEn) and approximate entropy (ApEn)

Dependencies: numpy>=1.11.2

To import: 
```python
from vectorizedsampleentropy import VectSampEn
from vectorizedsampleentropy import VectApEn
```

Functions: 
```python
VectSampEn.condprob # Calculates conditional probability A/B
VectSampEn.sampen   # Calculates sample entropy
VectSampEn.qse      # Calculates quadratic sample entropy
VectApEn.apen       # Calculates approximate entropy
```

Usage examples: 
```python
from pyscbwrapper import VectSampEn
import numpy as np

VSE = VectSampEn()
L = np.random.normal(0, 1, 1000)
r = 0.2*np.std(L)
m = 1
VSE.sampen(L, m, r)
```
