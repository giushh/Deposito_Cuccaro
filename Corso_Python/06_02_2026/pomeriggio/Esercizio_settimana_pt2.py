# pomeriggio 06/02/2026

"""
ESERCIZIO RIASSUNTIVO – PARTE 2 
Stesso programma della parte 1, ma organizzato in funzioni e 2 decoratori
(Niente dizionari: i risultati vengono restituiti come tupla)
"""

# Decoratore: stampa prima e dopo la chiamata della funzione
def stampa_chiamata(nome_funzione):
    def decoratore(funzione):
        def wrapper(*args, **kwargs):
            print("\n[PRIMA] della funzione", nome_funzione)
            risultato = funzione(*args, **kwargs)
            print("[DOPO] la funzione", nome_funzione)
            return risultato
        return wrapper
    return decoratore


# Decoratore: conta quante volte vengono chiamate le funzioni (totale)
# for fun
chiamate_totali = 0

def conta_chiamate(funzione):
    def wrapper(*args, **kwargs):
        global chiamate_totali
        chiamate_totali = chiamate_totali + 1
        return funzione(*args, **kwargs)
    return wrapper


# chiamate alle funzioni

@conta_chiamate
@stampa_chiamata("Creazione ordini")
def crea_ordini_iniziali():
    """
    crea una lista iniziale di ordini di esempio (lista di tuple)
    """
    ordini = [
        ("Mario", "elettronica", 120),
        ("Giulia", "abbigliamento", 45),
        ("Luca", "alimentari", 70),
        ("Sara", "alimentari", 30)
    ]
    return ordini


@conta_chiamate
@stampa_chiamata("Crea categorie")
def crea_categorie_valide():
    """
    restituisce l'insieme (set) delle categorie valide
    """
    categorie = {"elettronica", "abbigliamento", "alimentari", "cancelleria"}
    return categorie


@conta_chiamate
@stampa_chiamata("Validazione ordine")
def valida_ordine(ordine, categorie):
    """
    restituisce True solo se l'ordine è valido, cioè se ha un importo positivo
    e una categoria tra quelle valide
    """
    nome = ordine[0]
    categoria = ordine[1]
    importo = ordine[2]

    if categoria not in categorie:
        return False

    if importo < 0:
        return False

    return True


@conta_chiamate
@stampa_chiamata("Classifica importo")
def classifica_importo(importo):
    """
    classifica un importo in:
    - piccolo (<50)
    - medio (tra 50 e 100)
    - grande (>100)
    """
    if importo < 50:
        return "piccolo"
    elif importo <= 100:
        return "medio"
    else:
        return "grande"


@conta_chiamate
@stampa_chiamata("Genera lista ordini")
def genera_ordini_validi(lista_ordini, categorie):
    """
    generatore di ordini da una lista, controllando che siano validi
    """
    for ordine in lista_ordini:
        if valida_ordine(ordine, categorie):
            yield ordine


@conta_chiamate
@stampa_chiamata("Calcola totale")
def calcola_totale(lista_ordini, categorie):
    """
    calcola il totale importo degli ordini validi in lista_ordini
    """
    totale = 0
    for ordine in genera_ordini_validi(lista_ordini, categorie):
        totale = totale + ordine[2]
    return totale



# doppio decoratore
@stampa_chiamata("Inserimento da input")
@conta_chiamate
def inserisci_ordini_da_input(ordini, categorie_valide):
    """
    permette all'utente di inserire nuovi ordini finché non scrive stop.
    controlla anche che la categoria sia valida, riprovando se serve.
    """
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
            # riprova finché non mette una categoria giusta o si torna indietro
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


@stampa_chiamata("Analizza ordini")
@conta_chiamate
def analizza_ordini(ordini, categorie_valide):
    """
    separa ordini validi e scartati, calcola totale e ordini.
    restituisce una tupla con:
    (ordini_validi, ordini_scartati, totale_incasso)
    """
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

    return (ordini_validi, ordini_scartati, totale_incasso)


@stampa_chiamata("Stampa risultati")
@conta_chiamate
def stampa_risultati(ordini, ordini_validi, ordini_scartati, totale_incasso):
    """
    stampa il riepilogo finale come nella Parte 1
    """
    print("\nRiepilogo")
    print("Ordini totali:", len(ordini))
    print("Ordini validi:", len(ordini_validi))
    print("Ordini scartati:", len(ordini_scartati))
    print("Totale incasso:", totale_incasso)


@stampa_chiamata("Conteggio finale")
@conta_chiamate
def stampa_conteggio_finale():
    """
    stampa quante chiamate totali alle funzioni sono avvenute
    """
    print("\nNumero totale di chiamate alle funzioni:", chiamate_totali)



# esecuzione
ordini = crea_ordini_iniziali()

categorie_valide = crea_categorie_valide()

inserisci_ordini_da_input(ordini, categorie_valide)

# analisi (ritorna una tupla)
ris = analizza_ordini(ordini, categorie_valide)

ordini_validi = ris[0]
ordini_scartati = ris[1]
totale_incasso = ris[2]

stampa_risultati(ordini, ordini_validi, ordini_scartati, totale_incasso)

stampa_conteggio_finale()
