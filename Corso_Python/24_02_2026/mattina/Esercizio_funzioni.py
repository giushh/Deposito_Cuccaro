"""
1. Crea un array di 12 numeri equidistanti tra 0 e 1 usando linspace.
2. Cambia la forma dell'array a una matrice 3x4.
3. Genera una matrice 3x4 di numeri casuali tra 0 e 1.
4. Calcola e stampa la somma degli elementi di entrambe le matrici.
"""

import numpy as np

# 1
arr = np.linspace(0, 1, 12)
print("\nArray originale:", arr)
print("Shape:", arr.shape)

# 2
arr = arr.reshape(3, 4)
print("\nArray ridimensionato in matrice 3x4:\n", arr)
print("Shape:", arr.shape)

# 3
mat = np.random.rand(3, 4)
print("\nMatrice 3x4 casuale tra 0 e 1:\n", mat)

# 4
print("\nSomma prima matrice:", arr.sum())
print("Somma seconda matrice:", mat.sum())