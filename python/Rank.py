```python
import sympy as sp

a = sp.symbols('a')

A = sp.Matrix([
    [1, 2, 1],
    [2, 4, 2],
    [3, 6, a]
])

print("Matrix A:")
sp.pprint(A)

print("Rank of A:", A.rank())

print("When a = 3:")
print(A.subs(a, 3).rank())

print("When a != 3, rank of A = 2")
```
