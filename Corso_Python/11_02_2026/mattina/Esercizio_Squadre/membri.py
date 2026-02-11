
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
        pass


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
        pass

    def gioca_partita(self) -> int:
        pass


class CuocoAntipasti(Giocatore):
    def __init__(self, nome: str, eta: int, esperienza: dict):
        super().__init__(nome, eta, esperienza)
        self.categoria = CategoriaAntipasti

    def prepara_portata(self) -> int:
        pass


class CuocoPrimi(Giocatore):
    def __init__(self, nome: str, eta: int, esperienza: dict):
        super().__init__(nome, eta, esperienza)
        self.categoria = CategoriaPrimi

    def prepara_portata(self) -> int:
        pass


class CuocoSecondi(Giocatore):
    def __init__(self, nome: str, eta: int, esperienza: dict):
        super().__init__(nome, eta, esperienza)
        self.categoria = CategoriaSecondi

    def prepara_portata(self) -> int:
        pass


class Pasticcere(Giocatore):
    def __init__(self, nome: str, eta: int, esperienza: dict):
        super().__init__(nome, eta, esperienza)
        self.categoria = CategoriaDolci

    def prepara_portata(self) -> int:
        pass


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
        self.membri = []  # lista di MembroSquadra

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
                # __name__ è un metodo che restituisce il nome della classe come stringa
                elem.descrivi()

    def giocatori(self):
        # generator: yield solo istanze di Giocatore
        pass

    def seleziona_giocatore_per_categoria(self, categoria: type):
        """
        categoria: classe Categoria (es. CategoriaAntipasti).
        Deve mostrare i candidati e la loro esperienza (scala 1..5) su tutte le categorie.
        """
        pass
