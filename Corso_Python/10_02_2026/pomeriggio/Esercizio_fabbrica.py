# pomeriggio 10/02/2026

"""
Lo scopo dell'esercizio è creare un sistema di gestione per una fabbrica che produce e vende vari tipi di prodotti
Creare:
Classe Prodotto:
    Attributi:
    nome (stringa che descrive il nome del prodotto)
    costo_produzione (costo per produrre il prodotto)
    prezzo_vendita (prezzo a cui il prodotto viene venduto al pubblico)
    Metodi:
    calcola_profitto: restituisce la differenza tra il prezzo di vendita e il costo di produzione.
Classi parallele:
    Creare almeno due classi parallele a Prodotto, per esempio Elettronica e Abbigliamento.
    Aggiungere attributi specifici per ciascun tipo di prodotto, come materiale per Abbigliamento e garanzia per Elettronica.
Classe Fabbrica:
Attributi:
    inventario: un dizionario che tiene traccia del numero di ogni tipo di prodotto in magazzino.
    Metodi:
    aggiungi_prodotto: aggiunge prodotti all'inventario.
    vendi_prodotto: diminuisce la quantità di un prodotto in inventario e stampa il profitto realizzato dalla vendita.
    resi_prodotto: aumenta la quantità di un prodotto restituito in inventario.
"""

# classi padri

class Prodotto:
    
    # costruttore
    def __init__(self, nome: str, costo_produzione: int, prezzo_vendita: int, quantita: int):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.quantita = quantita
        
    # metodi
    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione


class Fabbrica:
    # inventario: dizionario con chiave = nome (lower) e valore = dict con costo_produzione, prezzo_vendita, quantita, categoria
    
    # costruttore
    def __init__(self, nome: str):
        self.nome = nome
        self.inventario = {}

    # metodi
    
    def aggiungi_prodotto(self, nome: str, costo_produzione: int, prezzo_vendita: int, quantita: int, categoria: str):
        nome = nome.lower()
        categoria = categoria.lower()
        
        if nome in self.inventario:
            # aggiorno i prezzi e incremento la quantità
            self.inventario[nome]["costo_produzione"] = costo_produzione
            self.inventario[nome]["prezzo_vendita"] = prezzo_vendita
            self.inventario[nome]["quantita"] += quantita
            self.inventario[nome]["categoria"] = categoria
            print("Prodotto aggiornato.")
        else:
            self.inventario[nome] = {
                "costo_produzione": costo_produzione,
                "prezzo_vendita": prezzo_vendita,
                "quantita": quantita,
                "categoria": categoria
            }
            print("Prodotto aggiunto")
                   
    def vendi_prodotto(self, nome: str, quantita: int, categoria: str):
        """
        diminuisce la quantità di un prodotto in inventario 
        e stampa il profitto realizzato dalla vendita.
        """
        nome = nome.lower()
        categoria = categoria.lower()
        
        if nome not in self.inventario:
            print("\nProdotto non trovato") 
            return
        
        prodotto = self.inventario[nome]

        if prodotto["categoria"] != categoria:
            print("\nProdotto trovato ma la categoria non corrisponde.")
            return

        if quantita <= 0:
            print("Quantità non valida")
            return

        if quantita <= prodotto["quantita"]:
            prodotto["quantita"] -= quantita

            profitto_unitario = prodotto["prezzo_vendita"] - prodotto["costo_produzione"]
            profitto_totale = profitto_unitario * quantita

            print(f"\nVendita completata: {quantita} unità di '{nome}' ({categoria})")
            print(f"Profitto unitario: €{profitto_unitario}")
            print(f"Profitto totale:  €{profitto_totale}")
        else:
            print("Quantità non disponibile")
            
            
    def resi_prodotto(self, nome: str, quantita: int, categoria: str):
        """
        resi_prodotto: aumenta la quantità di un prodotto restituito 
        in inventario.
        """
        nome = nome.lower()
        categoria = categoria.lower()

        if nome not in self.inventario:
            print("Il prodotto non esiste nell'inventario")
            return
        
        prodotto = self.inventario[nome]
        if prodotto["categoria"] != categoria:
            print("\nProdotto trovato ma la categoria non corrisponde.")
            return
        
        if quantita <= 0:
            print("Quantità non valida")
            return

        self.inventario[nome]["quantita"] += quantita
        print(f"Reso registrato: +{quantita} unità di '{nome}' ({categoria})")

    def mostra_inventario(self, categoria: str):
        categoria = categoria.lower()

        trovato = False
        print(f"\n--- Inventario ({categoria}) ---")
        for nome, dati in self.inventario.items():
            if dati["categoria"] == categoria:
                trovato = True
                print(f"[{nome}] - costo: €{dati['costo_produzione']} | prezzo: €{dati['prezzo_vendita']} | qta: {dati['quantita']}")
        
        if not trovato:
            print("Nessun prodotto presente per questa categoria.")


# classi figli

class Elettronica(Prodotto):
    
    def __init__(self, nome, costo_produzione, prezzo_vendita, anni_garanzia: int, quantita: int):
        super().__init__(nome, costo_produzione, prezzo_vendita, quantita)
        self.anni_garanzia = anni_garanzia


class Abbigliamento(Prodotto):
    
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale: str, quantita: int):
        super().__init__(nome, costo_produzione, prezzo_vendita, quantita)
        self.materiale = materiale


# main

print("\n***** GESTIONE FABBRICA *****")

CATEGORIE = ["elettronica", "abbigliamento", "prodotto"]

def scegli_categoria():
    # didattico e semplice: l'utente scrive direttamente il nome della categoria
    print("\nCategorie disponibili:", CATEGORIE)
    categoria = input("Scrivi la categoria: ").lower()

    if categoria in CATEGORIE:
        return categoria
    else:
        print("Categoria non valida.")
        return None


nome_fabbrica = input("Nome fabbrica: ")
fabbrica = Fabbrica(nome_fabbrica)

stop = False
while not stop:
    
    scelta = input(
        "\nPuoi:"
        "\n1. Aggiungi prodotto"
        "\n2. Vendi prodotto"
        "\n3. Reso prodotto"
        "\n4. Mostra inventario"
        "\n5. Uscita"
        "\nIndica il numero corrispondente \n> "
    )
    
    match scelta:
        case "1":
            print("\n--- Aggiungi prodotto ---")
            categoria = scegli_categoria()
            if categoria is None:
                continue

            nome = input("Nome prodotto: ")
            costo_produzione = int(input("Costo produzione: "))
            prezzo_vendita = int(input("Prezzo vendita: "))
            quantita = int(input("Quantità: "))

            fabbrica.aggiungi_prodotto(nome, costo_produzione, prezzo_vendita, quantita, categoria)
    
        case "2":
            print("\n--- Vendi prodotto ---")
            categoria = scegli_categoria()
            if categoria is None:
                continue

            nome = input("Nome prodotto: ")
            quantita = int(input("Quantità da vendere: "))

            fabbrica.vendi_prodotto(nome, quantita, categoria)

        case "3":
            print("\n--- Reso prodotto ---")
            categoria = scegli_categoria()
            if categoria is None:
                continue

            nome = input("Nome prodotto: ")
            quantita = int(input("Quantità resa: "))

            fabbrica.resi_prodotto(nome, quantita, categoria)

        case "4":
            categoria = scegli_categoria()
            if categoria is None:
                continue

            fabbrica.mostra_inventario(categoria)

        case "5":
            print("\n-- Uscita")
            stop = True

        case _:
            print("\nComando non valido. \nRiprova.")
            continue