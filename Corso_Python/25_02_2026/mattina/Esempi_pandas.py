import pandas as pd 

file_path = r'Corso_Python\25_02_2026\mattina\numeri.csv'

df = pd.read_csv(file_path)

# print le prime righe per confermare la lettura
print(df.head())


import pandas as pd

# Creazione di un DataFrame con dati di esempio
data = {
'Nome': ['Alice', 'Bob', 'Carla'],
'Età': [25, 30, 22],
'Città': ['Roma', 'Milano', 'Napoli']
}
df = pd.DataFrame(data) # ho creato un dizionario e l'ho trasformato in dataframe

# Stampa del DataFrame originale
print("DataFrame Originale:")
print(df)

# Selezione delle righe dove l'età è superiore a 23
df_older = df[df['Età'] > 23] # seleziona tutte le righe della colonna Età dove l'età è maggiore di 23

# slicing !

# Stampa delle righe selezionate
print("\nPersone con età superiore a 23 anni:")
print(df_older)

# Aggiungiamo una nuova colonna la persona maggiorenne
df['Maggiorenne'] = df['Età'] >= 18

# Stampa del DataFrame con la nuova colonna
print("\nDataFrame con colonna 'Maggiorenne':")
print(df)