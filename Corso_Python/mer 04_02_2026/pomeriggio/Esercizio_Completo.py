# Pomeriggio del 04/02/2026 

# Esercizio completo 
print("********** Esercizio completo **********")

print("----- Punto 1 -----")
# scrivi un sistema che controlli un num in input se è pari/dispari
num = int(input("Dimmi un numero, ti dirò se è pari o dispari: "))

if num % 2 == 0:
    print("Il numero ", num, " è pari")
else:
    print("Il numero ", num, " è dispari")


print("----- Punto 2 -----")
# prendi in input un numero intero positivo e stampa tutti i numeri da n a 0 (compreso) decrementando di passo 1
# deve ripetersi all'infinito

num2 = int(input("Dimmi un numero positivo, facciamo un conto alla rovescia: "))
exit = True

if num2 > 0:
    while exit:
        iteraz = num2
        for numero in range(iteraz + 1):
            print(iteraz)
            iteraz -= 1

        risposta = input("Vuoi fare un altro conto alla rovescia? (y/n) ")
        if risposta == "n":
            exit = False
else:
    print("Il numero non è valido")


print("----- Punto 3 -----")
# prendi in input una lista di numeri e stampa il quadrato di ogni elemento della lista

print("Facciamo una lista di numeri")
stop = False
lista = []

while not stop:
    ans = int(input("Che numero vuoi aggiungere? "))
    lista.append(ans)

    ans2 = input("Vuoi fermarti? (y/n) ")
    if ans2 == "y":
        stop = True

print("Stampo i quadrati dei numeri presenti nella lista ")
for n in lista:
    print(n * n)


print("----- Punto 4 -----")
# usa if, while e for insieme
# 1) trova massimo con for
# 2) conta elementi con while
# 3) se lista vuota stampa "Lista Vuota", altrimenti stampa massimo e numero di elementi

if len(lista) == 0:
    print("Lista Vuota")
else:
    massimo = lista[0]
    for n in lista:
        if n > massimo:
            massimo = n

    conteggio = 0
    i = 0
    while i < len(lista):
        conteggio += 1
        i += 1

    print("Il numero massimo trovato è:", massimo)
    print("Il numero di elementi nella lista è:", conteggio)
