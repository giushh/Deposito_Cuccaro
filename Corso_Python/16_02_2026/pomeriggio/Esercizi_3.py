#pomeriggio 16/02/2026

"""
Scrivete un programma che prenda i nomi degli alunni di una
classe e i loro voti, quando l’utente scrive media il programma
andrà a stampare i nomi di tutti gli alunni e per ogni alunno la
media dei voti.
Esempio:
Nome: Giovanni , Media: 7.5
Nome: Alfredo , Media: 9
Nome: Michela, Media 10
"""

studenti = {}  

stop = False

while not stop:
    
    scelta = input("\nPuoi:"
                   "\n1. Inserire un nuovo alunno"
                   "\n2. Stampare le medie"
                   "\n3. Uscita"
                   "\nIndica il numero corrispondente \n> ")
    
    match scelta:
        
        case "1":
            nome = input("Nome alunno: ")
            voti = []

            print("Inserisci i voti (scrivi -1 per terminare):")
            
            while True:
                voto = float(input("Voto: "))
                
                if voto == -1:
                    break
            
                voti.append(voto)
            
            studenti[nome] = voti
            print("Alunno inserito correttamente.")
        
        case "2":
            
            if not studenti:
                print("Nessun alunno inserito.")
            else:
                print("\n--- Medie ---")
                
                for nome, voti in studenti.items():
                    if len(voti) == 0:
                        media = 0
                    else:
                        somma = 0
                        for voto in voti:
                            somma += voto
                        media = somma / len(voti)
                    
                    print(f"Nome: {nome}, media: {media}, numero di voti: {len(voti)}")
        
        case "3":
            print("\n-- Uscita")
            stop = True
        
        case _:
            print("\nComando non valido. \nRiprova.")
            continue
