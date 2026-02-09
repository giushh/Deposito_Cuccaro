# mattina 09/02/2026

# Classi e oggetti

class Persona():
    # attributi di tutti gli oggetti persona
    n_braccia = 2
    n_gambe = 2
        
    # costruttore
    def __init__(self, nome, colore_occhi, colore_capelli):
        self.colore_occhi = colore_occhi
        self.colore_capelli = colore_capelli
        self.nome = nome
        
    def __str__(self):
        return "Sono un oggetto di tipo Persona"

ilaria_OBJ = Persona("Ilaria","verdi", "marroni")

print(ilaria_OBJ.nome + " ha gli occhi "+ ilaria_OBJ.colore_occhi +" e i capelli "+ ilaria_OBJ.colore_capelli)


# il nome della classe definisce: il tipo (non basilare) della classe, il costruttore e il nome univoco di quella classe
print("La classe Persona è di tipo ", type(ilaria_OBJ))

# questo stampa la locazione di memoria dove è salvato l'oggetto
# ma se definiamo __str__ (metodo speciale TO STRING) viene richiamato e stampa il return definito da noi e non la locazione di memoria
print(ilaria_OBJ)

# esempi dei 3 tipo di metodi: di istanza, di classe, statici

# metodi statici - slegati dalla logica della classe, fa cose dentro la classe, non sugli oggetti della classe
class Calcolatrice:
     @staticmethod
     def somma(a, b):
         return a+b
     
# uso il metodo senza creare un'istanza della classe
risultato = Calcolatrice.somma(11, 4)
print("La somma è", risultato)

# metodo di classe - lavora DENTRO la classe e non su un'istanza specifica
class Contatore:
    num_istanze = 0
    
    def __init__(self):
        Contatore.num_istanze += 1
        
    @classmethod
    def mostra_num_istanze(cls):
        print(f"Sono state create {cls.num_istanze} istanze")
        
# creazione di alcune istanze
c1 = Contatore()
c2 = Contatore()

# stampo numero istanze
Contatore.mostra_num_istanze()