# Mattina del 04/02/2026

# Controllo del flusso - gestione delle istruzioni da eseguire in base ad elementi confizionali
# 3 tipi: CONDIZIONI - CICLI - FUNZIONI

# Condizione - controllo del flusso che decide se eseguire un blocco di codice
# Ciclo - controllo del flusso che decide quante volte eseguire un blocco di codice
# Funzione - TBD

numero = int(input("Scrivi un numero positivo o negativo: "))
if numero > 0:                                       # va bene anche con parentesi if (numero > 0)
    print("Il numero è positivo")
    if numero > 99:                                  # if annidato
        print("Il numero ha tre cifre") 
elif numero < 0:                                     # torna su livello 0 di indentazione, i blocchi interni salgono al livello 1 
    print("Il numero è negativo")
else:                                                # blocco eseguito solo se le due condizioni precedenti non sono verificate
    print("Il numero è zero")


capitale = "roma"
risposta = input("Qual è la capitale dell'Italia? ")
if risposta.lower() == capitale:
    print("Risposta esatta")
else:
    print("Risposta sbagliata")