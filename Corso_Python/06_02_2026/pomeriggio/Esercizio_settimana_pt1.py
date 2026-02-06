# pomeriggio 06/02/2026

"""
ESERCIZIO RIASSUNTIVO – PARTE 1 - traccia generata da gpt

OBIETTIVO
Simulare la gestione di ordini in un piccolo negozio, utilizzando strutture dati,
controlli di flusso e funzioni.

REQUISITI
1. Dati
- Gestire una lista di ordini.
- Ogni ordine è rappresentato da una tupla nel formato:
  (nome_cliente, categoria, importo)

2. Collezioni
- Usare:
  - una lista per contenere gli ordini
  - un insieme (set) per definire le categorie valide
  - almeno una tupla per rappresentare i singoli ordini

3. Controlli
- Verificare se la categoria dell’ordine è valida.
- Classificare l’importo dell’ordine:
  - importo < 50 → ordine piccolo
  - importo tra 50 e 100 → ordine medio
  - importo > 100 → ordine grande

4. Cicli
- Utilizzare un ciclo for per analizzare gli ordini presenti.
- Utilizzare un ciclo while per permettere l’inserimento di nuovi ordini
  fino a quando l’utente decide di terminare.

5. Funzioni
- Creare funzioni per:
  - validare un ordine
  - classificare un ordine in base all’importo
  - calcolare il totale degli importi degli ordini validi

6. Generator
- Implementare almeno una funzione generatore (yield) che restituisca
  solo gli ordini validi, uno alla volta.

OUTPUT
Il programma deve stampare:
- il numero totale di ordini validi
- il totale incassato
- l’elenco degli ordini di importo grande

"""


# funzioni utili
def valida_ordine(ordine, categorie):
    """
    restituisce True solo se l'ordine è valido, cioè se ha un importo positivo e una categoria tra quelle valide
    """
    nome = ordine[0]
    categoria = ordine[1]
    importo = ordine[2]

    if categoria not in categorie:
        return False

    if importo < 0:
        return False

    return True


def classifica_importo(importo):
    """
    classifica un importo in piccolo (<50), medio (tra 50 e 100) o grande (>100)"""
    if importo < 50:
        return "piccolo"
    elif importo <= 100:
        return "medio"
    else:
        return "grande"


def genera_ordini_validi(lista_ordini, categorie):
    """
    generatore di ordini da una lista, controllando che siano validi
    """
    for ordine in lista_ordini:
        if valida_ordine(ordine, categorie):
            yield ordine


def calcola_totale(lista_ordini, categorie):
    """
    calcola il totale importo degli ordini in lista_ordini
    """
    totale = 0
    for ordine in genera_ordini_validi(lista_ordini, categorie):
        totale = totale + ordine[2]
    return totale

# simulazione di un database
# è una lista di tuple
ordini = []

categorie_valide = {"elettronica", "abbigliamento", "alimentari","cancelleria"}


print("\n********** Inserimento ordine **********")
print("Per riepologo digita -> stop")

while True:
    uscita = False
    if uscita:
        break
    print("\n# Nuovo ordine")
    nome = input("Nome cliente: ").lower()
    if nome == "stop":
        break
    
    print("Categorie disponibili ", categorie_valide)    
    while True:
        # Riprova finchè non mette una categoria giusta o l'utente digita stop
        categoria = input("Categoria: ")
        if categoria in categorie_valide:
            importo = int(input("Importo: "))

            nuovo_ordine = (nome, categoria, importo)
            ordini.append(nuovo_ordine)
            print("Ordine aggiunto\n")
            break
        else:
            print("Categoria non valida. Ricomincio")
            uscita = True
            break
        

ordini_validi = []                  
ordini_scartati = []

for ordine in ordini:
    
    # controlla se l'ordine è valido per categoria e importo
    if valida_ordine(ordine, categorie_valide):
        ordini_validi.append(ordine)

        # classifica se l'importo è piccolo, medio o grande
        tipo = classifica_importo(ordine[2])
    else:
        ordini_scartati.append(ordine)


totale_incasso = calcola_totale(ordini, categorie_valide)

print("\nRiepilogo")
print("Ordini totali:", len(ordini))
print("Ordini validi:", len(ordini_validi))
print("Ordini scartati:", len(ordini_scartati))
print("Totale incasso:", totale_incasso)



