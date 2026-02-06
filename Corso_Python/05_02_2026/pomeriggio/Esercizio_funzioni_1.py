# Pomeriggio 05/02/2026
# slide pagina 97

"""
1. Esercizio Base: Indovina il numero
Descrizione: Scrivi un programma che genera un numero casuale
tra 1 e 100 (inclusi). L'utente deve indovinare quale numero è
stato generato. Dopo ogni tentativo, il programma dovrebbe
dire all'utente se il numero da indovinare è più alto o più
basso rispetto al numero inserito. Il gioco termina quando
l'utente indovina il numero o decide di uscire.

EXTRA: creare una funzione che converte da input a lista e una per convertire da lista a tupla e viceversa
[TBD]
"""

import random

def indovina_numero(x):
    indovinato = False
    uscita = False
    tentativi = 0
    
    while not indovinato:
        print("\nTentativo n.", tentativi+1)
        tentativi += 1
        
        num = int(input("\nProva ad indovinare: "))
        if num < x:
            print("\nIl numero da indovinare è più grande")
        elif num > x:
            print("\nIl numero da indovinare è piu piccolo")
        else:
            indovinato = True
            break
            
        riprova = input(("\nRitenti? (y/n) "))
        if riprova == "n":
            uscita = True
            break
        elif riprova == "y":
            continue
        else:
            print("Comando sbagliato. Uscita")
            uscita = True
            break
        
    return indovinato, tentativi, uscita                  # ritorna una tupla con (indovinato, tentativi, uscita)

print("\n********** Gioco - indovina il numero **********")

numero = random.randint(1, 100)
vinto, tentativi, uscita = indovina_numero(numero)           # unpacking della tupla

if uscita == True:
    print("\nGioco terminato da utente o comando sbagliato")
elif not vinto:
    print("\nHai perso")
    print("\nNumero tentativi:", tentativi)
else:
    print("\nHai vinto!")
    print("\nNumero tentativi:", tentativi)
