"""
Obiettivo: Utilizzare pandas e numpy per esplorare, pulire, trasformare e analizzare 
un dataset di clienti della compagnia di telecomunicazioni. 
L'esercizio mira a costruire un modello predittivo di base per la churn rate 
e scoprire correlazioni tra vari attributi del cliente e la loro fedeltà.

Dataset:
• ID_Cliente: Identificativo unico per ogni cliente  
• Età: Età del cliente  
• Durata_Abbonamento: Quanti mesi il cliente è stato abbonato  
• Tariffa_Mensile: Quanto il cliente paga al mese  
• Dati_Consumati: GB di dati consumati al mese  
• Servizio_Clienti_Contatti: Quante volte il cliente ha contattato il servizio clienti  
• Churn: Se il cliente ha lasciato la compagnia (Si/No)  

1. Caricamento e Esplorazione Iniziale:
   ○ Caricare i dati da un file CSV.  
   ○ Utilizzare info(), describe(), e value_counts() per esaminare la distribuzione dei dati 
   e identificare colonne con valori mancanti.  

2. Pulizia dei Dati:
   ○ Gestire i valori mancanti in modo appropriato, considerando l'imputazione 
   o la rimozione delle righe.  
   ○ Verificare e correggere eventuali anomalie nei dati 
   (es. età negative, tariffe mensili irrealistiche).  

3. Analisi Esplorativa dei Dati (EDA):
   ○ Creare nuove colonne che potrebbero essere utili, come Costo_per_GB (tariffa mensile divisa per dati consumati).  
   ○ Utilizzare groupby() per esplorare la relazione tra Età, Durata_Abbonamento, Tariffa_Mensile e la Churn.  
   ○ Utilizzare metodi come corr() per identificare possibili correlazioni tra le variabili.  

4. Preparazione dei Dati per la Modellazione:
   ○ Convertire la colonna Churn in formato numerico (0 per "No", 1 per "Si").  
   ○ Separare i dati in training e test set, se si intende procedere con la modellazione.
"""

import pandas as pd
import numpy as np
from termcolor import colored as c

dataset = r"Corso_Python\26_02_2026\mattina\dataset.csv"
dataset_pulito = r"Corso_Python\25_02_2026\mattina\dataset_pulito.csv"


def genera_dataset(nome_file, n=200):
    id_cliente = np.arange(1, n + 1)
    eta = np.random.randint(18, 75, size=n)
    durata_abbonamento = np.random.randint(1, 72, size=n)
    tariffa = np.random.uniform(0, 80, size=n).round(2)
    dati = np.random.uniform(0.5, 200, size=n).round(2) # GB consumati al mese
    servizio_clienti = np.random.randint(0, 12, size=n) # quante volte al mese chiama il servizio clienti
    churn = np.random.choice(["No", "Si"], p=[0.75, 0.25], size=n) # se il cliente ha lasciato la compagnia

    df = pd.DataFrame({
        "ID_Cliente": id_cliente,
        "Eta": eta,
        "Durata_Abbonamento": durata_abbonamento,
        "Tariffa_Mensile": tariffa,
        "Dati_Consumati": dati,
        "Servizio_Clienti_Contatti": servizio_clienti,
        "Churn": churn
    })

    # sporco volutamente il dataset
    indici_nan = np.random.choice(df.index, 6, replace=False)
    df.loc[indici_nan[:3], "Tariffa_Mensile"] = np.nan
    df.loc[indici_nan[3:], "Eta"] = np.nan

    df.to_csv(dataset, index=False)
    print("\nDataset creato e salvato su csv.")
    
    
def carica_dati(file):
    df = pd.read_csv(file)
    print("\nDataset caricato")
    return df

def esamina(df):
    pass 
    # esamina dati e identifica colonne con valori mancanti, usa info() desccrive() value_counts()
    print("\nInfo:")
    print(df.info())
    
    print("\nStatistiche descrittive:")
    print(df.describe())

    print("\nDistribuzione churn:")
    print(df["Churn"].value_counts())

    print("\nValori mancanti:")
    print(df.isna().sum())
    
    
def pulizia(df):
    # gestisci dati mancanti, riempi o elimina
    # correggi valori anomali, es tariffe negative ecc 
    
    df = df.copy()
    df = df.drop_duplicates()

    # gestione valori mancanti
    # età e tariffa riempite con la media
    df["Eta"] = df["Eta"].fillna(df["Eta"].mean())
    df["Tariffa_Mensile"] = df["Tariffa_Mensile"].fillna(df["Tariffa_Mensile"].mean())
    
    # il metodo clip() restringe il valore in uno specifico range
    # in questo caso età tariffa e dati non possono essere minori di 0
    df["Eta"] = df["Eta"].clip(lower=0)
    df["Tariffa_Mensile"] = df["Tariffa_Mensile"].clip(lower=0)
    df["Dati_Consumati"] = df["Dati_Consumati"].clip(lower=0)
    
    print("\nPulizia completata")
    return df

    
