# pomeriggio 16/02/2026

"""
Scrivete un programma che chiede una stringa all’utente e
restituisce un dizionario rappresentante la "frequenza di
comparsa" di ciascun carattere componente la stringa.
Esempio:
Stringa "ababcc",
Risultato
{"a": 2, "b": 2, "c": 2}
"""

testo = input("Inserisci una stringa: ")

frequenze = {}   # dizionario vuoto

for carattere in testo:
    
    if carattere in frequenze:
        frequenze[carattere] += 1
    else:
        frequenze[carattere] = 1

print("\nRisultato:")
for carattere, conteggio in frequenze.items():
    print(f"'{carattere}' : {conteggio}")

