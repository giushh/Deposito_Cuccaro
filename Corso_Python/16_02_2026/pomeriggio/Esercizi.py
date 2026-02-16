# pomeriggio 16/02/2026

"""
Scrivete un programma che chiede all'utente una serie di parole 
e restituisce solo le vocali e l’indice della vocale all’interno delle parole.
"""

vocali = ["a", "e", "i", "o", "u"]

parole = []

print("Inserisci delle parole (scrivi 'stop' per terminare):")

stop = False
while not stop:
    parola = input("--> ")
    
    if parola == "stop":
        break
    
    parole.append(parola)


for elem in parole:
    print(f"\nParola: {elem}")
    
    for indice, lettera in enumerate(elem):
        if lettera.lower() in vocali:
            print(f"Vocale: {lettera} - Indice: {indice}")