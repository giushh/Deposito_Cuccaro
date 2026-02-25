"""
Esercizio 1: Analisi Esplorativa dei Dati con Pandas

Obiettivo:
Familiarizzare con le operazioni di base per l'esplorazione dei dati usando pandas.

Dataset:
Creare un dataset con le seguenti colonne:
- Nome
- Età
- Città
- Salario

Operazioni richieste:
1. Generare casualmente i dati (almeno 20 righe) e caricarli in un DataFrame.
2. Visualizzare le prime e ultime cinque righe.
3. Visualizzare il tipo di dati di ciascuna colonna.
4. Calcolare statistiche descrittive di base per le colonne numeriche.
5. Identificare e rimuovere eventuali duplicati.
6. Gestire i valori mancanti come da esempio docente:
   - Rimuovere le righe con almeno un valore mancante (dropna).
   - Sostituire i valori mancanti nelle colonne numeriche con la media (fillna con inplace=True).
   Nota: per lavorare sempre sullo stesso dataset, dopo dropna riassegniamo df = df.dropna()
7. Aggiungere una colonna "Categoria Età".
8. Salvare il DataFrame pulito in un file CSV.
"""

import pandas as pd
import numpy as np
import random


def genera_dataset():
    nomi_possibili = [
        "Luca", "Marco", "Giulia", "Anna", "Paolo", "Francesca",
        "Giorgio", "Elena", "Davide", "Sara", "Matteo", "Chiara",
        "Simone", "Laura", "Andrea", "Valentina", "Stefano", "Marta",
        "Alessio", "Federica", "Roberto", "Ilaria"
    ]

    citta_possibili = [
        "Napoli", "Roma", "Milano", "Torino", "Bologna",
        "Firenze", "Bari", "Genova"
    ]

    dati = {
        "Nome": [],
        "Età": [],
        "Città": [],
        "Salario": []
    }

    for _ in range(25):  # almeno 20 righe
        dati["Nome"].append(random.choice(nomi_possibili))
        dati["Età"].append(random.randint(15, 80))
        dati["Città"].append(random.choice(citta_possibili))
        dati["Salario"].append(random.randint(18000, 60000))

    # valori mancanti volutamente 
    dati["Nome"][2] = None
    dati["Età"][5] = np.nan
    dati["Salario"][7] = np.nan

    # valori duplicati volutamente 
    dati["Nome"].append(dati["Nome"][0])
    dati["Età"].append(dati["Età"][0])
    dati["Città"].append(dati["Città"][0])
    dati["Salario"].append(dati["Salario"][0])

    return dati


def crea_dataframe(dizionario):
    return pd.DataFrame(dizionario)


def visualizza_prime_ultime(df):
    print("\nPrime 5 righe:")
    print(df.head())

    print("\nUltime 5 righe:")
    print(df.tail())


def visualizza_tipi_dati(df):
    print("\nTipi di dato:")
    print(df.dtypes)


def statistiche_descrittive(df):
    print("\nStatistiche descrittive:")
    print(df.describe())


def classifica(eta):
    if eta <= 18:
        return "Giovane"
    elif eta <= 65:
        return "Adulto"
    else:
        return "Senior"


def pulisci_dataset(df):
    # rimozione duplicati
    df = df.drop_duplicates()

    # rimozione righe con almeno un valore mancante (come esempio docente)
    df = df.dropna()

    # sostituzione mancanti con media 
    df["Età"].fillna(df["Età"].mean(), inplace=True)
    df["Salario"].fillna(df["Salario"].mean(), inplace=True)


    return df


def aggiungi_categoria_eta(df):
    df["Categoria Età"] = df["Età"].apply(classifica)
    return df


def salva_csv(df, nome_file=r"Corso_Python\25_02_2026\mattina\dataset_pulito.csv"):
    df.to_csv(nome_file, index=False)
    print(f"\nFile salvato come {nome_file}")


def main():
    dizionario = genera_dataset()
    df = crea_dataframe(dizionario)

    print("DataFrame Originale:")
    print(df)

    visualizza_prime_ultime(df)
    visualizza_tipi_dati(df)
    statistiche_descrittive(df)

    df = pulisci_dataset(df)
    df = aggiungi_categoria_eta(df)

    print("\nDataFrame Pulito (+ Categoria Età):")
    print(df)

    salva_csv(df)


if __name__ == "__main__":
    main()