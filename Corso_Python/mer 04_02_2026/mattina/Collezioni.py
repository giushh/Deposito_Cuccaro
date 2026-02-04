# Mattina del 04/02/2026

# Liste - collezioni ordinate, modificabili e miste 
numeri = [1, 2, 3, 4, 5]                                        # lista di tipo numerico
nomi = ["Ilaria", "Mirko", "Giuseppe"]                          # lista di tipo stringa
mix = ["Ciao", 2, False]                                        # lista di tipi misti
print("Mi chiamo ", nomi[0])                                    # esempi stampe utilizzando l'indice delle liste
print("Ho ", mix[1], " mele")
print(numeri[0], " + ", numeri[1], " = ", numeri[0]+numeri[1])

# Lista di liste ~ tabella
lista = [numeri, nomi, mix]
print(lista[0])             # stamperà la lista alla posizione 0, cioè quella numerica [1, 2, 3, 4, 5]

# Metodi incorportati delle liste
numeri = [2, 5, 8, 3, 9]
print(len(numeri))              # stampa la lunghezza della lista, cioè il numero di elementi che contiene
numeri.append(10)               # aggiunge alla fine della lista l'elemento passato
print(numeri)                   # [2, 5, 8, 3, 9, 10]
numeri.insert(1, 4)             # inserisce in posizione 1 il valore 4
print(numeri)                   # [2, 4, 5, 8, 3, 9, 10]
numeri.remove(5)                # rimuove il valore 5
print(numeri)                   # [2, 4, 8, 3, 9, 10]
numeri.sort()                   # ordina gli elementi della lista
print(numeri)                   # [2, 3, 4, 8, 9, 10]



# Tuple - collezioni non modificabili, ordinate e miste
persona = ("Ilaria", 2026)
print(persona)
# persona[0]="Ciao" non  è permesso modificare una tupla, Typeerror
persona_lista = list(persona)       # trasformiamo la tupla in una lista, cosi può essere modificata
persona_lista[0] = "Paola"
print(persona_lista)

# Tuple packing - creazione di una tupla senza parentesi tonde
coordinate = 4, 7
print(coordinate)                   # (4, 7)

# Tuple unpacking - operazione inversa di packing
x, y = coordinate
print(coordinate)                   # (4, 7)



# Insiemi - collezioni modificabili, non ordinati e misti (anche se non è consigliato usare tipi diversi)
# bonus: non ammette elementi duplicati, gli elementi devono essere univoci, altrimenti verranno ignorati
# definiti o tramite set() oppure racchiudendo gli elementi in {}
set1 = set([1, 2, 3, 4, 5])
set2 = {4, 5, 6, 7}
print(set1, " - ", set2)                    # {1, 2, 3, 4, 5}  -  {4, 5, 6, 7}

print(set1.union(set2))                     # {1, 2, 3, 4, 5, 6, 7} - unione dei set
print(set1.intersection(set2))              # {4, 5} - intersezione (elementi comuni)
print(set1.difference(set2))                # {1, 2, 3} - differenza (elementi presenti nel set1 ma non nel set2)
print(set1.symmetric_difference(set2))      # {1, 2, 3, 6, 7} - differenza simmetrica (elementi che sono presenti in set1 o set2 ma non entrambi)