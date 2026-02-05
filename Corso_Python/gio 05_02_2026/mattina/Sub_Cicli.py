# Mattina del 05/02/2026

# break - rompe il ciclo appena viene letto
# continue - salta il resto del ciclo e salta alla prossima iterazione (SALTA UN GIRO MA NON CHIUDE IL CICLO)
# pass - placeholder per quando non vuoi fare alcuna operazione all'interno del ciclo 

for i in range(11):
    if i == 3:
        pass
    if i == 8:
        continue
    if i == 9:
        break
    print(i+1)
    
    
# Operatore "splat" -> * 
# espande un iterabile in elementi separati nelle collezioni

print("\nSenza operatore splat")
numeri = [range(1, 11)]
print(numeri)

print("Con operatore splat")
numeri = [*range(1, 11)]
print(numeri)