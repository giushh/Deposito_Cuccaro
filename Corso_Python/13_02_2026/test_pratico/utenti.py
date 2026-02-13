from abc import ABC, abstractmethod


class Badge:

    def __init__(self, codice: str):
        # incapsulamento, attributi privati
        # accesso solo tramite get 
        self.__codice = codice
        self.__attivo = True

    def get_codice(self):
        return self.__codice

    def is_attivo(self):
        return self.__attivo

    def disattiva(self):
        if self.__attivo is False:
            print("Il badge era già disattivato.")
            return
        self.__attivo = False
        print("Badge disattivato.")

    def attiva(self):
        if self.__attivo is True:
            print("Il badge era già attivo.")
            return
        self.__attivo = True
        print("Badge attivato.")


class Utente(ABC):
    """
    classe astratta: ogni utente ha nome, id e badge.
    le sottoclassi devono implementare descrivi_ruolo() per l'astrazione.
    """

    def __init__(self, user_id: str, nome: str, badge: Badge):
        self.__user_id = user_id
        self.__nome = nome
        self.__badge = badge

    def get_user_id(self):
        return self.__user_id

    def get_nome(self):
        return self.__nome

    def get_badge(self):
        return self.__badge

    @abstractmethod
    def descrivi_ruolo(self):
        # metodo astratto, dovrà essere implementato dalle classi figlie 
        print("\nQualcosa non va, sono il metodo della classe Utente.")


class Dipendente(Utente):       
    # ereditarietà, Dipendente è figlia di Utente
    def __init__(self, user_id: str, nome: str, badge: Badge, reparto: str):
        super().__init__(user_id, nome, badge)
        self.__reparto = reparto

    def get_reparto(self):
        return self.__reparto

    def descrivi_ruolo(self):
        return f"Dipendente - Reparto: {self.__reparto}"


class Responsabile(Utente):
    def __init__(self, user_id: str, nome: str, badge: Badge, area: str):
        super().__init__(user_id, nome, badge)
        self.__area = area

    def get_area(self):
        return self.__area

    def descrivi_ruolo(self):
        return f"Responsabile - Area: {self.__area}"
