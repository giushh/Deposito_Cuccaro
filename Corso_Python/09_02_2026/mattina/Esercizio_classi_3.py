# Esercizio 3 - 

"""
Crea una classe biblioteca che permetta di creare un libro e stamparlo

EXTRA: permetti di inserire quanti libri vuole l'utente nella biblioteca

"""
# prende la classe già creata nell'esercizio precedente

class Libro:
    
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
    
    def descrizione(self):
        descrizione = f"Il libro {self.titolo} è stato scritto da {self.autore} e ha {self.pagine} pagine."
        return descrizione
       

class Biblioteca:
    def __init__(self):
        self.num_libri = 0
        self.libri = []

    def libri_presenti(self):
        for elem in self.libri:
            yield elem

    def mostra_num_libri(self):
        print(f"Sono presenti {self.num_libri} libri")

# main
print("********** Biblioteca **********")

stop = False
biblioteca = Biblioteca()

while not stop:
    
    scelta = input("\nVuoi:"
                   "\n1. Inserire nuovo libro"
                   "\n2. Lista libri presenti in biblioteca"
                   "\n3. Uscire"
                   "\nInserisci 1/2/3 ")
    
    match scelta:
        case "1":
            print("\n-- Inserimento libro")
            titolo = input("Titolo: ")
            autore = input("Autore: ")
            pagine = input("Numero di pagine: ")
            
            libro = Libro(titolo, autore, pagine)
            
            biblioteca.num_libri += 1
            biblioteca.libri.append(libro)
            
            print("Libro inserito")
            
        case "2":
            if biblioteca.num_libri == 0:
                print("\nNon ci sono libri in biblioteca")
            else:
                print("\n-- Libri presenti")
                num = 1
                for libro in biblioteca.libri_presenti():
                    print(num, ". ", libro.descrizione())
                    num += 1
                
                """
                Il for chiede il primo valore al generator
                Il generator entra nel metodo e arriva al primo yield elem
                elem viene assegnato a libro
                Stampi la descrizione
                Il for chiede il valore successivo
                Il generator riprende da dove si era fermato
                Continua finché la lista finisce
                """
                
        case "3":
            print("\n-- Uscita")
            stop = True
        case _: 
            print("Comando non valido. \n--Uscita")
            stop = True