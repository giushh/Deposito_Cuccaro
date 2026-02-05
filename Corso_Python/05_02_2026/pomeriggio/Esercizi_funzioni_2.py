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
    Stampa la sequenza di Fibonacci fino al numero inferiore a n"""
    
    a = 0                 # Inizializziamo i primi due numeri della sequenza
    b = 1

    while a <= n:
        print(a)      # Stampa il numero corrente della sequenza
        c = a + b     # Calcola il numero successivo
        a = b         # Aggiorna il primo valore
        b = c         # Aggiorna il secondo valore

print("\n********** Sequenza di Fibonacci **********")

n = int(input("Quanti numeri della sequenza di Fibonacci vuoi stampare? "))

fibonacci(n)

print("Fatto, addio")