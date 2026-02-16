# mattina 16/02/2026

"""
create un programma che richiede all’utente tre numeri 
e verifica la presenza di almeno due numeri uguali, 
se non ci sono ci restituisce il numero più grande dei tre
"""

lista = []

print("Dimmi 3 numeri interi")

num1 = int(input("Primo: "))
lista.append(num1)

num2 = int(input("Secondo: "))
lista.append(num2)

num3 = int(input("Terzo: "))
lista.append(num3)

print("I numeri inseriti sono: ", lista)

if num1 == num2 or num2 == num3 or num1 == num3:
    print("Ci sono 2 numeri uguali")
else:
    indice = 0
    for num in lista:
        if num > lista[indice]:
            maggiore = num
            indice += 1

    print(f"Non ho trovato numeri uguali. Il maggiore è {maggiore}")
    
    
"""
per renderlo ripetibile e riutilizzabile si può utilizzare un while con una variabile che indicasse il numero dei numeri da inserire
"""