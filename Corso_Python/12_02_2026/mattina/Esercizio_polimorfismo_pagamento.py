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
        print(f"\n---> Pagamento effettuato con carta di credito ({importo} euro)")

class Paypal(MetodoPagamento):
    # costruttore
    def __init__(self, nome):
        super().__init__()
        self.nome = nome
    
    # metodi 
    def effettua_pagamento(self, importo):
        print(f"\n---> Pagamento effettuato con Paypal ({importo} euro)")
        
class BonificoBancario(MetodoPagamento):
    # costruttore
    def __init__(self, nome):
        super().__init__()
        self.nome = nome
    
    # metodi 
    def effettua_pagamento(self, importo):
        print(f"\n---> Pagamento effettuato con bonifico bancario ({importo} euro)")

# gestore

class GestorePagamenti:
    # costruttore
    def __init__(self, metodo):
        self.metodo = metodo        # passa l'oggetto della classe specifica

    # metodi
    def pagamento(self, importo):       # stessi parametri di effettua_pagamento
        self.metodo.effettua_pagamento(importo)     # richiama il metodo della classe corrispondente



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

            # l'utente sceglie con un numero 
            indice = int(input("\nScegli il metodo inserendo il numero corrispondente: ")) - 1

            # controllo indice
            if indice < 0 or indice >= len(metodi_disponibili):
                print("Scelta non valida.")
                continue

            # recupera il corrispondente oggetto 
            metodo_scelto = metodi_disponibili[indice]

            importo = int(input("Importo: "))

            # gestore ottiene l'oggetto 
            gestore = GestorePagamenti(metodo_scelto)

            # viene eseguito il pagamento, senza sapere qualche classe sia
            gestore.pagamento(importo)


        case "3":
            print("\n-- Uscita")
            stop = True
        case _:
            print("\nComando non valido. \nRiprova.")
            continue
