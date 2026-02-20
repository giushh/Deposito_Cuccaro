"""
Create un programma python utilizzando le api
https://pokeapi.co/api/v2/pokemon/ {numero} che simula un
pokedex, quando troverete un pokemon in maniera randomica
verificherà se è presente nel vostro pokedex (pokedex.json),
in caso non fosse presente vi permetterà di catturarlo 
salvando le caratteristiche.
(Sul sistema API sono presenti 1025 pokemon)
"""

import requests as r
import json as j
import random as rd

FILE_NAME = r"Corso_Python\20_02_2026\mattina\pokedex.json"
# r davanti alla stringa: Python non interpreta i backslash come escape


# creazione/aggiornamento del pokedex (scrittura su file)
def write_pokedex(pokedex):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        j.dump(pokedex, f, indent=4, ensure_ascii=False)


# lettura del pokedex (dal file)
def read_pokedex():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return j.load(f)
    except FileNotFoundError:
        return []
    except j.JSONDecodeError:
        # se il file esiste ma è corrotto/vuoto
        return []


# aggiunta di un pokemon al pokedex (append + save)
def append_pokedex(pokemon_entry):
    current_pokedex = read_pokedex()
    current_pokedex.append(pokemon_entry)
    write_pokedex(current_pokedex)


# estrazione di un pokemon randomico (1..1025)
def random_pokemon():
    return rd.randint(1, 1025)


# recupero info del pokemon tramite API
def get_pokemon(num):
    url = f"https://pokeapi.co/api/v2/pokemon/{num}"
    try:
        response = r.get(url, timeout=10)
        response.raise_for_status()
    except r.exceptions.RequestException as e:
        print(f"Errore nella richiesta: {e}")
        return None
    return response.json()


# testa o croce: 1 = catturato, 0 = scappato
def testa_croce():
    return rd.choice([1, 0])


# controlla se il pokemon (num) è già presente nel pokedex
def check_pokedex(pokedex_list, num):
    for entry in pokedex_list:
        if entry.get("id") == num:
            return True
    return False


# stampa semplice di una entry salvata (entry è un dict)
def print_entry(entry):
    print(f"\nID: {entry.get('id')}  Nome: {entry.get('nome')}")
    print(f"Tipi: {', '.join(entry.get('tipi', []))}")
    print(f"Altezza: {entry.get('altezza')}  Peso: {entry.get('peso')}")
    stats = entry.get("stats", {})
    if stats:
        print("Stats:", ", ".join([f"{k}={v}" for k, v in stats.items()]))


# crea la struttura da salvare nel pokedex.json, prendendo solo campi utili
def build_entry_from_api(data):
    tipi = []
    for t in data.get("types", []):
        # t["type"]["name"]
        tipi.append(t.get("type", {}).get("name", "unknown"))
        # le {} e "unknown" sono valori di default se la get non ritorna nulla, per evitare errori bloccanti


    stats = {}
    for s in data.get("stats", []):
        nome_stat = s.get("stat", {}).get("name", "unknown")
        valore = s.get("base_stat", 0)
        stats[nome_stat] = valore

    entry = {
        "id": data.get("id"),
        "nome": data.get("name"),
        "tipi": tipi,
        "altezza": data.get("height"),
        "peso": data.get("weight"),
        "stats": stats
    }
    return entry


def stampa_pokedex():
    pokedex = read_pokedex()
    if not pokedex:
        print("\nPokedex vuoto.")
        return

    print("\n--- IL TUO POKEDEX ---")
    for entry in pokedex:
        print(f"- [{entry.get('id')}] {entry.get('nome')} ({', '.join(entry.get('tipi', []))})")
    print(f"Totale catturati: {len(pokedex)}")


def esplora_e_cattura(num):
    pokedex = read_pokedex()

    data = get_pokemon(num)
    if data is None:
        return

    print(f"\nHai incontrato: #{data.get('id')} {data.get('name')}")

    if check_pokedex(pokedex, num):
        print("È già presente nel tuo Pokedex")
        return

    scelta = input("Non è nel Pokedex. Vuoi provare a catturarlo? (s/n)\n> ")
    if scelta.lower() != "s":
        print("Ok, lo lasci andare.")
        return

    esito = testa_croce()
    if esito == 1:
        print("Cattura riuscita!")
        entry = build_entry_from_api(data)
        append_pokedex(entry)
        print_entry(entry)
    else:
        print("Oh no... è scappato!")


def main():
    stop = False
    while not stop:
        scelta = input(
            "\n--- POKEDEX ---"
            "\nPuoi:"
            "\n1. Incontra un Pokemon random"
            "\n2. Mostra il tuo Pokedex"
            "\n3. Cerca/Incontra un Pokemon per numero"
            "\n4. Uscita"
            "\nIndica il numero corrispondente\n> "
        )

        match scelta:
            case "1":
                num = random_pokemon()
                esplora_e_cattura(num)

            case "2":
                stampa_pokedex()

            case "3":
                num_str = input("Inserisci il numero del Pokemon (1 - 1025)\n> ")
                if not num_str.isdigit():
                    print("Devi inserire un numero.")
                    continue
                num = int(num_str)
                if num < 1 or num > 1025:
                    print("Numero fuori range (1 - 1025).")
                    continue
                esplora_e_cattura(num)

            case "4":
                print("\n-- Uscita")
                stop = True

            case _:
                print("\nComando non valido.\nRiprova.")
                continue


if __name__ == "__main__":
    main()