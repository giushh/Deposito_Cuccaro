#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PANDAS - PANORAMICA COMPLETA (unico file, esempi pratici)

Contenuti:
1) Series e DataFrame
2) Lettura/scrittura CSV (demo in memoria)
3) Selezione: colonne, loc, iloc
4) Filtri booleani
5) Nuove colonne (operazioni vettoriali)
6) Missing values (NaN): isna, fillna, dropna
7) groupby + aggregazioni
8) sort_values + value_counts
9) merge (join) tra DataFrame
10) DateTime: to_datetime, set_index, resample
"""

import pandas as pd
import numpy as np
from io import StringIO


# ==============================================================
# 1) SERIES E DATAFRAME
# ==============================================================

print("=== 1) Series e DataFrame ===")

s = pd.Series([10, 20, 30], name="punti")
print("Series:\n", s, "\n")

df = pd.DataFrame({
    "nome": ["Anna", "Luca", "Marco", "Sara"],
    "eta":  [25, 40, 30, 22],
    "citta": ["Milano", "Roma", "Napoli", "Milano"],
    "spesa": [50.5, 120.0, 80.0, 30.0]
})

print("DataFrame:\n", df, "\n")


# ==============================================================
# 2) LETTURA/SCRITTURA CSV (IN MEMORIA)
# ==============================================================

print("=== 2) CSV in memoria (StringIO) ===")

buffer = StringIO()
df.to_csv(buffer, index=False)     # scrivo CSV in memoria
buffer.seek(0)                     # torno all'inizio del buffer
df_csv = pd.read_csv(buffer)       # leggo CSV dal buffer

print("Riletto da CSV:\n", df_csv, "\n")


# ==============================================================
# 3) SELEZIONE: COLONNE, loc, iloc
# ==============================================================

print("=== 3) Selezione dati ===")

print("Colonna 'nome':\n", df["nome"], "\n")

print("loc (riga per etichetta): df.loc[1]:\n", df.loc[1], "\n")

print("iloc (riga per posizione): df.iloc[0]:\n", df.iloc[0], "\n")

print("Sottotabella (righe 0-2, colonne 0-2):\n", df.iloc[0:3, 0:3], "\n")


# ==============================================================
# 4) FILTRI BOOLEANI
# ==============================================================

print("=== 4) Filtri booleani ===")

filtro_milano = df["citta"] == "Milano"
print("Solo Milano:\n", df[filtro_milano], "\n")

filtro_eta = df["eta"] >= 30
print("Età >= 30:\n", df[filtro_eta], "\n")

filtro_combinato = (df["citta"] == "Milano") & (df["spesa"] > 40)
print("Milano e spesa > 40:\n", df[filtro_combinato], "\n")


# ==============================================================
# 5) NUOVE COLONNE (OPERAZIONI VETTORIALI)
# ==============================================================

print("=== 5) Nuove colonne ===")

df["spesa_iva"] = df["spesa"] * 1.22  # esempio: IVA 22%
df["maggiorenne"] = df["eta"] >= 18

print(df, "\n")


# ==============================================================
# 6) MISSING VALUES (NaN)
# ==============================================================

print("=== 6) Missing values (NaN) ===")

df_nan = df.copy()
df_nan.loc[2, "spesa"] = np.nan          # imposto un NaN
print("Con NaN:\n", df_nan, "\n")

print("isna (dove sono NaN):\n", df_nan.isna(), "\n")

print("Conteggio NaN per colonna:\n", df_nan.isna().sum(), "\n")

# fillna: sostituisco NaN con la media della colonna
media_spesa = df_nan["spesa"].mean()
df_nan["spesa"] = df_nan["spesa"].fillna(media_spesa)
print("Dopo fillna con media:\n", df_nan, "\n")

# dropna: elimina righe con NaN (qui non ne restano)
df_drop = df.copy()
df_drop.loc[1, "citta"] = np.nan
print("Prima dropna:\n", df_drop, "\n")
print("Dopo dropna:\n", df_drop.dropna(), "\n")


# ==============================================================
# 7) GROUPBY + AGGREGAZIONI
# ==============================================================

print("=== 7) GroupBy e aggregazioni ===")

group = df.groupby("citta")["spesa"].agg(["count", "mean", "sum", "max"])
print(group, "\n")


# ==============================================================
# 8) SORT + VALUE_COUNTS
# ==============================================================

print("=== 8) Sort e value_counts ===")

print("Ordinato per spesa decrescente:\n", df.sort_values("spesa", ascending=False), "\n")

print("Conteggio città:\n", df["citta"].value_counts(), "\n")


# ==============================================================
# 9) MERGE (JOIN)
# ==============================================================

print("=== 9) Merge (join) ===")

df_lavori = pd.DataFrame({
    "nome": ["Anna", "Luca", "Sara"],
    "lavoro": ["Dev", "PM", "Designer"]
})

merged = pd.merge(df, df_lavori, on="nome", how="left")
print("Merge left (aggiunge lavoro quando presente):\n", merged, "\n")


# ==============================================================
# 10) DATETIME: to_datetime, set_index, resample
# ==============================================================

print("=== 10) DateTime e resample ===")

df_time = pd.DataFrame({
    "data": pd.date_range("2025-01-01", periods=10, freq="D"),
    "vendite": [5, 7, 3, 9, 2, 4, 6, 8, 1, 10]
})

df_time["data"] = pd.to_datetime(df_time["data"])
df_time = df_time.set_index("data")

print("Dati con index datetime:\n", df_time, "\n")

# resample settimanale (W) con somma
weekly = df_time.resample("W").sum()
print("Resample settimanale (somma vendite):\n", weekly, "\n")


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PANDAS AVANZATO (unico file copiabile)
- GroupBy (multi-chiave, agg, transform)
- Pivot / Pivot_table (anche multi-index)
- Gestione del tempo (datetime, resample, rolling, shift, tz)
- Indicizzazione avanzata (loc/iloc, MultiIndex, slice, query, mask, xs)

Esecuzione:
python pandas_avanzato.py
"""


