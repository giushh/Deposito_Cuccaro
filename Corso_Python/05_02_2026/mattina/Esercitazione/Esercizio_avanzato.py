# Mattina del 05/02/2026
# esercizio pagina 85 dalle slide
"""
 Scrivi un programma che:
 1. Chiede all'utente di inserire due numeri.
 2. Calcola e stampa i fattori comuni dei due numeri.
 3. Se lunico fattore comune è 1, stampa il messaggio: "I numeri sono coprimi".
 4. Ripeti lo stesso concetto con due stringhe:
 - verifica se hanno tutte le lettere in comune (es. "abs" e "sab"),
 - in questo caso le stringhe sono definite "complementari".
 5. Al termine, chiede all'utente se vuole ripetere l'operazione.
"""

print("********** Esercizio base **********")
print("Numeri coprimi")


while True:
    num1 = int(input("Dimmi un numero"))
    num2 = int(input("Dimmi un altro numero"))
    
    fattori = []
    # Determina il numero più piccolo tra i due
    minore = min(num1, num2)
    
    # Controlla divisibilità da 1 al numero minore
    for i in range(1, minore + 1):
        if num1 % i == 0 and num2 % i == 0:
            fattori.append(i)
    
    if len(fattori) == 1:
        if fattori[0] == 1:
            print("I numeri sono coprimi")
    
    

    scelta2 = input("Vuoi uscire? (y/n) [se non esci, ricominciamo]")          # se non esce, ricomuncia il ciclo
    if scelta2 == "n":
        continue                # spezza l'iterazione corrente e ricomincia
    elif scelta2 == "y":
        print("Addio")
        break                   # esce dal ciclo while
    else: 
        print("Scelta non valida. Uscita")
        break                   # esce dal ciclo while    