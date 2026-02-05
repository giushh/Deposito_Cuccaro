# Mattina del 04/02/2026

# Esercizi sulle condizioni 

# 1 - Creare una serie di condizioni annidate che a fronte di un input per ogni condizione decidano se farti passare o no
print("Vediamo se conosci la data di oggi")
giorno = int(input("Che giorno è oggi? "))
if (giorno == 4):
    print("Ottimo!")
    mese = input("In che mese siamo? ")
    if (mese == "2" or mese == "febbraio"):
        print("Ben fatto!")
        anno = int(input("In che anno siamo? "))
        if anno == 2026:
            print("Perfetto, conosci la data di oggi")
        else: 
            print("Anno sbagliato")
    else:
        print("Mese sbagliato")
else:
    print("Giorno sbagliato")
    
    
# 2 - Andare a creare un if con vari elif che gestisca un CRUD basilare (create, read, update, delete) che l'utente sceglie
lista = ["mele", "pere", "mirtilli"]
print("Questa è la tua lista: ", lista)
print("Puoi:")
print("1 - Aggiungi; 2 - Rimuovi; 3 - Elimina la lista")

do = input("Cosa vuoi fare? ")

if do == "1":
    elem = input("Cosa vuoi aggiungere? ")
    lista.append(elem)
    print("Lista aggiornata: ", lista)
elif do == "2":
    print("Cosa vuoi rimuovere da ", lista)
    elem = input()
    # print("Hai scelto ", elem)
    if (elem.lower() in lista):
        lista.remove(elem)
        print("Lista aggiornata: ", lista)
elif do == "3":
    lista.clear()
    print("Lista eliminata")
else:
    print("Comando non valido")
print("Fine")


# 3 - Creazione un if semplice per controllare se sei registrato, se non lo sei crei una struttura per la creazione dei dati dell'utente (nome, pass, id ecc)
# scopo: controllare la logica nella negazione, dove la condizione positiva (sono registrata) va a finire nell'else
print("Lista utenti")
utente = set()
presente = input("Sei già registrato? y/n ")

if presente == "n":
    print("Ok registriamo un nuovo utente")
    nome_utente = input("Come ti chiami? ")
    utente.add(nome_utente)

    nickname = input("Qual è il tuo nickname? ")
    utente.add(nickname)

    password = input("Scegli una password: ")
    password2 = input("Ripeti la password: ")
    if password == password2:
        print("Le password corrispondono. Possiamo proseguire")

        id_utente = nome_utente + nickname
        utente.add(id_utente)

        lista = list(utente)

        print("Utente registrato.")
        print("Nome:", lista[0])            # non è garantito l'ordine essenso un insieme, proseguiremo solo a scopo didattico
        print("Nickname:", lista[1])
    else:
        print("Le password non corrispondono. Uscita")
elif presente == "y":
    print("Perfetto, nulla da fare")
else:
    print("Comando errato")
