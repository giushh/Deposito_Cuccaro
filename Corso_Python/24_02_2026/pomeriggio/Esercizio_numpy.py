"""
Parte UNO: Sistema di gestione matrice 2D con NumPy

Il programma deve presentare un menu interattivo che consente
all'utente di eseguire varie operazioni su una matrice 2D.

Le operazioni disponibili includono:

1. Creare una nuova matrice 2D di dimensioni specificate da utente
   con numeri casuali tra 1 e 50.
2. Estrarre e stampare la sotto-matrice centrale.
3. Trasporre la matrice e stamparla.
4. Calcolare e stampare la somma di tutti gli elementi della matrice.
5. Uscire dal programma o ripetere.

Ogni volta che il sistema conclude un calcolo,
il risultato va salvato su un file txt.


Parte DUE: Andare a specializzare per aggiungere nuove operazioni

1. Moltiplicazione Element-wise con un'altra Matrice:
   L'utente può scegliere di creare una seconda matrice delle stesse dimensioni
   della prima e moltiplicarle elemento per elemento e stampare il risultato.
2. Calcolo della Media degli Elementi della Matrice:
   Calcolare e stampare la media di tutti gli elementi della matrice.

Ogni volta che il sistema conclude un calcolo,
il risultato va salvato su un file txt.


Parte 3: Ulteriore Estensione del Menu Interattivo

Estendere ulteriormente il programma precedente aggiungendo nuove opzioni al menu
per permettere ulteriori operazioni sulla matrice. Le nuove operazioni includono:

1. Calcolare la matrice inversa (se la matrice è quadrata e invertibile).
2. Applicare una funzione matematica a tutti gli elementi della matrice (ad esempio, sin, cos, exp).
3. Filtrare e visualizzare solo gli elementi della matrice che soddisfano una determinata condizione
   (ad esempio, maggiori di un certo valore).
4. RENDERE OGNI PARTE RICHIAMABILE SINGOLARMENTE
5. Uscire dal programma.

Tutti i dati necessari al programma possono essere randomizzati o chiesti da inserire all’utente.

Ogni volta che il sistema conclude un calcolo,
il risultato va salvato su un file txt.
"""

import numpy as np


matrice = None
nome_file = r"Corso_Python\24_02_2026\pomeriggio\matrice_dati.txt"


def salva_testo(testo):
    file = open(nome_file, "a")
    file.write(testo + "\n")
    file.close()


def calcola_inversa(matrice):
    inversa = np.linalg.inv(matrice)
    return inversa


def applica_funzione(matrice, nome_funzione):
    if nome_funzione == "sin":
        return np.sin(matrice)
    if nome_funzione == "cos":
        return np.cos(matrice)
    if nome_funzione == "exp":
        return np.exp(matrice)
    return None


def filtra_elementi(matrice, soglia):
    filtrati = matrice[matrice > soglia]
    return filtrati


stop = False
while not stop:

    scelta = input("\nPuoi:"
                   "\n1. Creare nuova matrice"
                   "\n2. Stampare sotto-matrice centrale"
                   "\n3. Trasporre la matrice"
                   "\n4. Calcolare somma elementi"
                   "\n5. Moltiplicazione element-wise con altra matrice"
                   "\n6. Calcolare media elementi"
                   "\n7. Calcolare matrice inversa"
                   "\n8. Applicare funzione matematica (sin/cos/exp)"
                   "\n9. Filtrare elementi (> soglia)"
                   "\n10. Uscita"
                   "\nIndica il numero corrispondente \n> ")

    match scelta:

        case "1":
            righe = int(input("\nNumero righe: "))
            colonne = int(input("Numero colonne: "))

            matrice = np.random.randint(1, 51, (righe, colonne))
            print("\nMatrice creata:\n", matrice)

            salva_testo("Nuova matrice creata:\n" + str(matrice))

        case "2":
            if matrice is not None:

                r, c = matrice.shape

                centro = matrice[r//4: 3*r//4, c//4: 3*c//4]

                print("\nSotto-matrice centrale:\n", centro)

                salva_testo("Sotto-matrice centrale:\n" + str(centro))
            else:
                print("\nDevi prima creare una matrice.")

        case "3":
            if matrice is not None:

                trasposta = matrice.T

                print("\nMatrice trasposta:\n", trasposta)

                salva_testo("Matrice trasposta:\n" + str(trasposta))
            else:
                print("\nDevi prima creare una matrice.")

        case "4":
            if matrice is not None:

                somma = matrice.sum()

                print("\nSomma elementi:", somma)

                salva_testo("Somma elementi: " + str(somma))
            else:
                print("\nDevi prima creare una matrice.")

        case "5":
            if matrice is not None:

                righe, colonne = matrice.shape
                matrice2 = np.random.randint(1, 51, (righe, colonne))
                
                prodotto = matrice * matrice2

                print("\nSeconda matrice:\n", matrice2)
                print("\nRisultato moltiplicazione element-wise:\n", prodotto)

                salva_testo("Seconda matrice:\n" + str(matrice2))
                salva_testo("Moltiplicazione element-wise:\n" + str(prodotto))
            else:
                print("\nDevi prima creare una matrice.")

        case "6":
            if matrice is not None:

                media = matrice.mean()

                print("\nMedia elementi:", media)

                salva_testo("Media elementi: " + str(media))
            else:
                print("\nDevi prima creare una matrice.")

        case "7":
            if matrice is not None:
                r, c = matrice.shape

                if r == c:
                    determinante = np.linalg.det(matrice)

                    if determinante != 0:
                        inversa = calcola_inversa(matrice)
                        print("\nMatrice inversa:\n", inversa)
                        salva_testo("Matrice inversa:\n" + str(inversa))
                    else:
                        print("\nLa matrice non è invertibile (determinante = 0).")
                else:
                    print("\nLa matrice deve essere quadrata per calcolare l'inversa.")
            else:
                print("\nDevi prima creare una matrice.")

        case "8":
            if matrice is not None:
                nome_funzione = input("\nScegli funzione (sin/cos/exp): ").strip().lower()

                risultato = applica_funzione(matrice, nome_funzione)

                if risultato is not None:
                    print("\nRisultato funzione", nome_funzione, ":\n", risultato)
                    salva_testo("Funzione " + nome_funzione + " applicata:\n" + str(risultato))
                else:
                    print("\nFunzione non valida.")
            else:
                print("\nDevi prima creare una matrice.")

        case "9":
            if matrice is not None:
                soglia = float(input("\nInserisci soglia (mostra elementi > soglia): "))

                filtrati = filtra_elementi(matrice, soglia)

                print("\nElementi filtrati:\n", filtrati)

                salva_testo("Elementi > " + str(soglia) + ":\n" + str(filtrati))
            else:
                print("\nDevi prima creare una matrice.")

        case "10":
            print("\n-- Uscita")
            stop = True

        case _:
            print("\nComando non valido. \nRiprova.")
            continue