"""
Es2: linspace, random, sum

Consegna:
1. Utilizza np.linspace per creare un array di 50 numeri equidistanti tra 0 e 10.
2. Utilizza np.random.random per creare un array di 50 numeri casuali compresi tra 0 e 1.
3. Somma i due array elemento per elemento per ottenere un nuovo array.
4. Calcola la somma totale degli elementi del nuovo array.
5. Calcola la somma degli elementi del nuovo array che sono maggiori di 5.
6. Stampa gli array originali, il nuovo array risultante dalla somma e le somme calcolate.
7. Salva i dati su un file TXT a ogni esecuzione.
8. Rendi ripetibile il processo complessivo.
9. Mostra quante volte è stato salvato nel file.
"""

import numpy as np


def esegui():

    array1 = np.linspace(0, 10, 50)
    array2 = np.random.random(50)
    array_somma = array1 + array2

    somma_totale = array_somma.sum()
    somma_maggiori_5 = array_somma[array_somma > 5].sum()

    print("\n--- Risultati ---")
    print("\nArray 1:\n", array1)
    print("\nArray 2:\n", array2)
    print("\nArray somma:\n", array_somma)
    print("\nSomma totale:", somma_totale)
    print("Somma elementi maggiori di 5:", somma_maggiori_5)

    return array1, array2, array_somma, somma_totale, somma_maggiori_5


def conta_salvataggi(nome_file):
    try:
        file = open(nome_file, "r")
        contenuto = file.read()
        file.close()
        return contenuto.count("SALVATAGGIO")
    except:
        return 0


def salva(nome_file, modalita, numero_salvataggio,
          array1, array2, array_somma,
          somma_totale, somma_maggiori_5):

    with open(nome_file, modalita) as file:
        file.write("\nSALVATAGGIO " + str(numero_salvataggio) + "\n")
        file.write("-" * 50 + "\n")
        file.write("Array 1:\n")
        file.write(str(array1) + "\n\n")
        file.write("Array 2:\n")
        file.write(str(array2) + "\n\n")
        file.write("Array somma:\n")
        file.write(str(array_somma) + "\n\n")
        file.write("Somma totale: " + str(somma_totale) + "\n")
        file.write("Somma elementi maggiori di 5: " + str(somma_maggiori_5) + "\n")


def mostra(nome_file):
    try:
        file = open(nome_file, "r")
        contenuto = file.read()
        file.close()
        print("\n--- Contenuto del file ---\n")
        print(contenuto)
    except:
        print("\nIl file non esiste ancora.")


def main():
    
    nome_file = r"Corso_Python\24_02_2026\mattina\dati_es2.txt"

    stop = False
    while not stop:

        scelta = input("\nPuoi:"
                       "\n1. Eseguire esercizio e salvare"
                       "\n2. Mostrare contenuto file"
                       "\n3. Uscita"
                       "\nIndica il numero corrispondente \n> ")

        match scelta:
            case "1":
                risposta = input("\nVuoi sovrascrivere il file? (s/n) \n> ")

                if risposta == "s":
                    modalita = "w"
                    numero_salvataggio = 1
                else:
                    modalita = "a"
                    numero_salvataggio = conta_salvataggi(nome_file) + 1

                array1, array2, array_somma, somma_totale, somma_maggiori_5 = esegui()

                salva(nome_file, modalita, numero_salvataggio,
                      array1, array2, array_somma,
                      somma_totale, somma_maggiori_5)

                print("\nSalvataggio numero:", numero_salvataggio)

            case "2":
                mostra(nome_file)

            case "3":
                print("\n-- Uscita")
                stop = True

            case _:
                print("\nComando non valido. \nRiprova.")
                continue


if __name__ == "__main__":
    main()