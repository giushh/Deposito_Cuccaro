# test venerdi 06/02/2026


"""
Esercizio 2
    Definisca una funzione chiamata conta_vocali. 
     
     La funzione deve: 
         
         ricevere una stringa come parametro 
         
         contare quante vocali contiene (a, e, i, o, u) 
         
         restituire il numero totale di vocali 
          
     
     Nel programma principale: 
         
         chiedi all’utente di inserire una parola 
         
         chiama la funzione 
         
         stampa il numero di vocali trovate
"""

def conta_vocali(stringa):
    """
    riceve una stringa come parametro 
         
    conta quante vocali contiene (a, e, i, o, u) 
         
    restituisce il numero totale di vocali
    """
    vocali = []
    
    for lettera in stringa:
        if lettera == "a" or lettera == "e" or lettera == "i" or lettera == "o" or lettera == "u":
            vocali.append(lettera)
    
    return len(vocali)

print("\n********** Esercizio 2 ***********")

parola = input("\nDimmi una parola: ")

num_vocali = conta_vocali(parola)

print("\nLa tua parola contiene",num_vocali,"vocali")