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
    Un dizionario menu dove dentro ci sono i piatti e prezzi che ha il ristorante
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
"""

class Ristorante:
    # attributi
    aperto = False
    menu = {}           # menu è di tipo dizionario, dove avrà coppie di (piatto, prezzo) per ogni elemento
    
    # costruttore
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        
    # metodi della classe
    def descrivi_ristorante(self):
        print(f"{self.nome} è un ristorante che ha un tipo di cucina {self.tipo_cucina}")
        
    def stato_ristorante(self):
        if self.aperto:
            print(f"Il ristorante {self.nome} è aperto")
        else: 
            print(f"Il ristorante {self.nome} è chiuso")
            
    def apri_ristorante(self):
        self.aperto = True
        self.stato_ristorante
        
    def chiudi_ristorante(self):
        self.aperto = False
        self.stato_ristorante
        
    def aggiungi_al_menu(self, piatto, prezzo):
        self.menu[piatto] = prezzo

        