pd.set_option("display.width", 140)
pd.set_option("display.max_columns", 50)


# ==============================================================
# 0) DATASET DI ESEMPIO
# ==============================================================

# Creiamo un dataset "vendite" realistico con date, negozi, categorie, prodotto, quantità e prezzo
rng = pd.date_range("2025-01-01", periods=120, freq="D")
np.random.seed(42)

df = pd.DataFrame({
    "data": np.random.choice(rng, size=600, replace=True),
    "negozio": np.random.choice(["Genova", "Milano", "Roma"], size=600),
    "categoria": np.random.choice(["Tech", "Food", "Casa"], size=600),
    "prodotto": np.random.choice(["A", "B", "C", "D"], size=600),
    "qta": np.random.randint(1, 6, size=600),
    "prezzo": np.round(np.random.uniform(2.5, 120.0, size=600), 2)
})

# Fatturato riga per riga
df["totale"] = df["qta"] * df["prezzo"]

# Converto la colonna data in datetime (di solito è già datetime, ma lo facciamo esplicito)
df["data"] = pd.to_datetime(df["data"])

print("=== DATASET (prime 5 righe) ===")
print(df.head(), "\n")


# ==============================================================
# 1) GROUPBY: aggregazioni, multi-chiave, agg avanzate
# ==============================================================

print("=== 1) GROUPBY base: per negozio (sum/mean/max) ===")
g1 = df.groupby("negozio")["totale"].agg(["count", "sum", "mean", "max"]).round(2)
print(g1, "\n")

print("=== 1b) GROUPBY multi-chiave: negozio + categoria ===")
g2 = df.groupby(["negozio", "categoria"])["totale"].agg(["sum", "mean"]).round(2)
print(g2.head(12), "\n")

print("=== 1c) GROUPBY con più colonne e agg con nomi custom ===")
g3 = df.groupby("categoria").agg(
    righe=("totale", "count"),
    fatturato=("totale", "sum"),
    qta_tot=("qta", "sum"),
    prezzo_medio=("prezzo", "mean")
).round(2)
print(g3, "\n")


# ==============================================================
# 2) GROUPBY + transform (feature per riga) e rank
# ==============================================================

print("=== 2) GROUPBY + transform: quota sul totale del negozio ===")
df["totale_negozio"] = df.groupby("negozio")["totale"].transform("sum")
df["quota_su_negozio"] = (df["totale"] / df["totale_negozio"]).round(6)

print(df[["negozio", "categoria", "totale", "totale_negozio", "quota_su_negozio"]].head(), "\n")

print("=== 2b) Rank: classifica fatturato per negozio (riga) ===")
df["rank_in_negozio"] = df.groupby("negozio")["totale"].rank(ascending=False, method="dense")
print(df[["negozio", "totale", "rank_in_negozio"]].head(), "\n")


# ==============================================================
# 3) PIVOT e PIVOT_TABLE
# ==============================================================

print("=== 3) PIVOT: totale per data x negozio (attenzione: pivot richiede chiavi uniche) ===")

# Per pivot usiamo un dataset aggregato (chiavi uniche), altrimenti pivot esplode
daily_store = df.groupby(["data", "negozio"], as_index=False)["totale"].sum()

pivot1 = daily_store.pivot(index="data", columns="negozio", values="totale").fillna(0).round(2)
print("Pivot (prime 5 righe):\n", pivot1.head(), "\n")

