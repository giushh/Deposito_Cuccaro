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
    num1 = int(input("\nDimmi un numero "))
    num2 = int(input("\nDimmi un altro numero "))
    
    fattori = []
    
    minore = min(num1, num2)                            # determina il numero più piccolo tra i due
    
    for i in range(1, minore + 1):                      # controlla divisibilità da 1 al numero minore
        if num1 % i == 0 and num2 % i == 0:
            fattori.append(i)
    
    if len(fattori) == 1:
        if fattori[0] == 1:
            print("\nI numeri sono coprimi")
    else:
        print("I numeri non sono coprimi, hanno in comune", fattori)
    
    str1 = input("\nInserisci la prima stringa: ").lower()
    str2 = input("\nInserisci la seconda stringa: ").lower()

    lettere1 = []                                           # lista delle lettere della prima stringa
    for c in str1:
        if c not in lettere1:
            lettere1.append(c)

    lettere2 = []                                           # lista delle lettere della seconda stringa
    for c in str2:
        if c not in lettere2:
            lettere2.append(c)
            
    comuni = []

    for c in lettere1:
        if c in lettere2:
            comuni.append(c)                                # controllo lettere comuni

    if len(comuni) == len(lettere1) and len(comuni) == len(lettere2):
        print("\nLe stringhe sono complementari")
    else:
        print("\nLe stringhe non sono complementari")

    
    scelta2 = input("\nVuoi uscire? (y/n) [se non esci, ricominciamo]")          # se non esce, ricomuncia il ciclo
    if scelta2 == "n":
        continue                # spezza l'iterazione corrente e ricomincia
    elif scelta2 == "y":
        print("\nAddio")
        break                   # esce dal ciclo while
    else: 
        print("\nScelta non valida. Uscita")
        break                   # esce dal ciclo while    