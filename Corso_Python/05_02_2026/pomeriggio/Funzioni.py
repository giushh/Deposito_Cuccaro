# Pomeriggio 05/02/2026

def saluta(nome):
    print("Ciao ",nome,"!")
    
def crea_lista_sequenziale(lunghezza):
    """
    Crea e ritorna una lista di numeri sequenziali da 1 a lunghezza, di passo 1
    """
    lista = [*range(1, lunghezza+1, 1)]
    return lista
    
def stampa_lista_singola(lista:list):
    """
    Stampa gli elementi singolarmente gli elementi in una lista"""
    for elem in lista:
        print(elem)
    
def is_primo(x):
    """
    Restituisce True se x è un numero primo
    """
    primo = True
    if x <= 1:
        primo = False
    else:
        i = 2
        while i * i <= x:
            if x % i == 0:
                primo = False
                break
            i += 1
    return primo
    
saluta("Ilaria")
numeri = crea_lista_sequenziale(10)
stampa_lista_singola(numeri)

num = int(input("Dimmi un numero:"))
if is_primo(num):
    print("Il numero", num, "è primo")
else:
    print("Il numero", num, "non è primo")
