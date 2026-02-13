from datetime import datetime
from utenti import Utente


def log_badge(azione):
    def decorator(funzione):
        def wrapper(self, utente, *args, **kwargs):

            timestamp_prima = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            codice = utente.get_badge().get_codice()

            print(f"[{timestamp_prima}] {azione} - Badge {codice} - Utente {utente.get_nome()}")

            risultato = funzione(self, utente, *args, **kwargs)

            timestamp_dopo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp_dopo}] Fine operazione {azione}")

            return risultato
        return wrapper
    return decorator


class RegistroAccessi:
    """gestisce la lista dei log """

    def __init__(self):
        self.__eventi = []  # PRIVATO

    def aggiungi_evento(self, evento: dict):
        self.__eventi.append(evento)

    def mostra_eventi(self):
        if len(self.__eventi) == 0:
            print("\nNessun evento registrato.")
            return

        print("\n--- REGISTRO ACCESSI ---")
        for evento in self.__eventi:
            timestamp = evento["timestamp"]
            azione = evento["azione"]
            nome = evento["nome"]
            badge = evento["badge"]
            ruolo = evento["ruolo"]

            print(f"{timestamp} | {azione} | {nome} | Badge {badge} | {ruolo}")


class ControlloAccessi:
    """controllo accessi entrata/uscita/bagno """

    def __init__(self, registro: RegistroAccessi):
        self.__registro = registro  # PRIVATO

    def _badge_valido(self, utente: Utente):
        # PROTETTO: metodo interno utilizzabile eventualmente da sottoclassi
        return utente.get_badge().is_attivo()

    def _registra(self, utente: Utente, azione: str):
        # PROTETTO: logica interna riutilizzabile da eventuali classi figlie
        evento = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "azione": azione,
            "nome": utente.get_nome(),
            "badge": utente.get_badge().get_codice(),
            "ruolo": utente.descrivi_ruolo()
        }
        self.__registro.aggiungi_evento(evento)

    @log_badge("ENTRATA")
    def entra(self, utente: Utente):
        if not self._badge_valido(utente):
            print("Accesso negato: badge non attivo.")
            return False

        self._registra(utente, "ENTRATA")
        print("Accesso consentito: entrata registrata.")
        return True

    @log_badge("USCITA")
    def esci(self, utente: Utente):
        if not self._badge_valido(utente):
            print("Uscita negata: badge non attivo.")
            return False

        self._registra(utente, "USCITA")
        print("Uscita registrata.")
        return True

    @log_badge("BAGNO")
    def vai_in_bagno(self, utente: Utente):
        if not self._badge_valido(utente):
            print("Operazione negata: badge non attivo.")
            return False

        self._registra(utente, "BAGNO")
        print("Pausa bagno registrata.")
        return True
