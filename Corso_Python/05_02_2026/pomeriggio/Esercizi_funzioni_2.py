# Pomeriggio 05/02/2026
# slide pagina 97

"""
2. Esercizio Avanzato: Sequenza di Fibonacci fino a N
Descrizione: Chiedi all'utente di inserire un numero N. Il
programma dovrebbe stampare la sequenza di Fibonacci fino a N.
Ad esempio, se l'utente inserisce 100, il programma dovrebbe
stampare tutti i numeri della sequenza di Fibonacci minori o
uguali a 100.

ps. la sequenza di Fibonacci è una sequenza di numeri in cui i primi due numeri sono 0 e 1
e ogni numero successivo è la somma dei due precedenti
(esempio: 0, 1, 1, 2, 3, 5, 8, 13, ...)
"""

def fibonacci(n):
    """
    Stampa la sequenza di Fibonacci fino all'ultimo numero prima di n"""
    
    a = 0                # inizializziamo i primi due numeri della sequenza
    b = 1

    while a <= n:
        print(a)         # stampa il numero corrente della sequenza
        c = a + b        # calcola il numero successivo
        a = b            # aggiorna il primo valore
        b = c            # aggiorna il secondo valore

print("\n********** Sequenza di Fibonacci **********")

n = int(input("Limite superiore della sequenza? "))

fibonacci(n)

print("Fatto, addio")