def eda(df):
    # EDA - analisi escplorativa dei dati
    # crea nuova colonna Costo_per_GB (tariffa mensile per dati consumati)
    # groupby() per la relazione tra età durata abbonamento tariffa mensile churn 
    # usa corr() per identificare popssibili correlazioni tra variabili
    
    df = df.copy()
    
    # creazione colonna Costo_per_GB e riempimento se Nan
    df["Costo_per_GB"] = df["Tariffa_Mensile"] / df["Dati_Consumati"]
    df["Costo_per_GB"] = df["Costo_per_GB"].fillna(df["Costo_per_GB"].median())
    
    # groupby 
    print("\nMedia variabili per churn:")
    media = df.groupby("Churn")[["Eta", "Durata_Abbonamento",
                                  "Tariffa_Mensile", "Dati_Consumati",
                                  "Servizio_Clienti_Contatti"]].mean()
    print(media.round(2))
    
    
    print("\nCorrelazioni:")
    corr = df[["Eta", "Durata_Abbonamento",
               "Tariffa_Mensile", "Dati_Consumati",
               "Servizio_Clienti_Contatti",
               "Costo_per_GB"]].corr()
    print(corr.round(3))
    
    return df
    

from sklearn.preprocessing import StandardScaler

def preparazione(df):
    # converti churn in 0 e 1
    # normalizza le colonne numeriche per prepararle alla modellazione
    df = df.copy() 
    
    # sostituzione si/no con 0/1 in churn
    df["Churn"] = df["Churn"].map({"No": 0, "Si": 1})
    
    """
    the iloc() function is a powerful tool that enables users to select specific rows
    and columns of a DataFrame by their integer position
     
    Preparazione dei dati per la modellazione del churn.

    In questa fase si separano le variabili indipendenti (feature) dalla variabile
    target (Churn). Le feature rappresentano le informazioni del cliente che
    utilizzeremo per prevedere se abbandonerà o meno il servizio.

    Successivamente si applica una normalizzazione tramite StandardScaler.
    La normalizzazione serve a portare tutte le variabili sulla stessa scala,
    in modo che nessuna feature con valori numericamente più grandi influenzi
    maggiormente il modello. Il metodo standardizza ogni colonna sottraendo
    la media e dividendo per la deviazione standard, ottenendo variabili con
    media 0 e deviazione standard 1.

    Infine si divide il dataset in training set e test set utilizzando iloc.
    L’80% dei dati viene utilizzato per addestrare il modello, mentre il 20%
    viene conservato per testarne le prestazioni su dati non visti.
    """

    # separazione feature e target
    X = df[["Eta",
            "Durata_Abbonamento",
            "Tariffa_Mensile",
            "Dati_Consumati",
            "Servizio_Clienti_Contatti",
            "Costo_per_GB"]]

    y = df["Churn"] # target

    # normalizzazione
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # trasformo l'array normalizzato in dataframe per mantenere le colonne
    X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

    # split manuale 80/20 con iloc
    split = int(len(df) * 0.8)

    X_train = X_scaled.iloc[:split]
    X_test = X_scaled.iloc[split:]

    y_train = y.iloc[:split]
    y_test = y.iloc[split:]

    print("Training size:", len(X_train))
    print("Test size:", len(X_test))
    

    return df


def main():
        print("****** Esercizio - Telecomunicazioni *****")
        
        print(c("\nGenerzione Dataset", "green"))
        genera_dataset(dataset)
        
        print(c("\nCaricamento Dataset", "green"))
        df = carica_dati(dataset)
        df_prima = df.copy(deep=True) # con deep True crea un oggetto indipendente 
        
        print(c("\nEsamino Dataset", "green"))
        esamina(df)
        
        print(c("\nPulizia Dataset", "green"))
        df = pulizia(df)

        print(c("\nAnalisi Esplorativa Dati - EDA", "green"))
        df = eda(df)

        print(c("\nPreparazione Dataset", "green"))
        df = preparazione(df)
        
        df.to_csv(dataset_pulito, index=False)
        print(c("\nDataset salvato.", "green"))
        
        scelta = input(c("\nVuoi vedere il Dataset prima e dopo? y/n >", "green"))
        if scelta == "y":
            print(c("\nDataset prima:", "green"))
            print(df_prima)
            print()
            print(c("\nDataset Dopo:", "green"))
            print(df)
        else:
            print(c("Ok ciao.", "red"))
            
            

if __name__ == "__main__":
    main()