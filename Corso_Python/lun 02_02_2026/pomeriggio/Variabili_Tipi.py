# Pomeriggio del 02/02/2026 - esempi di variabili e tipi

# Assegnazione diretta
nome = "Ilaria"
anno = 2026

# Leggere input da utente
nome = input("Come ti chiami? ")            # prende in input i caratteri immessi, di tipo stringa 
anno = int(input("In che anno siamo? "))    # conversione esplicita al tipo intero
print(nome, "siamo nell'anno", anno)        # stampo 

# Operazioni matematiche 
op1 = int(input("Dimmi un numero: "))                           # prende in input due numeri
op2 = int(input("Dimmi un altro numero (diverso da zero): "))
print("Hai inserito i numeri ", op1," e ", op2)                 # mostra a video i numeri scelti
# stampa le operazioni principali con i numeri scelti
print("Addizione: ", op1+op2," - Sottrazione: ", op1-op2," - Moltiplicazione: ", op1*op2," - Divizione: ", op1/op2," - Potenza: ", op1**op2)

# Interi vs Float
intero = 10
non_intero = 2.3
risultato  = intero - non_intero        # il risultato sarà ti tipo float 
print(intero, " + ", non_intero, " = ", risultato) 

# Stringhe
lettera = input("Dimmi una lettera: ")
messaggio = "Hai scelto una la lettera " + lettera      # concatenazione di due stringhe
print(messaggio)

stringa = "Mi piace fare i puzzle"
print("Stringa: ")
print("La lunghezza della stringa è: ", len(stringa))       # stampa lunghezza della stringa
print("Versione tutto in maiuscolo: ", stringa.upper())     # stampa la stringa in maiuscolo
print("Versione tutto in minuscolo: ", stringa.lower())     # stampa la stringa in minuscolo
print("Divisione della stringa: ", stringa.split(' '))      # quando incontra il carattere spazio divide la stringa in singole parole in una lista
print("Sostituzione: ", stringa.replace('puzzle','dolci'))  # sostituisce la parola "puzzle" con la parola "dolci"

# Char
carattere = 'a'     # singolo carattere
print("Questa è una variabile di tipo char: ", carattere)

# Boolean
booleanVero = True      # variabile booleana
booleanFalso = False 
print(int(booleanVero), int(booleanFalso))      # il valore numerico di True è 1, il valore numerico di False è 0
print( 5 > 10 )                                 # stampa False
print( 3 == 3 )                                 # confronta se quei due valori sono uguali, in questo caso True
x = 4
y = "4"
print( x == y )                                 # stampa False perché non sono dello stesso tipo, viene controllato sempre prima il tipo
print( x != y )                                 # confronta se sono diversi, in questo caso True 