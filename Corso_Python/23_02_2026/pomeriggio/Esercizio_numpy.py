# pomeriggio 23/02/2026

"""
Esercizio 1
    Crea un array NumPy utilizzando arange e
    verifica il tipo di dato (dtype) e la forma
    (shape) dell'array.
    Esercizio:
        1.Utilizza la funzione np.arange per creare
        un array di numeri interi da 10 a 49.
        
        2.Verifica il tipo di dato dell'array e
        stampa il risultato.
        
        3.Cambia il tipo di dato dell'array in
        float64 e verifica di nuovo il tipo di
        dato.
        
        4.Stampa la forma dell'array.
        
Esercizio 2
    1. Crea un array NumPy 1D di 20 numeri interi casuali compresi tra 10 e 50.
    2. Utilizza lo slicing per estrarre i primi 10 elementi dell'array.
    3. Utilizza lo slicing per estrarre gli ultimi 5 elementi
    dell'array.
    4. Utilizza lo slicing per estrarre gli elementi dall'indice 5
    all'indice 15 (escluso).
    5. Utilizza lo slicing per estrarre ogni terzo elementodell'array.
    6. Modifica, tramite slicing, gli elementi dall'indice 5
    all'indice 10 (escluso) assegnando loro il valore 99.
    7. Stampa l'array originale e tutti i sottoarray ottenuti tramite slicing.
    
    Obiettivo:
    Esercitarsi nell'u
    tilizzo dello slicing di NumPy per estrarre e
    modificare sottoarray specifici da un array più grande.
"""

import numpy as np

print("********** Esercizio 1 ***********")
arr = np.arange(10, 50, 1) # il 50 non è incluso
print("\nArray creato ", arr)

print("\nTipo di dato dell'array:", arr.dtype)

print("\nCambio tipo di dato")
arr.dtype='float64'

print("\nNuovo tipo di dato dell'array:", arr.dtype)

print("\nForma dell'array", arr.shape)


print("*********** Esercizio 2 ***********")

# 1. array 1d di 20 numeri interi casuali tra 10 e 50
arr2 = np.random.randint(10, 51, 20)

print("\nArray originale:", arr2)

# 2. primi 10 elementi
print("\nPrimi 10 elementi:", arr2[:10])

# 3. ultimi 5 elementi
print("\nUltimi 5 elementi:", arr2[-5:])

# 4. elementi dall'indice 5 all'indice 15 escluso
print("\nElementi da indice 5 a 15 escluso:", arr2[5:15])

# 5. ogni terzo elemento
print("\nOgni terzo elemento:", arr2[::3])

# 6. modifica elementi dall'indice 5 a 10 escluso assegnando 99
arr2[5:10] = 99

print("\nArray dopo modifica indici 5:10:", arr2)


# pomeriggio 23/02/2026
# esercizio 3: slicing su matrici 2d




print("*********** Esercizio 3 ***********")

# 1. crea una matrice 6x6 con interi casuali tra 1 e 100
arr3 = np.random.randint(1, 101, (6, 6))
print("\nMatrice originale (6x6):\n", arr3)

# 2. estrai la sotto-matrice centrale 4x4
centrale_4x4 = arr3[1:5, 1:5]
print("\nSotto-matrice centrale (4x4):\n", centrale_4x4)

# 3. inverti le righe della matrice estratta (solo righe, non colonne)
invertita = centrale_4x4[::-1, :]
print("\nMatrice centrale con righe invertite:\n", invertita)

# 4. estrai la diagonale principale della matrice invertita
diagonale = np.diag(invertita)
print("\nDiagonale principale della matrice invertita:", diagonale)

# 5. sostituisci i multipli di 3 con -1 (nuova variabile)
modificata = invertita.copy()
modificata[modificata % 3 == 0] = -1
print("\nMatrice invertita modificata:\n", modificata)

# 6. confronto finale richiesto
print("\n--- Confronto ---")
print("\nMatrice originale:\n", arr3)
print("\nSotto-matrice centrale 4x4:\n", centrale_4x4)
print("\nMatrice invertita (righe):\n", invertita)
print("\nDiagonale principale:\n", diagonale)
print("\nMatrice modificata:\n", modificata)

print("\n*********** Extra esercizio 3 ***********")

# calcolo somma totale della matrice invertita
print("\nSomma totale invertita:", invertita.sum())

# calcolo media per riga
print("\nMedia per riga invertita:", invertita.mean(axis=1)) 
# axis indica la dimensione lungo la quale applicare il metodo (0 sulle y-colonne, 1 sulle x-righe)

# ordino ogni riga della matrice invertita
ordinata_righe = np.sort(invertita, axis=1)
print("\nRighe ordinate:\n", ordinata_righe)

# ordino ogni colonna
ordinata_colonne = np.sort(invertita, axis=0)
print("\nColonne ordinate:\n", ordinata_colonne)

# trasposta della matrice invertita (extra concettuale)
trasposta = invertita.T
print("\nTrasposta della matrice invertita:\n", trasposta)

# reshape in 2x8 (solo se compatibile)
reshape_2x8 = invertita.reshape(2, 8)
print("\nReshape 2x8:\n", reshape_2x8)