# Mattina del 05/02/2026

"""
Esercizio Completo

Descrizione: Scrivi un programma che chieda all'utente di inserire un numero intero positivo n. 
Il programma deve poi eseguire le seguenti operazioni:

1. Utilizzare un ciclo while per garantire che l'utente inserisca un numero positivo. 
    Se l'utente inserisce un numero negativo o zero, il programma deve continuare a chiedere un numero 
    fino a quando non viene inserito un numero positivo.
2. Utilizzare un ciclo for con range per calcolare e stampare la somma dei numeri pari da 1 a n.
3. Utilizzare un ciclo for per stampare tutti i numeri dispari da 1 a n.
4. Utilizzare una struttura if per determinare se n è un numero primo. 
    Un numero primo è divisibile solo per 1 e per se stesso. 
    Il programma deve stampare se n è primo o no.
"""

print("\n********** Esercizio completo ***********")

stop = False
tentativi = []
while not stop:
    n = int(input("\nInserisci un numero intero positivo: "))
    
    if n < 0 or n == 0:                                             # punto 1
        print("Non mi piace questo numero, riprova.")
        tentativi.append(n)
        # DEBUG 
        print(tentativi)
        continue
    
    primo = True                                                    # punto 4
    if n <= 1:
        primo = False
    else:
        i = 2
        while i * i <= n:
            if n % i == 0:
                primo = False
                break
            i += 1
    if primo:
        print("\nIl numero",n,"è primo")
    else:
        print("\nIl numero",n,"non è primo")
    
    numeri = [*range(1, n+1, 1)]                                      # calcolo pari e dispari
    pari = []
    dispari = []
    somma = 0
    
    for num in numeri:
        if num % 2 == 0:
            somma += num
            pari.append(num)
        else:
            dispari.append(num)                 
    
    print("\nLa lista dei numeri è:", numeri)                       
    print("\nLa somma dei numeri pari è", somma)                    # punto 2
    
    print("\nI numeri dispari della lista sono:")                   # punto 3
    for num in dispari:
        print(num)
        
    # EXTRA: andare a creare una lista che salva tutti i tentativi e un ultima sezione del programma che permetta di visionare o modificare la lsita
    
    scelta = input("\nVuoi vedere la lista dei tentativi? (y/n) ")      
    if scelta == "y":
        
        print("\nEccola:", tentativi)
        sub_scelta = input("\nVuoi modificare la lista? (y/n) ")
        if sub_scelta == "y":
             
            print("Puoi:")
            print("1 - Aggiungi; 2 - Rimuovi; 3 - Elimina la lista")

            do = input("Cosa vuoi fare? ")

            if do == "1":
                
                elem = int(input("Cosa vuoi aggiungere (alla fine)? "))
                tentativi.append(elem)
                print("Lista aggiornata: ", tentativi)
                
            elif do == "2":
                
                print("Cosa vuoi rimuovere da ", tentativi)
                elem = int(input())
                if (elem in tentativi):
                    tentativi.remove(elem)
                    print("Lista aggiornata: ", tentativi)
                else:
                    print("Elemento non presente.")
            
            elif do == "3":
                
                tentativi.clear()
                print("Lista eliminata")
                
            else:
                print("Comando non valido") 
            
        elif sub_scelta == "n":
            print("Lista dei tentativi non modificata")
        else:
            "Scelta non valida"
            
    else:
        print("Scelta non valida, skip")
    
    scelta2 = input("Vuoi uscire? (y/n) [se non esci, ricominciamo] ")          
    if scelta2 == "n":
        continue                # spezza l'iterazione corrente e ricomincia
    elif scelta2 == "y":
        stop = True             # esce dal ciclo while
    else: 
        print("Scelta non valida. Uscita")
        stop = True             # esce dal ciclo while
    
print("\n********** Fine **********")
    
