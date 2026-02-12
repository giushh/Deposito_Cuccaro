# mattina 12/02/2026

"""
creare una classe base MetodoPagamento e diverse classi derivate che rappresentano
diversi metodi di pagamento. Questo scenario permetterà di vedere il polimorfismo in
azione, permettendo alle diverse sottoclassi di implementare i loro specifici
comportamenti di pagamento, pur aderendo all'interfaccia comune definita dalla classe
base.
1.Classe MetodoPagamento:
    Metodi:
    effettua_pagamento(importo): un metodo che ogni sottoclasse dovrà implementare.
2.Classi Derivate:
    CartaDiCredito:
        Metodi come effettua_pagamento(importo) che simula un pagamento tramite carta
        di credito.
    PayPal:
        Metodi come effettua_pagamento(importo) che simula un pagamento tramite PayPal.
    BonificoBancario:
        Metodi come effettua_pagamento(importo) che simula un pagamento tramite
        bonifico bancario.
3.GestorePagamenti:
    Una classe che usa un'istanza di MetodoPagamento per effettuare pagamenti, senza
    preoccuparsi del dettaglio del metodo di pagamento.
    
Rendilo ripetibile
"""
# classe padre
class MetodoPagamento:
    
    # metodi
    def effettua_pagamento(self, importo):
        print("\nQualcosa non ha funzionato, genio")        # se stampa questa, il polimorfismo non ha funzionato
        
# classi figli

class CartaDiCredito(MetodoPagamento):
    # costruttore
    def __init__(self, nome):
        super().__init__()
        self.nome = nome
    
    # metodi 
    def effettua_pagamento(self, importo):
        print(f"Pagamento effettuato con carta di credito ({importo} euro)")

class Paypal(MetodoPagamento):
    # costruttore
    def __init__(self, nome):
        super().__init__()
        self.nome = nome
    
    # metodi 
    def effettua_pagamento(self, importo):
        print(f"Pagamento effettuato con Paypal ({importo} euro)")
        
class BonificoBancario(MetodoPagamento):
    # costruttore
    def __init__(self, nome):
        super().__init__()
        self.nome = nome
    
    # metodi 
    def effettua_pagamento(self, importo):
        print(f"Pagamento effettuato con bonifico bancario ({importo} euro)")

# gestore

class GestorePagamenti:
    # costruttore
    def __init__(self, metodo):
        self.metodo = metodo        # si specializza in base alla classe passata

    # metodi
    def pagamento(self, metodo):       # stessi parametri di effettua_pagamento
        metodo.effettua_pagamento(importo)     # richiama il metodo della classe corrispondente



metodi_disponibili = [CartaDiCredito("Carta di credito"), Paypal("Paypal"), BonificoBancario("Bonifico Bancario")]
# lista degli oggetti corrispondenti ai 3 pagamaenti

def stampa_metodi(lista):
    print("\nPagamenti disponibili:\n")
    count = 1
    for elem in lista:
        print(f"{count}. {elem.nome}")
        count += 1


stop = False
while not stop:
    
    scelta = input("\nPuoi:"
                   "\n1. Visualizzare pagamenti disponibili"
                   "\n2. Effetturare un pagamento"
                   "\n3. Uscita"
                   "\nIndica il numero corrispondente \n> ")
    
    match scelta:
        case "1":
            stampa_metodi(metodi_disponibili)
    
        case "2":
            stampa_metodi(metodi_disponibili)
            quale_metodo = input("Come vuoi effettuare il pagamento? Scrivi il nome del pagamento\n").lower()
            importo = int(input("Importo: "))
            gestore = GestorePagamenti(quale_metodo)
            gestore.pagamento(importo)

        case "3":
            print("\n-- Uscita")
            stop = True
        case _:
            print("\nComando non valido. \nRiprova.")
            continue
