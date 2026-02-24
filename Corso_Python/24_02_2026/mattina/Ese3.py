"""
NumPy

Esercizio 1: Somma e Media di Elementi
- Creare un array NumPy di 15 elementi contenente numeri casuali compresi tra 1 e 100.
- Calcolare e stampare la somma di tutti gli elementi dell'array.
- Calcolare e stampare la media di tutti gli elementi dell'array.

Esercizio 2: Manipolazione di Array Multidimensionali
- Creare una matrice 5x5 contenente numeri interi sequenziali da 1 a 25.
- Estrarre e stampare la seconda colonna della matrice.
- Estrarre e stampare la terza riga della matrice.
- Calcolare e stampare la somma degli elementi della diagonale principale della matrice.
"""

import numpy as np


# 1
print("***** Esercizio 1: Somma e Media di Elementi *****")

array = np.random.randint(1, 101, 15)
print("\nArray di 15 numeri casuali tra 1 e 100:\n", array)

somma = array.sum()
media = array.mean()

print("\nSomma degli elementi:", somma)
print("Media degli elementi:", media)


# 2
print("\n\n***** Esercizio 2: Manipolazione di Array Multidimensionali *****")

matrice = np.arange(1, 26).reshape(5, 5)
print("\nMatrice 5x5 (numeri da 1 a 25):\n", matrice)

seconda_colonna = matrice[:, 1]
print("\nSeconda colonna:\n", seconda_colonna)

terza_riga = matrice[2, :]
print("\nTerza riga:\n", terza_riga)

diagonale = np.diag(matrice)
somma_diagonale = diagonale.sum()

print("\nDiagonale principale:\n", diagonale)
print("Somma della diagonale principale:", somma_diagonale)