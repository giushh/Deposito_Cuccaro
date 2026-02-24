# mattina 
import numpy as np

# funzione linspace
# genera un array con valori equidistanti tra un val iniziale e uno finale

arr = np.linspace(0, 1, 5) # tra 0 e 1 compreso, dammi 5 valori equidistanti
print(arr) # Output: [0. 0.25 0.5 0.75 1. ]


# funzione random 
# genera numeri casuali

random_arr = np.random.rand(3, 3)
# Matrice 3x3 con valori casuali uniformi tra 0 e 1
print(random_arr)

# funzioni universali - si applicato a tutti gli elementi contemporaneamente
# non modificano l'array, ne ricavano solo informazioni 

arr = np.array([1, 2, 3, 4, 5])

sum_value = np.sum(arr)
mean_value = np.mean(arr)
std_value = np.std(arr)

print("Sum:", sum_value) # Output: Sum: 15
print("Mean:", mean_value) # Output: Mean: 3.0
print("Standard Deviation:", std_value)
# Output: Standard Deviation: 1.4142135623730951



# Inversa di una Matrice

# Creazione di una matrice quadrata
A = np.array([[1, 2], [3, 4]])

# Calcolo dell'inversa della matrice
A_inv = np.linalg.inv(A)
print("Inversa di A:\n", A_inv)

# Norma di un Vettore

# Creazione di un vettore
v = np.array([3, 4])

# Calcolo della norma del vettore
norm_v = np.linalg.norm(v)
print("Norma di v:", norm_v)
# Output: 5.0


"""numpy.linalg.solve
Questa funzione viene utilizzata per risolvere un sistema lineare
di equazioni della forma Ax=BAx = BAx=B, dove AAA è una matrice
quadrata e BBB è un vettore o una matrice."""

# Creazione della matrice A e del vettore B
A = np.array([[3, 1], [1, 2]])
B = np.array([9, 8])

# Risoluzione del sistema di equazioni Ax = B
x = np.linalg.solve(A, B)
print("Soluzione x:", x) # Output: [2. 3.]


"""numpy.fft.fft
Questa funzione calcola la Trasformata di Fourier Discreta (DFT) di
un array. La DFT è uno strumento potente per analizzare le frequenze
dei segnali.
"""
# Creazione di un segnale
t = np.linspace(0, 1, 400)
sig = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 120 * t)

# Calcolo della Trasformata di Fourier
fft_sig = np.fft.fft(sig)

# Frequenze associate
freqs = np.fft.fftfreq(len(fft_sig))

print("Trasformata di Fourier:", fft_sig)
print("Frequenze associate:", freqs)


"""In questo esempio, lo scalare 10 viene broadcasted per avere la stessa
dimensione dell'array arr."""

arr = np.array([1, 2, 3, 4])
scalar = 10

# Broadcasting aggiunge lo scalare a ogni elemento dell'array
result = arr + scalar
print(result) # Output: [11 12 13 14]
