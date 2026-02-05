# Pomeriggio del 05/02/2026
"""
1. Chiedi all'utente di inserire un numero intero positivo n. 
Se l'utente inserisce un numero negativo o zero, continua a chiedere un numero fino a quando non viene inserito un numero positivo.
2. Genera una lista di numeri interi tra 1 e n (incluso). La lunghezza della lista deve essere n.
3. Utilizza un ciclo for per calcolare e stampare la somma dei numeri pari nella lista.
4. Utilizza un ciclo for per stampare tutti i numeri dispari nella lista.
5. Determina se un numero è primo (senza funzioni).
6. Utilizza un ciclo for per stampare tutti i numeri primi nella lista.
7. Infine, utilizza una struttura if per determinare se la somma dei numeri primi è un numero primo e stampa il risultato
"""

# DISCLAIMER: il codice poteva essere più efficiente con l'aggiunta di una funzione is_primo() 
# a scopo didattico, non è stata aggiunta

print("\n********** Esercizio completo 2***********")

stop = False                                                        # variabile per terminare il ciclo principale
while not stop:
    n = int(input("\nInserisci un numero intero positivo: "))       # PUNTO 1
    
    if n <= 0 or n == 0:                                            # continuerà a chiedere un numero finchè non è positivo e diverso da zero
        print("\nNon mi piace questo numero, riprova.")             # dato che n è di tipo intero, se viene inserito un float va in errore 
        continue
    
    numeri = [*range(1, n+1, 1)]                                    # PUNTO 2
    pari = []
    dispari = []
    primi = []
    somma_pari = 0
    somma_primi = 0
    
    
    for num in numeri:                                              # divisione in numeri pari e dispari in due liste separate
        if num % 2 == 0:
            somma_pari += num
            pari.append(num)
        else:
            dispari.append(num)                 
    
    print("\nLa lista dei numeri è:", numeri)                       # PUNTO 3                       
    print("\nLa somma dei numeri pari è", somma_pari)                    
    
    print("\nI numeri dispari della lista sono:")                   # PUNTO 4
    for num in dispari:
        print(num)
    
    print("\nLa lista di numeri ottenuta ha i seguenti numeri primi:")  # controllo numeri primi nella lista
    for num in numeri:
        primo = True
        if num <= 1:
            primo = False
        else:
            i = 2
            while i * i <= num:
                if num % i == 0:
                    primo = False
                    break
                i += 1
        
        if primo:                                                       # PUNTO 5 e 6
            primi.append(num)                                           # salvataggio in una lista separata
            print(num)
    
    
    for num in primi:                                                   # calcolo somma dei numeri primi
        somma_primi += num
    
    
    primo = True                                                        # PUNTO 7
    if somma_primi <= 1:
        primo = False
    else:
        i = 2
        while i * i <= somma_primi:
            if somma_primi % i == 0:
                primo = False
                break
            i += 1
    
    if primo:
        print("\nLa somma dei numeri primi della lista è", somma_primi, "ed è un numero primo")
    else:
        print("\nLa somma dei numeri primi della lista è", somma_primi, "e non è un numero primo")

    
    scelta2 = input("\nVuoi ricominciare? (y/n)")          
    if scelta2 == "y":
        continue
    elif scelta2 == "n":
        stop = True
    else: 
        print("Scelta non valida. Uscita")
        stop = True
    
print("\n********** Fine **********")
