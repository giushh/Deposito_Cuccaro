
import random

# classi figli

class Categoria:
    nome = "generica"

    @classmethod
    def label(cls) -> str:
        return cls.nome


class CategoriaAntipasti(Categoria):
    nome = "antipasti"


class CategoriaPrimi(Categoria):
    nome = "primi"


class CategoriaSecondi(Categoria):
    nome = "secondi"


class CategoriaDolci(Categoria):
    nome = "dolci"


# classi padri

class MembroSquadra:
    def __init__(self, nome: str, eta: int):
        self.nome = nome
        self.eta = int(eta)

    def descrivi(self) -> None:
        print(f"{self.nome} ({self.eta} anni) - membro della squadra.")
        


class Giocatore(MembroSquadra):
    """
    Esperienza su scala 1..5 per ogni categoria.
    esperienza è un dizionario del tipo
    self.esperienza = {
        "antipasti": 1..5,
        "primi": 1..5,
        "secondi": 1..5,
        "dolci": 1..5
}
    """
    def __init__(self, nome: str, eta: int, esperienza: dict):
        super().__init__(nome, eta)
        self.esperienza = esperienza

    def mostra_esperienza(self) -> None:
        print(f"\nEsperienza di {self.nome}:")

        categorie = ["antipasti", "primi", "secondi", "dolci"]

        for cat in categorie:
            valore = self.esperienza[cat]
            pieno = "★" * valore
            vuoto = "☆" * (5 - valore)
            print(f" - {cat}: {pieno}{vuoto} ({valore}/5)")


    def gioca_partita(self) -> int:
        # nelle classi figlie sarà specializzato in prepara_portata()
        return self.prepara_portata()
    
    def prepara_portata(self) -> int:
        
    # membrosquadra (nome,eta) -> giocatore (+esperienza) -> ruolo (+categoria)

        # le classi categoria hanno un metodo label() che restituisce il nome della categoria (in questo caso)
        # e viene usato come chiave per prendere il valore corrispondente nel dizionario
        chiave = self.categoria.label()
        livello = self.esperienza[chiave]

        base = random.randint(1, 8)
        bonus = livello * 3
        punteggio = base + bonus

        print(f"{self.nome} prepara {chiave}: base={base}, bonus={bonus}, totale={punteggio}")

        return punteggio


class CuocoAntipasti(Giocatore):
        
    def __init__(self, nome: str, eta: int, esperienza: dict):
        super().__init__(nome, eta, esperienza)
        self.categoria = CategoriaAntipasti    


class CuocoPrimi(Giocatore):
    def __init__(self, nome: str, eta: int, esperienza: dict):
        super().__init__(nome, eta, esperienza)
        self.categoria = CategoriaPrimi


class CuocoSecondi(Giocatore):
    def __init__(self, nome: str, eta: int, esperienza: dict):
        super().__init__(nome, eta, esperienza)
        self.categoria = CategoriaSecondi


class Pasticcere(Giocatore):
    def __init__(self, nome: str, eta: int, esperienza: dict):
        super().__init__(nome, eta, esperienza)
        self.categoria = CategoriaDolci


class Allenatore(MembroSquadra):
    def __init__(self, nome: str, eta: int, anni_di_esperienza: int):
        super().__init__(nome, eta)
        self.anni_di_esperienza = int(anni_di_esperienza)

    def dirige_allenamento(self) -> None:
        pass


class Assistente(MembroSquadra):
    def __init__(self, nome: str, eta: int, specializzazione: str):
        super().__init__(nome, eta)
        self.specializzazione = specializzazione

    def supporta_team(self) -> None:
        pass


class Squadra:
    def __init__(self, nome: str):
        self.nome = nome
        self.membri = []  # lista di MembroSquadra, contiene TUTTI i ruoli

    def aggiungi_membro(self, membro: MembroSquadra) -> None:
        if isinstance(membro, MembroSquadra):       # verifica se l'oggetto deriva dalla quella classe
            self.membri.append(membro)
            print("\nMembro aggiunto.")
        else: 
            print("Membro non valido.")

    def descrivi_squadra(self) -> None:
        print(f"\n=== {self.nome} ===")

        if len(self.membri) == 0:
            print("Nessun membro presente.")
        else:
            for elem in self.membri:
                print(f"\nRuolo: {type(elem).__name__}")
                # __name__ è un attributo che restituisce il nome della classe come stringa
                elem.descrivi()

    def giocatori(self):
        # generator: yield solo istanze di Giocatore
        # idea: scorre tutti i giocatori della lista membri, se trova Giocatore lo restituisce
        for elem in self.membri:
            if isinstance(elem, Giocatore):
                yield elem

    def seleziona_giocatore_per_categoria(self, categoria: type):
        """
            categoria: classe Categoria (es. CategoriaAntipasti).

            Il metodo individua tutti i giocatori della squadra specializzati
            nella categoria richiesta, mostra i candidati disponibili e la loro
            esperienza (scala 1..5) per ciascuna portata.

            Tra i candidati viene selezionato un giocatore (ad esempio in modo
            casuale) che verrà incaricato di preparare la portata.

            Il metodo restituisce il giocatore scelto, così nel main sarà possibile
            richiamare:

                g1 = squadra1.seleziona_giocatore_per_categoria(cat)
                p1 = g1.prepara_portata()

            e successivamente confrontare i punteggi delle due squadre.


        
        print(f"\nSelezione per {categoria.label()} - {self.nome}")
            
        for g in self.giocatori():
            if g.categoria == categoria:
                print(f"\nGiocatore trovato: {g.nome}")
                g.mostra_esperienza()
                return g
            
        print("Nessun giocatore trovato per questa categoria.")
        return None"""
        
        candidati = []

        for g in self.giocatori():
            if g.categoria == categoria:
                candidati.append(g)

        if len(candidati) == 0:
            print("Nessun giocatore trovato per questa categoria.")
            return None

        print("\nCandidati disponibili:")
        for g in candidati:
            print(f"- {g.nome}")
            g.mostra_esperienza()

        scelto = random.choice(candidati)
        print(f"\nScelto per la portata: {scelto.nome}")

        return scelto
    
    def bonus_staff_round(self) -> int:
        """
        bonus casuale per la singola portata (round).
        - allenatore: può dare +1 con probabilità 50%
        - ogni Assistente: può dare +1 con probabilità 30%
        """
        bonus = 0

        for m in self.membri:
            if isinstance(m, Allenatore):
                if random.random() < 0.5:
                    bonus += 1
            elif isinstance(m, Assistente):
                if random.random() < 0.3:
                    bonus += 1

        return bonus


