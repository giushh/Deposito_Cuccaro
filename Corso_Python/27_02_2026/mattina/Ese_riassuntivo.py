"""
Esercizio Riassuntivo - Traccia generata da IA su specifiche richieste

Obiettivo:
- Realizzare un mini progetto di analisi dati simulando statistiche di partite di Lorcana,
  integrando NumPy per la generazione dei dati, Pandas per manipolazione e analisi,
  Matplotlib e Seaborn per la visualizzazione.

Scenario:
- Si vuole simulare un dataset di partite giocate tra due giocatori con mazzi composti da due colori.
  Per ogni partita si registrano alcune informazioni utili per fare analisi statistiche,
  come durata, lore finale, numero di turni e risultato.

Fase 1 – Generazione dei dati con NumPy
- Generare almeno 150 partite simulate
- Creare le seguenti variabili:
  - id_partita progressivo
  - colore_mazzo_g1, colore_mazzo_g2 scelti tra combinazioni realistiche:
    amethyst ruby, amber steel, sapphire steel, emerald ruby
  - numero_turni generato casualmente in un intervallo plausibile
  - lore_g1 e lore_g2 con valori coerenti rispetto alla vittoria a 20 lore
  - vincitore determinato in base al lore più alto
- Inserire volutamente alcuni valori mancanti e almeno una riga duplicata

Fase 2 – Creazione del DataFrame con Pandas
- Costruire un DataFrame a partire dai dati generati
- Assegnare nomi chiari alle colonne
- Visualizzare le prime righe con head
- Usare info e describe per una prima analisi strutturale e statistica

Fase 3 – Esplorazione e pulizia
- Individuare valori mancanti con isnull
- Decidere una strategia coerente per gestirli
- Rimuovere eventuali duplicati
- Verificare che i tipi di dato siano corretti

Fase 4 – Manipolazione e analisi
- Calcolare la durata media delle partite in termini di turni
- Calcolare la percentuale di vittorie per ciascuna combinazione di colori del giocatore 1
- Usare groupby per analizzare la media dei turni per combinazione di mazzo
- Creare una pivot table che mostri numero di vittorie per combinazione di colori
- Creare una nuova colonna che classifichi le partite come brevi, medie o lunghe in base ai turni

Fase 5 – Visualizzazione con Matplotlib
- Grafico a barre con il numero di vittorie per combinazione di mazzo
- Istogramma della distribuzione dei turni

Fase 6 – Visualizzazione con Seaborn
- Scatter plot tra numero_turni e lore_vincitore
- Heatmap della matrice di correlazione tra variabili numeriche (turni, lore_g1, lore_g2)
- Matrice dei matchup 
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


nome_file = r"Corso_Python\27_02_2026\mattina\dati_lorcana.csv"


def genera_dati_numpy():
    np.random.seed(42)

    numero_partite = 160
    id_partita = np.arange(1, numero_partite + 1)

    combinazioni_mazzo = np.array([
        "amethyst sapphire",
        "amber emerald",
        "emerald sapphire",
        "emerald amethyst"
    ])

    colore_mazzo_g1 = np.random.choice(combinazioni_mazzo, size=numero_partite, replace=True)
    colore_mazzo_g2 = np.random.choice(combinazioni_mazzo, size=numero_partite, replace=True)

    numero_turni = np.random.randint(4, 16, size=numero_partite)

    vincitore_binario = np.random.choice([1, 2], size=numero_partite, p=[0.5, 0.5])

    lore_g1 = np.zeros(numero_partite, dtype=int)
    lore_g2 = np.zeros(numero_partite, dtype=int)

    for i in range(numero_partite):
        if vincitore_binario[i] == 1:
            lore_g1[i] = 20
            lore_g2[i] = np.random.randint(0, 20)
        else:
            lore_g2[i] = 20
            lore_g1[i] = np.random.randint(0, 20)

    vincitore = np.where(lore_g1 > lore_g2, "G1", "G2")

    indici_nan_turni = np.random.choice(np.arange(numero_partite), size=7, replace=False)
    indici_nan_lore = np.random.choice(np.arange(numero_partite), size=7, replace=False)
    indici_nan_colore = np.random.choice(np.arange(numero_partite), size=4, replace=False)

    numero_turni = numero_turni.astype(float)
    numero_turni[indici_nan_turni] = np.nan

    lore_g1 = lore_g1.astype(float)
    lore_g2 = lore_g2.astype(float)

    for j, idx in enumerate(indici_nan_lore):
        if j % 2 == 0:
            lore_g1[idx] = np.nan
        else:
            lore_g2[idx] = np.nan

    colore_mazzo_g1 = colore_mazzo_g1.astype(object)
    for idx in indici_nan_colore[:2]:
        colore_mazzo_g1[idx] = np.nan

    colore_mazzo_g2 = colore_mazzo_g2.astype(object)
    for idx in indici_nan_colore[2:]:
        colore_mazzo_g2[idx] = np.nan

    return id_partita, colore_mazzo_g1, colore_mazzo_g2, numero_turni, lore_g1, lore_g2, vincitore


def salva_csv(id_partita, colore_mazzo_g1, colore_mazzo_g2, numero_turni, lore_g1, lore_g2, vincitore):
    dizionario_dati = {
        "id_partita": id_partita,
        "mazzo_g1": colore_mazzo_g1,
        "mazzo_g2": colore_mazzo_g2,
        "numero_turni": numero_turni,
        "lore_g1": lore_g1,
        "lore_g2": lore_g2,
        "vincitore": vincitore
    }

    df = pd.DataFrame(dizionario_dati)
    df = pd.concat([df, df.iloc[[9]]], ignore_index=True)
    df.to_csv(nome_file, index=False)


def importa_csv():
    df = pd.read_csv(nome_file)

    print("\nPrime righe (head):")
    print(df.head())

    print("\nInfo:")
    print(df.info())

    print("\nDescribe (colonne numeriche):")
    print(df.describe())

    return df


def esplora_pulisci(df):
    print("\nValori mancanti per colonna:")
    print(df.isnull().sum())

    moda_g1 = df["mazzo_g1"].mode(dropna=True)[0]
    moda_g2 = df["mazzo_g2"].mode(dropna=True)[0]

    df["mazzo_g1"] = df["mazzo_g1"].fillna(moda_g1)
    df["mazzo_g2"] = df["mazzo_g2"].fillna(moda_g2)

    mediana_turni = df["numero_turni"].median()
    df["numero_turni"] = df["numero_turni"].fillna(mediana_turni)

    mediana_lore_g1 = df["lore_g1"].median()
    mediana_lore_g2 = df["lore_g2"].median()

    df["lore_g1"] = df["lore_g1"].fillna(mediana_lore_g1)
    df["lore_g2"] = df["lore_g2"].fillna(mediana_lore_g2)

    prima = len(df)
    df = df.drop_duplicates()
    dopo = len(df)

    print(f"\nRighe prima rimozione duplicati: {prima}")
    print(f"Righe dopo rimozione duplicati:  {dopo}")

    df["id_partita"] = df["id_partita"].astype(int)
    df["numero_turni"] = df["numero_turni"].round(0).astype(int)
    df["lore_g1"] = df["lore_g1"].round(0).astype(int)
    df["lore_g2"] = df["lore_g2"].round(0).astype(int)

    df["vincitore"] = np.where(df["lore_g1"] >= df["lore_g2"], "G1", "G2")

    print("\nValori mancanti dopo pulizia:")
    print(df.isnull().sum())

    print("\nDtypes dopo pulizia:")
    print(df.dtypes)

    return df


def analisi(df):
    durata_media_turni = df["numero_turni"].mean()
    print(f"\nDurata media (turni): {durata_media_turni:.2f}")

    df["vittoria_g1"] = (df["vincitore"] == "G1").astype(int)

    percentuali_vittorie_g1 = df.groupby("mazzo_g1")["vittoria_g1"].mean() * 100
    percentuali_vittorie_g1 = percentuali_vittorie_g1.sort_values(ascending=False)

    print("\nPercentuale vittorie di G1 per mazzo_g1:")
    print(percentuali_vittorie_g1.round(2))

    media_turni_per_matchup = df.groupby(["mazzo_g1", "mazzo_g2"])["numero_turni"].mean()
    media_turni_per_matchup = media_turni_per_matchup.sort_values(ascending=False)

    print("\nMedia turni per matchup (mazzo_g1, mazzo_g2):")
    print(media_turni_per_matchup.round(2).head(10))

    pivot_vittorie = pd.pivot_table(
        df,
        values="vittoria_g1",
        index="mazzo_g1",
        columns="mazzo_g2",
        aggfunc="sum",
        fill_value=0
    )

    print("\nPivot - Numero vittorie di G1 per matchup (righe=G1, colonne=G2):")
    print(pivot_vittorie)

    df["categoria_durata"] = pd.cut(
        df["numero_turni"],
        bins=[-1, 7, 11, 100],
        labels=["breve", "media", "lunga"]
    )

    print("\nConteggio categorie durata:")
    print(df["categoria_durata"].value_counts())

    return df




"""
disclaimer: anche se alcuni tipi statistiche sono irrilevanti per le informazioni legate al gioco
(tipo numero di turni) sono stati volutamente inseriti a scopo didattico per esplorare i diversi tipi di grafici
"""

def grafici_matplotlib(df):
    vittorie_per_mazzo_g1 = df.groupby("mazzo_g1")["vittoria_g1"].sum().sort_values(ascending=False)

    plt.figure(figsize=(10, 5))
    plt.bar(vittorie_per_mazzo_g1.index, vittorie_per_mazzo_g1.values)
    plt.title("Vittorie Totali - Giocatore 1 per Tipo di Mazzo")
    plt.xlabel("Tipo di Mazzo (Giocatore 1)")
    plt.ylabel("Numero di Vittorie")
    plt.xticks(rotation=25, ha="right")
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.hist(df["numero_turni"], bins=12, edgecolor="black")
    plt.title("Distribuzione del Numero di Turni per Partita")
    plt.xlabel("Numero di Turni")
    plt.ylabel("Frequenza delle Partite")
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.show()


def grafici_seaborn(df):
    df["Lore Vincitore"] = np.where(df["vincitore"] == "G1", df["lore_g1"], df["lore_g2"])

    df_visual = df.rename(columns={
        "numero_turni": "Numero Turni",
        "lore_g1": "Lore Giocatore 1",
        "lore_g2": "Lore Giocatore 2",
        "vincitore": "Vincitore",
        "vittoria_g1": "Vittoria Giocatore 1"
    })

    plt.figure(figsize=(10, 5))
    sns.scatterplot(
        data=df_visual,
        x="Numero Turni",
        y="Lore Vincitore",
        hue="Vincitore",
        alpha=0.8
    )
    plt.title("Relazione tra Durata della Partita e Lore del Vincitore")
    plt.xlabel("Numero di Turni")
    plt.ylabel("Lore del Vincitore")
    plt.grid(True, linestyle="--", alpha=0.3)
    plt.tight_layout()
    plt.show()

    df_numerico = df_visual[[
        "Numero Turni",
        "Lore Giocatore 1",
        "Lore Giocatore 2",
        "Vittoria Giocatore 1",
        "Lore Vincitore"
    ]]

    matrice_corr = df_numerico.corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(
        matrice_corr,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        linewidths=0.5
    )
    plt.title("Matrice di Correlazione tra Variabili Numeriche")
    plt.tight_layout()
    plt.show()



def calcola_matrice_matchup(df):
    matchup = df.groupby(["mazzo_g1", "mazzo_g2"])["vittoria_g1"].agg(["sum", "count"]).reset_index()
    matchup["percentuale_vittorie_g1"] = (matchup["sum"] / matchup["count"]) * 100

    matrice_vittorie = matchup.pivot(index="mazzo_g1", columns="mazzo_g2", values="sum").fillna(0).astype(int)
    matrice_totali = matchup.pivot(index="mazzo_g1", columns="mazzo_g2", values="count").fillna(0).astype(int)
    matrice_percentuali = matchup.pivot(index="mazzo_g1", columns="mazzo_g2", values="percentuale_vittorie_g1").fillna(0).round(2)

    print("\nMatrice Matchup - Vittorie Giocatore 1 (righe=G1, colonne=G2):")
    print(matrice_vittorie)

    print("\nMatrice Matchup - Partite Totali (righe=G1, colonne=G2):")
    print(matrice_totali)

    print("\nMatrice Matchup - Percentuale Vittorie Giocatore 1 (righe=G1, colonne=G2):")
    print(matrice_percentuali)

    plt.figure(figsize=(9, 6))
    sns.heatmap(matrice_percentuali, annot=True, fmt=".1f", linewidths=0.5)
    plt.title("Matchup - Percentuale Vittorie Giocatore 1")
    plt.xlabel("Mazzo Giocatore 2")
    plt.ylabel("Mazzo Giocatore 1")
    plt.tight_layout()
    plt.show()

    return matrice_vittorie, matrice_totali, matrice_percentuali






def main():
    id_partita, colore_mazzo_g1, colore_mazzo_g2, numero_turni, lore_g1, lore_g2, vincitore = genera_dati_numpy()
    salva_csv(id_partita, colore_mazzo_g1, colore_mazzo_g2, numero_turni, lore_g1, lore_g2, vincitore)
    df = importa_csv()
    df = esplora_pulisci(df)
    df = analisi(df)
    calcola_matrice_matchup(df)
    grafici_matplotlib(df)
    grafici_seaborn(df)


if __name__ == "__main__":
    main()