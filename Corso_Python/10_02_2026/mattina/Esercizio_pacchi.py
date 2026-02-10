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
    
    stati = ["magazzino", "consegna", "consegnato"]
    
    def __init__(self, magazzino, codice:str, peso:float, stato:str):
        self.magazzino = magazzino
        self.codice = codice.upper()
        self.peso = float(peso)
        self.stato = stato
        
        if self.stato in self.stati:
            self.magazzino.aggiungi_modifica(self.codice, self.peso, self.stato)

    def mostra_info(self):
        print(f"[{self.codice}] Peso:{self.peso} - Stato:{self.stato}")
    
    def cambia_stato(self, nuovo_stato:str):
        if nuovo_stato in self.stati:
            self.stato = nuovo_stato
            self.magazzino.aggiungi_modifica(self.codice, self.peso, self.stato)
            return True
        else:
            return False


class Magazzino:
    
    lista_pacchi = {}
    
    def __init__(self, nome:str):
        self.nome = nome
    
    def aggiungi_modifica(self, codice:str, peso, stato):
        codice = codice.upper()
        
        if codice in self.lista_pacchi:
            self.lista_pacchi[codice]["peso"] = float(peso)
            self.lista_pacchi[codice]["stato"] = stato
            print("\nOrdine aggiornato.")
        else:
            self.lista_pacchi[codice] = {
                "peso" : float(peso),
                "stato" : stato 
            }
            print("\nOrdine aggiunto.")
    
    def cerca_per_codice(self, codice:str):
        codice = codice.upper()
        
        if codice in self.lista_pacchi:
            print("\nOrdine trovato:\n")
            print(f"[{codice}] Peso:{self.lista_pacchi[codice]['peso']} - Stato:{self.lista_pacchi[codice]['stato']}")
        else:
            print("Ordine non trovato.")

    # [TO DO] def cerca_per_peso
    # [TO DO] def cerca_per_stato
    
    def mostra_tutti(self):
        if not self.lista_pacchi:
            print("\nNessun pacco presente.")
            return
        
        for codice, dati in self.lista_pacchi.items():
            print(f"[{codice}] Peso:{dati['peso']} - Stato:{dati['stato']}")

    def mostra_per_stato(self, stato:str):
        trovati = False
        for codice, dati in self.lista_pacchi.items():
            if dati["stato"] == stato:
                print(f"[{codice}] Peso:{dati['peso']} - Stato:{dati['stato']}")
                trovati = True
        if not trovati:
            print("\nNessun pacco trovato per questo stato.")


class GestorePacchi:
    
    def __init__(self, magazzino:Magazzino):
        self.magazzino = magazzino
    
    def cambio_stato(self, codice:str, stato_out:str):
        codice = codice.upper()
        
        if codice in self.magazzino.lista_pacchi:
            if stato_out in Pacco.stati:
                self.magazzino.lista_pacchi[codice]["stato"] = stato_out
                print("\nStato aggiornato.")
            else:
                print("\nStato non valido.")
        else:
            print("\nOrdine non trovato.")
    
    def calcolo_peso(self, lista_pacchi:dict):
        totale = 0.0
        for codice, dati in lista_pacchi.items():
            totale += float(dati["peso"])
        return totale

    def calcolo_peso_non_consegnati(self):
        totale = 0.0
        for codice, dati in self.magazzino.lista_pacchi.items():
            if dati["stato"] != "consegnato":
                totale += float(dati["peso"])
        return totale


print("\n***** GESTORE PACCHI *****")

magazzino = Magazzino("Magazzino Centrale")
gestore = GestorePacchi(magazzino)

p1 = Pacco(magazzino, "A001", 2.5, "magazzino")
p2 = Pacco(magazzino, "B010", 1.2, "magazzino")
p3 = Pacco(magazzino, "C036", 5.0, "magazzino")
p4 = Pacco(magazzino, "D785", 0.8, "magazzino")
p5 = Pacco(magazzino, "E004", 3.4, "magazzino")

stop = False
while not stop:
    
    scelta = input("\nPuoi:"
                   "\n1. Visualizza stato pacchi"
                   "\n2. Cambia stato pacco"
                   "\n3. Uscita"
                   "\nIndica il numero corrispondente \n> ")
    
    match scelta:
        case "1":
            print("\n--- Pacchi in magazzino ---")
            magazzino.mostra_per_stato("magazzino")
            print("\n--- Pacchi in consegna ---")
            magazzino.mostra_per_stato("consegna")
            print("\n--- Pacchi consegnati ---")
            magazzino.mostra_per_stato("consegnato")
            print("\nPeso totale pacchi non ancora consegnati:", gestore.calcolo_peso_non_consegnati())
    
        case "2":
            codice = input("\nInserisci il codice pacco\n> ").upper()
            if codice in magazzino.lista_pacchi:
                stato = input("Inserisci il nuovo stato (magazzino / consegna / consegnato)\n> ")
                
                if stato in Pacco.stati:
                    gestore.cambio_stato(codice, stato)
                else:
                    print("Stato non valido.")
            else:
                print("Codice pacco non presente in magazzino.")

        case "3":
            print("\n-- Uscita")
            stop = True
        
        case _:
            print("\nComando non valido. \nRiprova.")
            continue
