# Pomeriggio del 04/02/2026

# 1 - scrivi un programma che chiede all'utente la sia età
# se è inferiore a 18 dice che può vedere il film, altrimenti no (usa match)

print("********** Esercizio 1 **********")
eta = int(input("Quanti anni hai? "))
if eta > 0:
    if eta < 18:
        minorenne = "si"
    else:
        minorenne = "no"

    match minorenne:
        case "si": 
            print("Mi dispiace non puoi guardare questo film")
        case "no":
            print("Puoi vedere questo film")
else: 
    print("Non puoi avere un'età negativa")

# 2 - Calcolatrice (con match)
print("\n********** Esercizio 2 **********")
op1 = int(input("Dimmi un numero: "))
op2 = int(input("Dimmi un altro numero: "))

print("Che operazione vuoi fare?"
        "\nAddizione (+)"
        "\nSottrazione (-)"
        "\nMoltiplicazione (*)"
        "\nDivisione (/)"
        "\nIndicami il simbolo dell'operazione scelta")
operazione = input()

match operazione:
    case "+":
        print(op1, " + ",op2," = ", op1+op2)
    case "-":
        print(op1, " - ",op2," = ", op1-op2)
    case "*":
        print(op1, " * ",op2," = ", op1*op2)
    case "/":
        if op2 == 0:
            print("Non si può dividere per zero")
        else:
            print(op1, " / ",op2," = ", op1/op2)
    case _: 
        print("Operazione non valida")
        
        
# 2.1 -VARIANTE match di match
print("\n********** Esercizio 2.1  **********")
print("I tuoi studi")
risposta = input("Hai fatto l'università? ")

match risposta:
    case "si":
        risposta2 = input("Congratulazioni! Ambito umanistico o scientifico? (rispondi con u/s) ")
        match risposta2:
            case "u":
                print("Davvero interessante")
            case "s":
                print("Wow bellissimo")
    case "no":
        print("Avrai avuto le tue ragioni sicuramente")