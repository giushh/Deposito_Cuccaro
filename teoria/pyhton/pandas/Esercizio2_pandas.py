"""
Esercizio 2: Manipolazione e Aggregazione dei Dati

Obiettivo: Approfondire le capacità di manipolazione e aggregazione dei dati con pandas.

Dataset: Utilizzare un dataset che registra le vendite di prodotti in diverse città,
includendo le colonne Prodotto, Quantità, Prezzo Unitario e Città.

1. Caricare i dati in un DataFrame.
2. Aggiungere una colonna "Totale Vendite" che sia il risultato del prodotto tra Quantità e Prezzo Unitario.
3. Raggruppare i dati per Prodotto e calcolare il totale delle vendite per ciascun prodotto.
4. Trovare il prodotto più venduto in termini di Quantità.
5. Identificare la città con il maggior volume di vendite totali.
6. Creare un nuovo DataFrame che mostri solo le vendite superiori a un certo valore (es. 1000 euro).
7. Ordinare il DataFrame originale per la colonna "Totale Vendite" in ordine decrescente.
8. Visualizzare il numero di vendite per ogni città.
"""

import pandas as pd

nome_file = r"Corso_Python\25_02_2026\pomeriggio\vendite.csv"

print("****** Esercizio 2 - Manipolazione e Aggregazione dei Dati ******")

def crea_dataset():
    # 1
    dati = {
        "Prodotto": ["Computer", "Smartphone", "Tablet", "Monitor", "Mouse", "Computer"],
        "Quantità": [25, 40, 35, 15, 80, 30],
        "Prezzo Unitario": [900, 500, 300, 200, 40, 900],
        "Città": ["Roma", "Milano", "Napoli", "Roma", "Milano", "Napoli"]
    }

    df = pd.DataFrame(dati)
    # crea un dataframe a partire da un dizionario

    return df


def salva_csv(df):
    df.to_csv(nome_file, index=False)
    # salva il dataframe in formato csv


def aggiungi_totale_vendite(df):
    # 2
    df["Totale Vendite"] = df["Quantità"] * df["Prezzo Unitario"]
    return df


def totale_per_prodotto(df):
    # 3
    risultato = df.groupby("Prodotto")["Totale Vendite"].sum()
    # raggruppa le righe per prodotto e somma i valori della colonna totale vendite
    return risultato


def prodotto_piu_venduto(df):
    # 4
    quantita = df.groupby("Prodotto")["Quantità"].sum()
    # raggruppa per prodotto e somma le quantità
    return quantita.idxmax()
    # restituisce id con il valore massimo


def citta_maggiori_vendite(df):
    # 5
    totale = df.groupby("Città")["Totale Vendite"].sum()
    # raggruppa per città e somma le vendite totali
    return totale.idxmax()


def vendite_superiori_soglia(df, soglia):
    # 6
    filtrato = df[df["Totale Vendite"] > soglia]
    # seleziona solo le righe che rispettano la condizione
    return filtrato


def ordina_per_totale(df):
    # 7
    ordinato = df.sort_values(by="Totale Vendite", ascending=False)
    # ordina il dataframe in base a una colonna in ordine decrescente (crescente false)
    return ordinato


def numero_vendite_per_citta(df):
    # 8
    conteggio = df["Città"].value_counts()
    # conta quante volte appare ogni valore nella colonna città
    return conteggio



df = crea_dataset()

print("\nDataset iniziale:")
print(df)

df = aggiungi_totale_vendite(df)

salva_csv(df)

print("\nDataFrame con Totale Vendite:")
print(df)

print("\nTotale vendite per prodotto:")
print(totale_per_prodotto(df))

print("\nProdotto più venduto (per quantità):")
print(prodotto_piu_venduto(df))

print("\nCittà con maggior volume di vendite:")
print(citta_maggiori_vendite(df))

print("\nVendite superiori a 1000 euro:")
print(vendite_superiori_soglia(df, 1000))

print("\nDataFrame ordinato per Totale Vendite (decrescente):")
print(ordina_per_totale(df))

print("\nNumero di vendite per città:")
print(numero_vendite_per_citta(df))