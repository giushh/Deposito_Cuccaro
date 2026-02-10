# pomeriggio 09/02/2026

"""
Esercizio: Sistema di Gestione Negozio
Lo scopo di questo esercizio è implementare un sistema di gestione per un negozio che deve
interagire con clienti, gestire l'inventario e permettere agli amministratori di
supervisionare le operazioni. Il sistema sarà strutturato in tre parti principali:
1.Gestione Clienti:
    I clienti possono visualizzare gli articoli disponibili in inventario.
    I clienti possono selezionare e acquistare articoli dall'inventario.
    Il sistema tiene traccia degli acquisti dei clienti.
2.Gestione dell'Inventario:
    Gli articoli in magazzino sono elencati con il nome, il prezzo e la quantità.
    È possibile aggiungere nuovi articoli all'inventario.
    Gli articoli possono essere rimossi o aggiornati (ad es., cambiare prezzo o
    quantità).
3.Amministrazione:
    Gli amministratori possono visualizzare un rapporto delle vendite.
    Gli amministratori possono visualizzare lo stato corrente dell'inventario.
    Il sistema tiene traccia dei guadagni totali.
    Puoi pre inserire gli amministratori non i clienti
Il sistema dovrebbe permettere di simulare un'interazione base tra il cliente e il negozio
dopo un login e una registrazione, nonché fornire gli strumenti necessari per la
manutenzione e l'analisi del negozio da parte degli amministratori.
"""

# pomeriggio 09/02/2026

class Negozio:
    inventario = {}
    guadagni_totali = 0.0
    vendite = []

    class Articolo:
        def __init__(self, codice, nome, prezzo, quantita):
            self.codice = codice
            self.nome = nome
            self.prezzo = float(prezzo)
            self.quantita = int(quantita)

        def descrizione(self):
            return f"[{self.codice}] {self.nome} - €{self.prezzo:.2f} (disp: {self.quantita})"

    @classmethod
    def articoli(cls):
        for codice, dati in cls.inventario.items():
            yield codice, dati

    @classmethod
    def stampa_inventario(cls):
        if not cls.inventario:
            print("\nInventario vuoto.")
            return
        print("\n--- Inventario ---")
        for codice, dati in cls.articoli():
            print(f"[{codice}] {dati['nome']} - €{dati['prezzo']:.2f} (disp: {dati['quantita']})")

    @classmethod
    def aggiungi_articolo(cls, codice, nome, prezzo, quantita):
        codice = codice.upper()
        # l'inventario è un dizionario innestato con chiave (codice) e valore un altro dizionario con nome, prezzo, quantità
        if codice in cls.inventario:
            cls.inventario[codice]["nome"] = nome
            cls.inventario[codice]["prezzo"] = float(prezzo)
            cls.inventario[codice]["quantita"] += int(quantita)
        else:
            cls.inventario[codice] = {
                "nome": nome,
                "prezzo": float(prezzo),
                "quantita": int(quantita)
            }
        print("\nArticolo inserito o aggiornato.")

    @classmethod
    def rimuovi_articolo(cls, codice):
        codice = codice.upper()
        if codice in cls.inventario:
            del cls.inventario[codice]
            print("\nArticolo rimosso.")
        else:
            print("\nArticolo non trovato.")

    
    @classmethod
    def aggiorna_articolo(cls, codice, nuovo_nome=None, nuovo_prezzo=None, nuova_quantita=None):
        codice = codice.upper()

        if codice not in cls.inventario:
            print("\nArticolo non trovato.")
            return

        if nuovo_nome is not None:
            cls.inventario[codice]["nome"] = str(nuovo_nome)

        if nuovo_prezzo is not None:
            cls.inventario[codice]["prezzo"] = float(nuovo_prezzo)

        if nuova_quantita is not None:
            cls.inventario[codice]["quantita"] = int(nuova_quantita)

        print("\nArticolo aggiornato.")

    @classmethod
    def acquista(cls, nome_cliente, codice, quantita):
        codice = codice.upper()
        quantita = int(quantita)

        if codice not in cls.inventario:
            print("\nArticolo non trovato.")
            return False, 0

        if quantita > cls.inventario[codice]["quantita"]:
            print("\nQuantità non disponibile.")
            return False, 0

        totale = cls.inventario[codice]["prezzo"] * quantita
        cls.inventario[codice]["quantita"] -= quantita
        cls.guadagni_totali += totale

        cls.vendite.append({
            "cliente": nome_cliente,
            "nome": cls.inventario[codice]["nome"],
            "quantita": quantita,
            "totale": totale
        })

        print(f"\nAcquisto completato: €{totale:.2f}")
        return True, totale

    @classmethod
    def resoconto_vendite(cls):
        print("\n--- Vendite ---")
        if not cls.vendite:
            print("Nessuna vendita.")
            return
        for v in cls.vendite:
            print(f"{v['cliente']} ha acquistato {v['quantita']} x {v['nome']} → €{v['totale']:.2f}")
        print(f"\nGuadagni totali: €{cls.guadagni_totali:.2f}")


