# pomeriggio 11/02/2026

"""
Creare una classe ContoBancario che incapsula le informazioni di un conto e fornisce metori per gestire il saldo in modo sicuro.
L'obiettivo è utilizzare l'incapsulamento per prevenire accessi non autorizzati o modifiche inappropriate al saldo del conto.

Classe ContoBancario:
Attributi privati:
__titolare (stringa che rappresenta il nome del titolare del conto)
__saldo (decimale che rappresenta il saldo del conto)
Metodi pubblici:
deposita(importo): aggiunge un importo al saldo solo se l'importo è positivo.
preleva(importo): sottrae un importo dal saldo solo se ci sono fondi sufficienti e l'importo è positivo.
visualizza_saldo(): restituisce il saldo corrente senza permettere la sua modifica diretta.
Gestione dei Metodi e Sicurezza:
I metodi deposita e preleva devono controllare che gli importi siano validi (e.g., non negativi).
Aggiungere metodi "getter" e "setter" per gli attributi come _titolare, applicando validazioni appropriate (e.g., il titolare deve essere una stringa non vuota).
"""


class ContoBancario:
    def __init__(self, titolare, saldo_iniziale=0.0):
        # attributi "privati" 
        self.__titolare = ""
        self.__saldo = 0.0

        # uso il setter per validare subito
        self.set_titolare(titolare)

        # saldo iniziale valido (solo se numero e >= 0)
        if (type(saldo_iniziale) == int or type(saldo_iniziale) == float) and saldo_iniziale >= 0:
            self.__saldo = float(saldo_iniziale)

    #  GETTER / SETTER 
    def get_titolare(self):
        return self.__titolare

    def set_titolare(self, nuovo_titolare):
        # versione semplificata: controlliamo solo che sia stringa e non vuota
        if type(nuovo_titolare) == str and nuovo_titolare != "":
            self.__titolare = nuovo_titolare
        else:
            print("Errore: titolare non valido")

    def visualizza_saldo(self):
        # getter del saldo (solo lettura)
        return self.__saldo

    #  metodi
    def deposita(self, importo):
        # controlli: numero e positivo
        if type(importo) != int and type(importo) != float:
            print("Errore: importo non valido")
            return False

        if importo > 0:
            self.__saldo = self.__saldo + float(importo)
            print("Deposito OK. Nuovo saldo:", self.__saldo)
            return True
        else:
            print("Errore: importo non valido")
            return False

    def preleva(self, importo):
        # controlli: numero, positivo, fondi sufficienti
        if type(importo) != int and type(importo) != float:
            print("Errore: importo non valido")
            return False

        importo = float(importo)

        if importo <= 0:
            print("Errore: importo non valido")
            return False
        elif importo > self.__saldo:
            print("Errore: fondi insufficienti")
            return False
        else:
            self.__saldo = self.__saldo - importo
            print("Prelievo OK. Nuovo saldo:", self.__saldo)
            return True


class Utente:
    def __init__(self, username):
        # attributo PROTETTO (convenzione)
        self._username = username


class Cliente(Utente):
    # Cliente può vedere e modificare il conto
    def __init__(self, username, conto):
        super().__init__(username)
        self._conto = conto

    def mostra_conto(self):
        print("Titolare:", self._conto.get_titolare())
        print("Saldo:", self._conto.visualizza_saldo())

    def deposita(self, importo):
        self._conto.deposita(importo)

    def preleva(self, importo):
        self._conto.preleva(importo)

    def cambia_titolare(self, nuovo_titolare):
        self._conto.set_titolare(nuovo_titolare)


class Admin(Utente):
    # Admin può solo vedere il conto
    def __init__(self, username, conto):
        super().__init__(username)
        self._conto = conto

    def mostra_conto(self):
        print("Titolare:", self._conto.get_titolare())
        print("Saldo:", self._conto.visualizza_saldo())


# main

print("=== BANCA ===")

conto = ContoBancario("Ilaria", 50)

cliente = Cliente("cliente01", conto)
admin = Admin("admin01", conto)

stop = False
utente_attivo = None

while not stop:

    # login
    if utente_attivo == None:
        print("\n--- LOGIN ---")
        print("1) Entra come Cliente")
        print("2) Entra come Admin")
        print("0) Esci")
        scelta = input("Scelta: ")

        match scelta:
            case "1":
                utente_attivo = cliente
                print("Login effettuato come CLIENTE.")
            case "2":
                utente_attivo = admin
                print("Login effettuato come ADMIN.")
            case "0":
                print("Uscita.")
                stop = True
            case _:
                print("Scelta non valida.")
        continue

    # menu naviazione
    print("\n--- MENU ---")
    print("1) Visualizza conto")

    if type(utente_attivo) == Cliente:
        print("2) Deposita")
        print("3) Preleva")
        print("4) Cambia titolare")
        print("9) Logout")
        print("0) Esci")

        scelta = input("Scelta: ")

        match scelta:
            case "1":
                utente_attivo.mostra_conto()

            case "2":
                importo = float(input("Importo da depositare: "))
                utente_attivo.deposita(importo)

            case "3":
                importo = float(input("Importo da prelevare: "))
                utente_attivo.preleva(importo)

            case "4":
                nuovo = input("Nuovo titolare: ")
                utente_attivo.cambia_titolare(nuovo)

            case "9":
                utente_attivo = None
                print("Logout effettuato.")

            case "0":
                print("Uscita.")
                stop = True

            case _:
                print("Scelta non valida.")

    else:
        # se sei admin, puoi solo visualizzare il conto
        print("9) Logout")
        print("0) Esci")

        scelta = input("Scelta: ")

        match scelta:
            case "1":
                utente_attivo.mostra_conto()

            case "9":
                utente_attivo = None
                print("Logout effettuato.")

            case "0":
                print("Uscita.")
                stop = True

            case _:
                print("Scelta non valida.")
