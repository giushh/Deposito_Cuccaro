# Esercizio 1 - Facile

"""
Crea una classe chiamata Punto. Questa classe dovrebbe avere:
Due attributi: x e y, per rappresentare le coordinate del punto nel piano.
Un metodo muovi che prenda in input un valore per dx e un valore per dy e modifichi le coordinate del punto di questi valori.
Un metodo distanza_da_origine che restituisca la distanza del punto dall'origine (0,0) del piano.

Rendilo ripetibile , cioè chiedere se continuare a spostare il punto o no

EXTRA: Andare a gestire nel primo esercizio X punti che sono X oggetti che deve definire tutti e stampare tutti assieme.
"""

class Punto:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def muovi(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        
    def distanza_da_origine(self):
        # ritorna una tupla (x,y) con la distanza dall'origine, 
        return (self.x ** 2 + self.y ** 2) ** 0.5 # teorema di pitagora per la distanza dal centro
    
    def stampa_coordinate(self):
        return f"({self.x}, {self.y})"
    
print("********** Piano Cartesiano **********")

stop = False
p = Punto(0,0)
while not stop:
    
    scelta = input("\nVuoi:"
                   "\n1. Inserire un nuovo punto"
                   "\n2. Muovere il punto corrente"
                   "\n3. Distanza da origine punto corrente"
                   "\n4. Uscire"
                   "\nInserisci 1/2/3/4 ")
    
    match scelta:
        case "1":
            print("\n-- Inserimento punto")
            x = int(input("Dimmi il punto sulle ascisse: "))
            y = int(input("Dimmi il punto sulle ordinate: "))
           
            p = Punto(x, y)  
            print("Il punto inserito è alle coordinate", p.stampa_coordinate())
            
        case "2":
            print("\n-- Movimento punto")
            print("Punto corrente (", p.x,",",p.y,")")
            x = int(input("Spostamento sulle ascisse: "))
            y = int(input("Spostamento sulle ordinate: "))
            p.muovi(1, -2)
            print("Il punto spostato è alle coordinate", p.stampa_coordinate())
            
        case "3":
            print("\n-- Distanza da origine")
            distanza = p.distanza_da_origine() 
            print("La distanza dall'origine è: ", distanza)
            
        case "4":
            print("\n-- Uscita")
            stop = True
        case _: 
            print("Comando non valido. \n--Uscita")
            stop = True
