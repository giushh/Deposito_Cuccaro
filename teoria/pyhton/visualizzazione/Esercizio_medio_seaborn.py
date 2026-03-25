"""
Esercizio Medio: Normalizzazione dei Dati

Creato un DataFrame pandas con tre colonne: altezza, peso e età.
Normalizza altezza e peso con min-max.
Lascia invariata età.
Mostra DataFrame originale e modificato.
Usa seaborn e funzioni.
"""


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def crea_dataframe():
    np.random.seed(0)
    return pd.DataFrame({
        "altezza": np.random.normal(170, 10, 50),
        "peso": np.random.normal(70, 15, 50),
        "eta": np.random.randint(18, 60, 50)
    })


def min_max(serie):
    return (serie - serie.min()) / (serie.max() - serie.min())


def normalizza(df):
    df2 = df.copy()
    df2["altezza"] = min_max(df["altezza"])
    df2["peso"] = min_max(df["peso"])
    return df2


def grafici(df, df_norm):

    fig, axes = plt.subplots(2, 2, figsize=(10, 6))

    # ORIGINALE
    sns.histplot(df["altezza"], bins=10, stat="count", ax=axes[0, 0])
    axes[0, 0].set_title("Altezza originale")

    sns.histplot(df["peso"], bins=10, stat="count", ax=axes[1, 0])
    axes[1, 0].set_title("Peso originale")

    # NORMALIZZATO
    sns.histplot(df_norm["altezza"], bins=10, stat="count", ax=axes[0, 1])
    axes[0, 1].set_xlim(0, 1)
    axes[0, 1].set_title("Altezza normalizzata")

    sns.histplot(df_norm["peso"], bins=10, stat="count", ax=axes[1, 1])
    axes[1, 1].set_xlim(0, 1)
    axes[1, 1].set_title("Peso normalizzato")

    plt.tight_layout()
    plt.show()


df = crea_dataframe()
df_norm = normalizza(df)

grafici(df, df_norm)