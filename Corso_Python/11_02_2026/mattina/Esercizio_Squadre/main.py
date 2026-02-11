# mattina 11/02/2026

"""
Creare una classe padre Membro squadra e una Squadra che conterrà le diverse classi figlie che rappresentano ruoli specifici 
all'interno della squadra di calcio, come Giocatore, Allenatore, Assistente

classe MembroSquadra:
    Attributi:
    nome (stringa)
    età (intero)
    Metodi:
    descrivi() (stampa una descrizione generale del membro della squadra)
    
Classi Derivate:

Giocatore:
    Attributi aggiuntivi come ruolo (e.g., attaccante, difensore) e numero_maglia
    Metodi come gioca_partita() che possono includere azioni specifiche del giocatore
Allenatore:
    Attributi aggiuntivi come anni_di_esperienza
    Metodi come dirige_allenamento() che dettagliano come l'allenatore conduce gli allenamenti
Assistente:
    Attributi aggiuntivi come specializzazione (e.g., fisioterapista, analista di gioco)
    Metodi specifici del ruolo, come supporta_team() che può descrivere varie forme di supporto al team

Crea due squadre e falle giocare contro.

SPECIALIZZAZIONE:
-- Masterchef - Gara a squadre
Ogni squadra deve preparare un menù completo composto da quattro portate: antipasto, primo, secondo e dolce.
Ogni squadra è formata da diversi membri con ruoli differenti. 
Tutti derivano da una classe base comune, che contiene le informazioni generali (come nome ed età), 
mentre le classi derivate rappresentano i ruoli specifici all’interno della brigata di cucina. 
I giocatori sono specializzati in una determinata portata, mentre l’allenatore e gli assistenti 
svolgono funzioni di supporto e coordinamento.

La partita si svolge in più fasi, una per ogni portata del menù. 
In ciascuna fase, il membro incaricato prepara il piatto e il risultato dipende dal suo livello di esperienza 
nella categoria assegnata. Al termine delle prove, si confrontano i risultati ottenuti dalle due squadre 
e viene dichiarata vincitrice quella che ha ottenuto le prestazioni migliori complessive.

"""


from membri import (
    Squadra,
    CuocoAntipasti, CuocoPrimi, CuocoSecondi, Pasticcere,
    Allenatore, Assistente,
    CategoriaAntipasti, CategoriaPrimi, CategoriaSecondi, CategoriaDolci
)

def crea_esperienza(antipasti, primi, secondi, dolci):
    # l'esperienza in ogni categoria va da 1 a 5
    return {
        "antipasti": antipasti,
        "primi": primi,
        "secondi": secondi,
        "dolci": dolci
    }

print("=== MASTERCHEF: Gara a squadre ===\n")

# Creazione squadre
squadra1 = Squadra("Squadra Rossa")
squadra2 = Squadra("Squadra Blu")

# --- Squadra 1 ---
squadra1.aggiungi_membro(Allenatore("Chef Marco", 45, 15))
squadra1.aggiungi_membro(Assistente("Giulia", 29, "Dispensa/Logistica"))
squadra1.aggiungi_membro(CuocoAntipasti("Luca", 26, crea_esperienza(5, 2, 2, 1)))
squadra1.aggiungi_membro(CuocoPrimi("Sara", 30, crea_esperienza(2, 5, 3, 2)))
squadra1.aggiungi_membro(CuocoSecondi("Paolo", 33, crea_esperienza(2, 3, 5, 1)))
squadra1.aggiungi_membro(Pasticcere("Anna", 24, crea_esperienza(1, 2, 2, 5)))
# AGGIUNGI ALTRI MEMBRI PER AVERE PIU SCELTA
# --- Squadra 2  ---
squadra2.aggiungi_membro(Allenatore("Chef Elena", 41, 12))
squadra2.aggiungi_membro(Assistente("Davide", 31, "Impiattamento"))
squadra2.aggiungi_membro(CuocoAntipasti("Marta", 27, crea_esperienza(4, 2, 2, 2)))
squadra2.aggiungi_membro(CuocoPrimi("Nico", 28, crea_esperienza(2, 4, 3, 2)))
squadra2.aggiungi_membro(CuocoSecondi("Francesco", 35, crea_esperienza(2, 3, 4, 1)))
squadra2.aggiungi_membro(Pasticcere("Chiara", 23, crea_esperienza(1, 2, 2, 4)))

stop = False
while not stop:
    print("\n--- MENU ---")
    print("1) Mostra squadre")
    print("2) Sfida (selezione portate)")
    print("0) Esci")
    scelta = input("Scelta: ").strip()

    match scelta:
        case "1":
            squadra1.descrivi_squadra()
            squadra2.descrivi_squadra()
        
        case "2":
            print("\n== Selezione giocatori per portata ==")

            categorie = [CategoriaAntipasti, CategoriaPrimi, CategoriaSecondi, CategoriaDolci]
            for cat in categorie:
                print(f"\nPortata: {cat.label().upper()}")
                _g1 = squadra1.seleziona_giocatore_per_categoria(cat)
                _g2 = squadra2.seleziona_giocatore_per_categoria(cat)
        
        case "3":
            print("Uscita.")
            stop = True
        
        case _:
            print("Scelta non valida. Riprova")
            continue 