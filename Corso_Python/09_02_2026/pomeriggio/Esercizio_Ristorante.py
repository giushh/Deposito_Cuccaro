# pomeriggio 09/02/2026 - Esercizio Ristorante

"""
Obiettivo: Creare una classe Ristorante che permetta di gestire alcune funzionalità di base .
Requisiti:
1.Definizione della Classe:
    Creare una classe chiamata Ristorante.
    La classe dovrebbe avere un costruttore __init__ che accetta due parametri: nome (nome del ristorante) e
    tipo_cucina (tipo di cucina offerta).
    Definire un attributo aperto che indica se il ristorante è aperto o chiuso. Questo attributo deve essere
    impostato su False di default (cioè, il ristorante è chiuso).
    Una lista di liste menu dove dentro ci sono i piatti e prezzi che ha il ristorante
2.Metodi della Classe:
    - descrivi_ristorante(): Un metodo che stampa una frase descrivendo il ristorante, includendo il nome e il
    tipo di cucina.
    - stato_apertura(): Un metodo che stampa se il ristorante è aperto o chiuso.
    - apri_ristorante(): Un metodo che imposta l'attributo aperto su True e stampa un messaggio che indica che
    il ristorante è ora aperto.
    - chiudi_ristorante(): Un metodo che imposta l'attributo aperto su False e stampa un messaggio che indica
    che il ristorante è ora chiuso.
    - aggiungi_al_menu(): Un metodo per aggiungere piatti al menu
    - togli_dal_menu(): Un metodo per togliere piatti al menu
    - stampa_menu(): Un metodo per stampare il menu
3.Testare la Classe:
    Creare un'istanza della classe Ristorante, passando i valori appropriati al costruttore.
    Testare tutti i metodi creati per assicurarsi che funzionino come previsto.
    
    
EXTRA: utilizzo dei dizionari
"""

class Ristorante:
    # attributi
    aperto = False
    menu = {}           # menu è di tipo dizionario, dove avrà coppie di (piatto, prezzo) per ogni elemento
    
    # costruttore
    def __init__(self, nome:str, tipo_cucina:str):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        
    # metodi della classe
    def descrivi_ristorante(self):
        print(f"\n{self.nome} è un ristorante che ha un tipo di cucina {self.tipo_cucina}")
        
    def stato_apertura(self):
        if self.aperto:
            print(f"\nIl ristorante {self.nome} è aperto")
        else: 
            print(f"\nIl ristorante {self.nome} è chiuso")
            
    def apri_ristorante(self):
        self.aperto = True
        self.stato_apertura()
        
    def chiudi_ristorante(self):
        self.aperto = False
        self.stato_apertura()
        
    def aggiungi_al_menu(self, piatto:str, prezzo:int):
        self.menu[piatto] = prezzo

    def togli_dal_menu(self, piatto):
        # il metodo .pop("key") rimuove l'elemento associato a quella key dal dizionario
        self.menu.pop(piatto)

    def stampa_menu(self):
        print(f"\nMenu del ristorante {self.nome}:\n")
        count = 1
        for chiave, valore in self.menu.items():
            print(f"{count}. {chiave}: {valore} €")
            count += 1

# main 

ristor_1 = Ristorante("Marigliano", "italiana")

print(f"\n***** Gestione Ristorante {ristor_1.nome} *****")

stop = False
while not stop:
    
    scelta = input("\nVuoi:"
                   "\n1. Descrizione ristorante"
                   "\n2. Stato del ristorante"
                   "\n3. Apri ristorante"
                   "\n4. Chiudi ristorante"
                   "\n5. Aggiungi al menu"
                   "\n6. Togli dal menu"
                   "\n7. Stampa menu"
                   "\n8. Uscita"
                   "\nInserisci valore corrispondente ")
    
    match scelta:
        case "1":
            ristor_1.descrivi_ristorante()
        case "2":
            ristor_1.stato_apertura()
        case "3":
            if ristor_1.aperto:
                print("\nE' già aperto")
            else:
                ristor_1.apri_ristorante()
        case "4":
            if not ristor_1.aperto:
                print("\nE' già chiuso")
            else:
                ristor_1.chiudi_ristorante()
        case "5":
            if not ristor_1.aperto:
                print(f"\nIl ristorante {ristor_1.nome} è chiuso, non puoi aggiungere piatti al menu.")
            else:
                piatto = input("\nNome del piatto: ")
                prezzo = int(input("Prezzo: "))
                ristor_1.aggiungi_al_menu(piatto, prezzo)
                print(f"{piatto} aggiunto")
        case "6":
            if not ristor_1.aperto:
                print(f"\nIl ristorante {ristor_1.nome} è chiuso, non puoi togliere piatti dal menu.")
            else:
                ristor_1.stampa_menu()
                piatto = input("\nChe piatto vuoi eliminare?")
                ristor_1.togli_dal_menu(piatto)
                print(f"{piatto} rimosso")
        case "7":
            ristor_1.stampa_menu()
        case "8":
            print("\n-- Uscita")
            stop = True
        case _: 
            print("Comando non valido. \n--Uscita")
            stop = True
            
            
