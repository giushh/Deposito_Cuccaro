# test venerdi 06/02/2026

"""
Esercizio 1

1. Chieda all’utente di inserire un numero intero positivo. 
     
2. Usi un ciclo for per stampare tutti i numeri da 1 fino al numero inserito. 
     
3. Per ogni numero: 
         
    stampi "pari" se il numero è pari 
         
    stampi "dispari" se il numero è dispari 
          
     
4. Se l’utente inserisce un numero minore o uguale a zero, il programma deve stampare un messaggio di errore.
"""

print("\n********** Esercizio 1 ***********")

def is_pari(x):
    """
    Calcola se x è un numero pari
    """
    pari = False
    if x % 2 == 0:
        pari = True
    return pari

num = int(input("\nDimmi un numero intero positivo: "))

if num <= 0:
    print("[Errore] - Il numero inserito non è intero positivo")
else:
    lista = [*range(1, num+1,1)]
    print("\nStampo i numeri da 1 fino a", num)
    for n in lista:
        print(n)
        if is_pari(n):
            print("che è pari")
        else:
            print("che è dispari")
