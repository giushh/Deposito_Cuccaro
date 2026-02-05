# Mattina del 05/02/2026
# esercizio pagina 85 dalle slide

"""
 1.Base / Numeri pari e dispari o sequenza Descrizione:
 Scrivi un programma che chiede all'utente di inserire un numero o una stringa scegliendo prima quale.
 Il programma dovrebbe determinare se il numero è pari o dispari e stampare il risultato e se deve ripetere o stampare e poi ripetere.
 """

print("********** Esercizio base **********")
print("Numeri pari/dispari/sequenza")

stop = False

while not stop:
    scelta = input("Vuoi inserire un numero o una stringa? (n/s)")
    if scelta == "n":
        while True: 
            num = int(input("Hai scelto il numero. Quale? "))
            if num % 2 == 0:
                print("Il numero ", num, "è pari")
            else:
                print("Il numero ", num, "è dispari")
            
            sub_scelta1 = input("Vuoi mettere un altro numero o tornare alla scelta iniziale? ( n - numero; s - scelta)")
            if sub_scelta1 == "n":
                continue
            elif sub_scelta1 =="s":
                break
            else:
                print("Scelta non valida.")
                break
            
    elif scelta == "s":
        while True: 
            stringa = input("Hai scelto la stringa. Quale? ")
            if len(stringa) % 2 == 0:
                print("La stringa",stringa," ha una lunghezza di", len(stringa), "che è pari")
            else:
                print("La stringa",stringa," ha una lunghezza di", len(stringa), "che è dispari")
            
            sub_scelta1 = input("Vuoi mettere un'altra stringa o tornare alla scelta iniziale? ( str - stringa ; s - scelta)")
            if sub_scelta1 == "str":
                continue
            elif sub_scelta1 =="s":
                break
            else:
                print("Scelta non valida.")
                break
    else:
        print("Scelta non valida. Uscita")
        break
    
    scelta2 = input("Vuoi uscire? (y/n) ")
    if scelta2 == "n":
        continue                # spezza l'iterazione corrente e ricomincia
    elif scelta2 == "y":
        stop = True             # esce dal ciclo while
    else: 
        print("Scelta non valida. Uscita")
        stop = True             # esce dal ciclo while





