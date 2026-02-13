
from utenti import Badge, Dipendente, Responsabile
from controlli import RegistroAccessi, ControlloAccessi


def scegli_utente(utenti: list):
    """
    fa scegliere all'utente quale profilo usare
    ritorna l'oggetto Utente selezionato.
    """
    if not utenti:
        print("\nNessun utente disponibile.")
        return None

    print("\n--- Seleziona utente ---")         # stampa utenti
    for i, u in enumerate(utenti, start=1):
        print(f"{i}. {u.get_nome()} ({u.descrivi_ruolo()})")

    scelta = input("\nNumero utente: ")

    if scelta.isdigit():
        indice = int(scelta) - 1
        if 0 <= indice < len(utenti):
            return utenti[indice]

    print("\nScelta non valida.")
    return None


def main():
    
    # badge e utenti predefiniti
    badge1 = Badge("B-100")
    badge2 = Badge("B-200")
    badge3 = Badge("B-300")
    badge4 = Badge("B-400")
    badge5 = Badge("B-500")

    utenti = [
        Dipendente("U-1", "Mario", badge1, "Magazzino"),
        Responsabile("U-2", "Anna", badge2, "IT"),
        Dipendente("U-3", "Luca", badge3, "Produzione"),
        Dipendente("U-4", "Giulia", badge4, "Amministrazione"),
        Responsabile("U-5", "Paolo", badge5, "Risorse Umane")
    ]

    registro = RegistroAccessi()
    controllo = ControlloAccessi(registro)

    stop = False
    while not stop:
        scelta = input("\nPuoi:"
                       "\n1. Entra (badge)"
                       "\n2. Esci (badge)"
                       "\n3. Vai in bagno"
                       "\n4. Mostra log"
                       "\n5. Disattiva badge"
                       "\n6. Attiva badge"
                       "\n7. Stato badge"
                       "\n8. Uscita"
                       "\nIndica il numero corrispondente \n> ")

        match scelta:
            case "1":
                utente = scegli_utente(utenti)
                if utente is not None:
                    controllo.entra(utente)

            case "2":
                utente = scegli_utente(utenti)
                if utente is not None:
                    controllo.esci(utente)

            case "3":
                utente = scegli_utente(utenti)
                if utente is not None:
                    controllo.vai_in_bagno(utente)

            case "4":
                registro.mostra_eventi()

            case "5":
                utente = scegli_utente(utenti)
                if utente is not None:
                    utente.get_badge().disattiva()
                    print("\nBadge disattivato.")

            case "6":
                utente = scegli_utente(utenti)
                if utente is not None:
                    utente.get_badge().attiva()
                    print("\nBadge attivato.")

            case "7":
                utente = scegli_utente(utenti)
                if utente is not None:
                    badge = utente.get_badge()
                    stato = "ATTIVO" if badge.is_attivo() else "NON ATTIVO"
                    print(f"\nBadge {badge.get_codice()} -> {stato}")

            case "8":
                print("\n-- Uscita")
                stop = True

            case _:
                print("\nComando non valido. \nRiprova.")
                continue


if __name__ == "__main__":
    main()