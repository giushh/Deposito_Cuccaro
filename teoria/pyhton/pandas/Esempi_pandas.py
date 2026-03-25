import pandas as pd

"""Esempio Pratico: Uso di pivot_table
Supponiamo di avere un dataset che registra le vendite giornaliere di diversi prodotti in
varie città. Potremmo voler analizzare le vendite medie per prodotto in ciascuna città."""

# Dati di esempio
data = {
 'Data': ['2021-01-01', '2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
 'Città': ['Roma', 'Milano', 'Napoli', 'Roma', 'Milano'],
 'Prodotto': ['Mouse', 'Tastiera', 'Mouse', 'Tastiera', 'Mouse'],
 'Vendite': [100, 200, 150, 300, 250]
}

df = pd.DataFrame(data)
print(df)

# Creazione della tabella pivot
pivot_df = df.pivot_table(values='Vendite', index='Prodotto', columns='Città', aggfunc='mean')
print()
print(pivot_df)


"""Esempio Pratico di groupby,Immaginiamo di voler calcolare il totale delle vendite per ciascun
prodotto, utilizzando il dataset delle vendite giornaliere."""

data = {
 'Data': ['2021-01-01', '2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
 'Città': ['Roma', 'Milano', 'Napoli', 'Roma', 'Milano'],
 'Prodotto': ['Mouse', 'Tastiera', 'Mouse', 'Tastiera', 'Mouse'],
 'Vendite': [100, 200, 150, 300, 250]
}

df = pd.DataFrame(data)

# Utilizzo di groupby per aggregare i dati
grouped_df = df.groupby('Prodotto').sum()

print(grouped_df)

"""altro esempio con merge"""
print()

data_vendite = {
 'Prodotto': ['Tastiera', 'Mouse', 'Monitor', 'Tastiera', 'Monitor'],
 'Quantità': [5, 10, 2, 7, 3],
 'Città': ['Roma', 'Milano', 'Roma', 'Napoli', 'Milano'],
 'Data': ['2021-09-01', '2021-09-01', '2021-09-02', '2021-09-02', '2021-09-03']
}
vendite_df = pd.DataFrame(data_vendite)
print("\nStampo data_vendite")
print(vendite_df)

data_costi = {
 'Prodotto': ['Tastiera', 'Mouse', 'Monitor'],
 'Costo per unità': [50, 25, 150]
}
costi_df = pd.DataFrame(data_costi)
print("\nStampo data_costi")
print(costi_df)

# Unione dei DataFrame
df_merge = pd.merge(vendite_df, costi_df, on='Prodotto')

# Creazione della tabella pivot
pivot_table = df_merge.pivot_table(index='Prodotto', columns='Città', values='Quantità', aggfunc='sum')

# Visualizzazione del risultato
print("\nDopo aver fatto il merge (su prodotto in comune) e pivot")
print(pivot_table)