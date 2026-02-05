# Pomeriggio del 04/02/2026

# Ciclo while numerico
print("********** Esempio 1 **********")
num = 10
iteraz = 0
print("Contiamo fino a 10")

while iteraz < num:
    print(iteraz + 1)
    iteraz += 1
    
    
# Ciclo while booleano
print("********** Esempio 2 **********")
num = 10
iteraz = 0

controllore = True
while controllore:
    print("Contiamo fino a",num)
    while iteraz < num:
        print(iteraz + 1)
        iteraz += 1
    num += 10
    uscita = input("Vuoi continuare a contare? (y/n) ")
    if uscita == "n":
        controllore = False
print("Addio")


# Ciclo for 
print("********** Esempio 3 **********")
menu = ["antipasto", "primo", "secondo", "frutta", "dolce"]

print("Il menu di oggi prevede:")
for portate in menu:
    print(portate)


# Ciclo for 
print("********** Esempio 3 **********")
frutta = ["mele", "fragole", "mirtilli", "banane", "mango", "pere"]

for elem in range(len(frutta)):
    print(frutta[elem])