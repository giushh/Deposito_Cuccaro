# mattina 24/02/2026

"""
Crea uno script Python che esegua i seguenti passaggi:
    1.Crea un array NumPy (ndarray) utilizzando np.arange con valori da 0 a 49
    più altre 50 posizioni casuali tra 49 e 101.
    Stampa l’array, il suo dtype e la sua shape.
    
    2.Modifica il tipo di dato (dtype) dell’array in float64.
    Verifica e stampa di nuovo dtype e shape.
    
    3.Utilizza lo slicing per ottenere:
    i primi 10 elementi
    gli ultimi 7 elementi
    gli elementi dall’indice 5 all’indice 20 escluso
    ogni quarto elemento dell'array
    
    4.Modifica tramite slicing gli elementi dall’indice 10 a 15 (escluso
    assegnando loro il valore 999.
    
    5.Utilizza la fancy indexing per selezionare:
    gli elementi in posizione [0, 3, 7, 12, 25, 33, 48]
    tutti gli elementi pari dell’array utilizzando una maschera booleana
    tutti gli elementi maggiori della media dell'array
    
    6.Stampa:
    l’array originale dopo tutte le modifiche
    tutti i sotto-array ottenuti tramite slicing e fancy indexin
""" 

import numpy as np 
from termcolor import colored as c

# 1 
arr1 = np.arange(50)
arr2 = np.random.randint(49, 101, 50)

arr = np.concatenate((arr1, arr2))

print(c("\n***** Punto 1 - Creazione array *****", "green"))
print("Array creato:",arr)
print("Tipo:", arr.dtype)
print("Shape:", arr.shape)

# 2
arr_cambio_tipo = arr.copy()
arr_cambio_tipo.dtype = 'float64'

print(c("\n***** Punto 2 - Modifica tipo *****", "green"))
print("Tipo:", arr_cambio_tipo.dtype)
print("Shape:", arr_cambio_tipo.shape)

# 3
print(c("\n***** Punto 3 - Slicing *****", "green"))
print("Array:",arr)
print("Primi 10 elementi:",arr[:10])
print("Ultimi 7 elementi:", arr[-7:])
print("Dall'indice 5 a 20, escluso ogni quarto elemento", arr[5:20:4])

# 4 
print(c("\n***** Punto 4 - Modifica elementi, assegno 999 agli elementi dall'indice 10 a 15 escluso *****", "green"))
print("Prima:", arr)
arr[10:15] = 99
print("Dopo:", arr)

# 5 
print(c("\n***** Punto 5 - Fancy Indexing *****", "green"))
print("Array:", arr)

posizioni = [0, 3, 7, 12, 25, 33, 48]

pari = arr[arr % 2 == 0]
media = arr.mean()
maggiori_media = arr[arr > media]

print("Posizioni specifiche selezionate:", posizioni)
print(arr[posizioni])
print("Elementi pari:", pari)
print("Elementi maggiori della media:", media)
print(maggiori_media)