def solo_amministratore(funzione):
    def wrapper(self, *args, **kwargs):
        if not self.utente.amministratore:
            print("\nAccesso negato: solo amministratore.")
            return None
        return funzione(self, *args, **kwargs)
    return wrapper


class Utente:
    def __init__(self, amministratore=False, nome=""):
        self.nome = nome
        self.amministratore = amministratore
        self.acquisti = []

    class Cliente:
        def __init__(self, utente):
            self.utente = utente

        def visualizza_articoli(self):
            Negozio.stampa_inventario()

        def compra_articolo(self):
            Negozio.stampa_inventario()
            codice = input("\nCodice articolo: ")
            quantita = input("Quantità: ")
            ok, totale = Negozio.acquista(self.utente.nome, codice, quantita)
            if ok:
                self.utente.acquisti.append((codice, quantita, totale))

        def storico_acquisti_cliente(self):
            print("\n--- Storico acquisti ---")
            if len(self.utente.acquisti) == 0:
                print("Nessun acquisto.")
                return
            for a in self.utente.acquisti:
                print(f"{a[1]} x {a[0]} → €{a[2]:.2f}")

    class Amministratore:
        def __init__(self, utente):
            self.utente = utente

        @solo_amministratore
        def visualizza_inventario(self):
            Negozio.stampa_inventario()

        @solo_amministratore
        def inserisci_articolo(self):
            codice = input("Codice: ")
            nome = input("Nome: ")
            prezzo = input("Prezzo: ")
            quantita = input("Quantità: ")
            Negozio.aggiungi_articolo(codice, nome, prezzo, quantita)

        @solo_amministratore
        def elimina_articolo(self):
            codice = input("Codice articolo: ")
            Negozio.rimuovi_articolo(codice)

        @solo_amministratore
        def aggiorna_articolo(self):
            codice = input("\nCodice articolo da aggiornare: ").strip()

            print("\nCosa vuoi aggiornare?")
            print("1) Nome")
            print("2) Prezzo")
            print("3) Quantità")
            scelta = input("Scelta: ")

            if scelta == "1":
                nuovo_nome = input("Nuovo nome: ")
                Negozio.aggiorna_articolo(codice, nuovo_nome=nuovo_nome)

            elif scelta == "2":
                nuovo_prezzo = input("Nuovo prezzo: ")
                Negozio.aggiorna_articolo(codice, nuovo_prezzo=nuovo_prezzo)

            elif scelta == "3":
                nuova_quantita = input("Nuova quantità: ")
                Negozio.aggiorna_articolo(codice, nuova_quantita=nuova_quantita)

            else:
                print("\nScelta non valida.")

        @solo_amministratore
        def resoconto_vendite(self):
            Negozio.resoconto_vendite()


# main

stop = False

while not stop:
    print("\n***** SCHERMATA PRINCIPALE *****")
    print("1) Login")
    print("2) Chiudi programma")

    scelta = input("Scelta: ")

    match scelta:
        case "1":
            nome = input("\nInserisci nome utente: ").strip()

            if nome == "12345":
                utente = Utente(True, "admin")
            else:
                utente = Utente(False, nome)

            cliente = Utente.Cliente(utente)
            amministratore = Utente.Amministratore(utente)

            esci_area_personale = False

            while not esci_area_personale:
                if utente.amministratore:
                    scelta = input(
                        "\n--- AREA AMMINISTRATORE ---"
                        "\n1. Visualizza inventario"
                        "\n2. Inserisci articolo"
                        "\n3. Elimina articolo"
                        "\n4. Aggiorna articolo"
                        "\n5. Vendite"
                        "\n6. Esci (torna alla schermata principale)"
                        "\nScelta: "
                    )

                    match scelta:
                        case "1":
                            amministratore.visualizza_inventario()
                        case "2":
                            amministratore.inserisci_articolo()
                        case "3":
                            amministratore.elimina_articolo()
                        case "4":
                            amministratore.aggiorna_articolo()
                        case "5":
                            amministratore.resoconto_vendite()
                        case "6":
                            print("\nUscita dall'area amministratore...")
                            esci_area_personale = True
                        case _:
                            print("\nScelta non valida.")
                            continue

                else:
                    scelta = input(
                        "\n--- AREA CLIENTE ---"
                        "\n1. Visualizza articoli"
                        "\n2. Acquista"
                        "\n3. Storico acquisti"
                        "\n4. Esci (torna alla schermata principale)"
                        "\nScelta: "
                    )

                    match scelta:
                        case "1":
                            cliente.visualizza_articoli()
                        case "2":
                            cliente.compra_articolo()
                        case "3":
                            cliente.storico_acquisti_cliente()
                        case "4":
                            print("\nUscita dall'area cliente...")
                            esci_area_personale = True
                        case _:
                            print("\nScelta non valida.")
                            continue

        case "2":
            print("\nChiusura programma.")
            stop = True

        case _:
            print("\nScelta non valida. Riprova.")
            continue
