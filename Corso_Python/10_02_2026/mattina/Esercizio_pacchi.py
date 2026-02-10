# mattina 10/02/2026

"""
Il sistema deve includere una classe Pacco con: codice (stringa), peso (numero) e stato (es. "in magazzino", "in consegna", "consegnato"),
con un metodo per mostrare le info e un metodo per cambiare stato.

Deve esserci una classe Magazzino che contiene una lista (o dizionario) di pacchi e permette di aggiungere un pacco, 
cercarlo per codice, e mostrare tutti i pacchi in un certo stato.

Deve esserci infine una classe GestorePacchi che usa il magazzino per mettere un pacco “in consegna”, 
segnare un pacco come “consegnato” e calcolare il peso totale dei pacchi ancora non consegnati.

Nel programma principale crea almeno 5 pacchi, inseriscili nel magazzino, 
cambia lo stato di alcuni pacchi (almeno una consegna avviata e una consegna completata) 
e stampa: elenco pacchi “in magazzino”, elenco pacchi “in consegna” e il peso totale dei pacchi non ancora consegnati.
"""

class Pacco:
    
    stati = ["in magazzino", "in consegna", "consegnato"]
    
    def __init__(self, codice:str, peso:float, stato:str):      # stato può essere "in magazzino", "in consegna", "consegnato"
        self.codice = codice
        self.peso = peso
        
        # il costruttore si assicurerà che lo stato del pacco sia valido
        # quando si creerà un oggetto di tipo Pacco ritornerà un valore di True/False
        if stato in self.stati:
            self.stato = stato
            return True
        else:
            return False
        
    # metodi
    def mostra_info(self):
        pass
    
    def cambia_stato(self):
        pass
    
            

class Magazzino:
    
    lista_pacchi = {}
    
    def __init__(self):
        pass
    
    # metodi
    
    def aggiungi(self, codice:str, peso:float, stato:str):
        pass
    
    def cerca(self, codice:str, peso:float, stato:str)
        pass
    
    def mostra_tutti(self):
        pass
    
    

class GestorePacchi:
    
    def __init__(self):
        pass

# main

print("\n***** GESTORE PACCHI *****")

stop = False
while not stop:
    
    scelta = input("Cosa vuoi fare?"
                   "1. Visualizza stato pacchi"
                   "2. Cambia stato pacco"
                   "3. Uscita")
    
    match scelta:
        case "1":
            pass
    
        case "2":
            pass
        
        case "3":
            pass
        
        case _:
            pass