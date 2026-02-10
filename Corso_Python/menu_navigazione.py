stop = False
while not stop:
    
    scelta = input("\nPuoi:"
                   "\n1. "
                   "\n2. "
                   "\n3. Uscita"
                   "\nIndica il numero corrispondente \n> ")
    
    match scelta:
        case "1":
            pass
    
        case "2":
            pass

        case "3":
            print("\n-- Uscita")
            stop = True
        case _:
            print("\nComando non valido. \nRiprova.")
            continue