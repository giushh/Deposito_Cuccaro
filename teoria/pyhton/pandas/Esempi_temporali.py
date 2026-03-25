"""Pandas offre strumenti specifici per manipolare date e
tempi, permettendo di analizzare serie temporali, cambiare
la frequenza dei dati, e generare periodi di tempo."""

import pandas as pd
df = pd.DataFrame()
# Generazione di una serie di date
date_range = pd.date_range(start='2021-01-01', periods=10, freq='M')

# Resampling dei dati di una serie temporale
df_resampled = df.resample('M').mean()

"""pd.to_datetime()
Converte un indice o una colonna in formato datetime, permettendo di sfruttare
tutte le funzionalità di time series DI python"""

# esempio: colonna “date” in stringhe → datetime
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
# oppure per creare un indice
df.index = pd.to_datetime(df['date'])

"""DataFrame.resample()
Ridimensiona (aggregate o down/up-sample) la frequenza temporale dei dati,
specificando l’intervallo desiderato (‘D’=day, ‘M’=month, ‘H’=hour, …)."""

# partendo da un DataFrame con indice DatetimeIndex:
df_daily = df.resample('D').mean() # media giornaliera
df_monthly = df.resample('M').sum() # somma mensile


"""Series.shift()
“Sposta” i valori lungo l’asse temporale di un numero di periodi, utile per
calcolare differenze ritardate, tassi di crescita, ecc."""

# aggiunge una colonna con il valore del giorno precedente
df['prev_day'] = df['value'].shift(1)
# tasso di variazione giornaliero
df['daily_return'] = df['value'].pct_change()
# equivalente a shift + calcolo %

"""Series.rolling()
Calcola statistiche mobili su una finestra temporale scorrevole."""

# finestra mobile di 7 giorni: media e deviazione standard
df['rolling_mean7'] = df['value'].rolling(window=7).mean()
df['rolling_std7'] = df['value'].rolling(window=7).std()