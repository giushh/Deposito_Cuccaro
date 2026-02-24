"""
Esercizio 1: Somma e Media di Elementi
- Creare un array NumPy di 15 elementi contenente numeri casuali compresi tra 1 e 100.
- Calcolare e stampare la somma di tutti gli elementi dell'array.
- Calcolare e stampare la media di tutti gli elementi dell'array.

Esercizio 2: Manipolazione di Array Multidimensionali
- Creare una matrice 5x5 contenente numeri interi sequenziali da 1 a 25.
- Estrarre e stampare la seconda colonna della matrice.
- Estrarre e stampare la terza riga della matrice.
- Calcolare e stampare la somma degli elementi della diagonale principale della matrice.

Esercizio 3: Operazioni con Fancy Indexing
- Creare un array NumPy di forma (4, 4) contenente numeri casuali interi tra 10 e 50.
- Utilizzare fancy indexing per selezionare e stampare gli elementi agli indici (0,1), (1,3), (2,2) e (3,0).
- Utilizzare fancy indexing per selezionare e stampare tutte le righe dispari dell'array
  (considerando la numerazione delle righe che parte da 0).
- Modificare gli elementi selezionati nel primo punto dell'esercizio aggiungendo 10 al loro valore.
"""

import numpy as np


# 1
print("\n***** Esercizio 1: Somma e Media di Elementi *****")

array = np.random.randint(1, 101, 15)
print("\nArray di 15 numeri casuali tra 1 e 100:\n", array)

somma = array.sum()
media = array.mean()

print("\nSomma degli elementi:", somma)
print("Media degli elementi:", media)


# 2
print("\n***** Esercizio 2: Manipolazione di Array Multidimensionali *****")

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

# 3
print("\n***** Esercizio 3: Operazioni con Fancy Indexing *****")

matrice = np.random.randint(10, 51, (4, 4))
print("\nMatrice iniziale:\n", matrice)

righe = [0, 1, 2, 3]
colonne = [1, 3, 2, 0]

elementi = matrice[righe, colonne]
print("\nElementi selezionati agli indici (0,1), (1,3), (2,2), (3,0):\n", elementi)

righe_dispari = matrice[[1, 3], :]
print("\nRighe dispari:\n", righe_dispari)

matrice[righe, colonne] = matrice[righe, colonne] + 10

print("\nMatrice dopo aver aggiunto 10:\n", matrice)