print("=== 3b) PIVOT_TABLE: totale medio per negozio x categoria ===")
pivot2 = pd.pivot_table(
    df,
    index="negozio",
    columns="categoria",
    values="totale",
    aggfunc="mean",
    fill_value=0
).round(2)
print(pivot2, "\n")

print("=== 3c) PIVOT_TABLE con multi-index: negozio x categoria, colonne=prodotto ===")
pivot3 = pd.pivot_table(
    df,
    index=["negozio", "categoria"],
    columns="prodotto",
    values="totale",
    aggfunc="sum",
    fill_value=0
).round(2)
print(pivot3.head(12), "\n")


# ==============================================================
# 4) GESTIONE DEL TEMPO: set_index, resample, rolling, shift, period
# ==============================================================

print("=== 4) TIME: resample settimanale per negozio ===")

# Mettiamo la data come index per lavorare meglio con resample
ts = daily_store.set_index("data")

# Resample settimanale: somma per negozio
weekly = ts.groupby("negozio")["totale"].resample("W").sum().round(2)
print("Weekly (prime righe):\n", weekly.head(10), "\n")

print("=== 4b) TIME: rolling (media mobile 7 giorni) sul totale giornaliero di un negozio ===")
genova_daily = pivot1["Genova"]  # Serie indicizzata per data
rolling7 = genova_daily.rolling(window=7).mean().round(2)
print(pd.DataFrame({"Genova_tot": genova_daily.head(12), "Genova_roll7": rolling7.head(12)}), "\n")

print("=== 4c) TIME: shift (valore giorno precedente) e variazione % ===")
prev = genova_daily.shift(1)
pct = ((genova_daily - prev) / prev * 100).replace([np.inf, -np.inf], np.nan).round(2)
print(pd.DataFrame({"oggi": genova_daily.head(10), "ieri": prev.head(10), "var_%": pct.head(10)}), "\n")

print("=== 4d) TIME: PeriodIndex (raggruppo per mese) ===")
df["mese"] = df["data"].dt.to_period("M")
per_mese = df.groupby(["mese", "negozio"])["totale"].sum().round(2)
print(per_mese.head(12), "\n")

print("=== 4e) TIMEZONE: localizzare e convertire (demo) ===")
# Creiamo una mini serie con timezone
mini_time = pd.date_range("2025-01-01", periods=3, freq="H")
mini = pd.Series([100, 120, 90], index=mini_time, name="valore")
mini = mini.tz_localize("Europe/Rome").tz_convert("UTC")  # Rome -> UTC
print(mini, "\n")


# ==============================================================
# 5) INDICIZZAZIONE AVANZATA
# ==============================================================

print("=== 5) Indicizzazione avanzata: loc/iloc, slice su date ===")

# pivot1 ha index datetime: posso fare slicing per intervallo
subset_date = pivot1.loc["2025-02-01":"2025-02-10"]
print("Slicing date 2025-02-01..2025-02-10:\n", subset_date.head(), "\n")

print("=== 5b) query: filtra con espressione ===")
q = df.query("negozio == 'Roma' and categoria == 'Tech' and totale > 200")
print("Query (prime 5):\n", q.head(), "\n")

print("=== 5c) mask booleana complessa con isin + between ===")
mask = df["negozio"].isin(["Genova", "Milano"]) & df["prezzo"].between(20, 50) & (df["qta"] >= 3)
print(df.loc[mask, ["data", "negozio", "categoria", "prezzo", "qta", "totale"]].head(), "\n")

print("=== 5d) MultiIndex: selezione con xs (cross-section) ===")
# pivot3 ha MultiIndex su index (negozio, categoria)
# Estraggo solo "Milano" con xs:
milano_only = pivot3.xs("Milano", level="negozio")
print("Solo Milano (xs):\n", milano_only.head(), "\n")

print("=== 5e) MultiIndex: slice su due livelli ===")
# Creo un MultiIndex esplicito per demo e faccio slicing con IndexSlice
idx = pd.IndexSlice
# Seleziono (Genova..Roma) e categoria specifica, poi tutte le colonne
multi_slice = pivot3.loc[idx["Genova":"Roma", "Tech"], :]
print("Slice MultiIndex (negozio Genova..Roma, categoria Tech):\n", multi_slice.head(), "\n")

print("=== 5f) set_index multiplo e selezione con loc ===")
df_mi = df.set_index(["negozio", "categoria", "data"]).sort_index()
# Seleziono tutte le righe di Genova/Tech in un intervallo di date
sel = df_mi.loc[("Genova", "Tech", slice("2025-01-15", "2025-01-20")), ["prodotto", "qta", "prezzo", "totale"]]
print("Genova/Tech 2025-01-15..2025-01-20:\n", sel.head(), "\n")


print("=== FINE DENO ===")