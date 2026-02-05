# Pomeriggio del 04/02/2026

# 1 - chiedi all'utente un numero. il programma fa un conto alla rovescia da quel numero fino a zero, stampando ogni numero e chiederti se vuoi ricominciare
print("********** Esercizio 1 **********")

print("Conto alla rovescia")

continua = True

while continua:
    iteraz = int(input("Da che numero partiamo? "))
    for numero in range((iteraz+1)):
        print(iteraz)
        iteraz -= 1
    risposta = input("Vuoi fare un altro conto alla rovescia? (y/n) ")
    if risposta == "n":
        continua = False


# 2 - chiedi all'utente un numero. controlla se è primo / pari o no. si ferma quando ha 5 numeri primi
print("********** Esercizio 2 **********")

print("Controlliamo 5 numeri primi")
count = 0
while count < 5: 
    num = int(input("Dimmi un numero "))
    
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
        count += 1
    
    if num % 2 == 0:
        pari = True
    else:
        pari = False
        
    print("Il numero scelto ", num, " è: ")
    print("Primo: ", primo)
    print("Pari: ", pari)
    
    print("Numeri primi trovati: ", count)
    


