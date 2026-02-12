# mattina 12/02/2026

# polimorfismo passivo - duck typing

class Cane:
    def parla(self):
        return "Bau!"

class Gatto:
    def parla(self):
        return "Miao!"

def fai_parlare(animale):
    # Non importa di che tipo sia l'animale, l'animale parlerà (se ha quel metodo definito)
    print(animale.parla())

cane = Cane()
gatto = Gatto()

fai_parlare(cane) # Output: Bau!
fai_parlare(gatto) # Output: Miao!
