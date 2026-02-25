"""
Obiettivo: Utilizzare pandas per analizzare un set di dati di vendite generato casualmente, applicando le tecniche di pivot e groupby.

Descrizione:
Gli studenti dovranno generare un DataFrame di vendite che include i seguenti campi:
"Data", "Città", "Prodotto" e "Vendite".
I dati devono essere generati per un periodo di un mese, con vendite registrate per tre diverse città e tre tipi di prodotti.

1. Generazione dei Dati: Utilizzare numpy per creare un set di dati casuali.
2. Creazione della Tabella Pivot: Creare una tabella pivot per analizzare le vendite medie di ciascun prodotto per città.
3. Applicazione di GroupBy: Utilizzare il metodo groupby per calcolare le vendite totali per ogni prodotto.
"""

import pandas as pd
import numpy as np


print("****** Esercizio 1 - Pivot e groupby vendite *****")
# 1
date = pd.date_range(start="2026-02-01", periods=28, freq="D")  # crea una sequenza di date consecutive
citta = ["Roma", "Milano", "Napoli"]
prodotti = ["A", "B", "C"]

n_date = len(date)
n_citta = len(citta)
n_prodotti = len(prodotti)
righe = n_date * n_citta * n_prodotti

colonna_date = np.repeat(date, n_citta * n_prodotti)  # ripete ogni data per coprire tutte le combinazioni città/prodotto
colonna_citta = np.tile(np.repeat(citta, n_prodotti), n_date)  # costruisce il pattern delle città ripetuto per ogni giorno
colonna_prodotti = np.tile(prodotti, n_date * n_citta)  # ripete i prodotti per tutte le città e tutti i giorni
colonna_vendite = np.random.randint(10, 201, size=righe)  # genera vendite casuali intere in un intervallo

df = pd.DataFrame({
    "Data": colonna_date,
    "Città": colonna_citta,
    "Prodotto": colonna_prodotti,
    "Vendite": colonna_vendite
})  # crea un dataframe a partire da colonne già pronte

print("\n--- DataFrame vendite (prime 10 righe) ---")
print(df.head(10))  # mostra le prime righe per controllare velocemente i dati


# 2
tabella_pivot = df.pivot_table(
    values="Vendite",
    index="Prodotto",
    columns="Città",
    aggfunc="mean"
)  # crea una tabella riassuntiva incrociando righe/colonne e aggregando i valori

print("\n--- Tabella pivot: vendite medie per prodotto e città ---")
print(tabella_pivot)


# 3
vendite_totali_prodotto = df.groupby("Prodotto")["Vendite"].sum()  # raggruppa per prodotto e somma le vendite

print("\n--- Groupby: vendite totali per prodotto ---")
print(vendite_totali_prodotto)