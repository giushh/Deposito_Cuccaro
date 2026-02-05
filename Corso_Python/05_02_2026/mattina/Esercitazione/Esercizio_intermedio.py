# Mattina del 05/02/2026
# esercizio pagina 85 dalle slide

"""
 2.Intermedio/ Numeri primi in un intervallo :
 Chiedi all'utente di inserire due numeri che definiscono un intervallo (es 10 e 50).
 Il programma dovrebbe stampare tutti i numeri primi compresi in quell'intervallo o i numeri non primi o entrambi divisi a tua scelta, 
 salvandoli in due aggregazioni differenti e chiedere se deve ripetere
 """

print("********** Esercizio intermedio **********")
print("Numeri primi in un intervallo")

while True:
    start = int(input("Dimmi l'inizio dell'intervallo: "))
    stop = int(input("Dimmi la fine dell'intervallo: "))
    lista = [*range(start, stop+1, 1)]
    
    print("\nLista con i numeri dell'intervallo scelto: ", lista)
    lista_primi = []
    lista_non_primi = []
    
    count_primi = 0
    count_non_primi = 0
    
    for num in lista:
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
        if primo:
            count_primi += 1
            lista_primi.append(num)
        else: 
            count_non_primi += 1
            lista_non_primi.append(num)
            
    print("\nNumeri primi trovati",count_primi, lista_primi)
    print("\nNumeri non primi trovati ",count_non_primi, lista_non_primi)

    scelta2 = input("Vuoi uscire? (y/n) ")
    if scelta2 == "n":
        continue                # spezza l'iterazione corrente e ricomincia
    elif scelta2 == "y":
        print("Addio")
        break                   # esce dal ciclo while
    else: 
        print("Scelta non valida. Uscita")
        break                   # esce dal ciclo while    