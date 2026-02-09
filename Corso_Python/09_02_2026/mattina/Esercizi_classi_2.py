# Esercizio 2 - Facile

"""
Crea una classe chiamata Libro. Questa classe dovrebbe avere:
Tre attributi: titolo, autore e pagine.
Un metodo descrizione che restituisca una stringa del tipo "Il libro 'titolo' è stato scritto da 'autore' e ha 'pagine' pagine.".

Rendilo ripetibile , cioè chiedere se continuare a inserire libri

"""

class Libro:
    
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
    
    def descrizione(self):
        descrizione = f"Il libro {self.titolo} è stato scritto da {self.autore} e ha {self.pagine} pagine."
        return descrizione
        

print("********** Libri **********")

stop = False
while not stop:
    
    scelta = input("\nVuoi:"
                   "\n1. Inserire nuovo libro"
                   "\n2. Avere descrizione libro corrente"
                   "\n3. Uscire"
                   "\nInserisci 1/2/3 ")
    
    match scelta:
        case "1":
            print("\n-- Inserimento libro")
            titolo = input("Titolo: ")
            autore = input("Autore: ")
            pagine = input("Numero di pagine: ")
            
            libro = Libro(titolo, autore, pagine)
            print("Libro inserito")
            
        case "2":
            print(libro.descrizione())
            
        case "3":
            print("\n-- Uscita")
            stop = True
        case _: 
            print("Comando non valido. \n--Uscita")
            stop = True
