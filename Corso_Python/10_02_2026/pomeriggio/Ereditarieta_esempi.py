# pomeriggio 10/02/2026

# esempi ereditarietà

# ESEMPIO 1
# Classe base
class Animale:
    def __init__(self, nome):
        self.nome = nome

    def parla(self):
        print(f"{self.nome} fa suono generico.")

# Classe derivata (eredita da Animale)
class Cane(Animale):

    def parla(self):
        print(f"{self.nome} abbaia!")

animale_generico = Animale("AnimaleGenerico")
cane = Cane("Fido")

animale_generico.parla() # Output: AnimaleGenerico fa suono generico.
cane.parla() # Output: Fido abbaia!



# ESEMPIO 2
class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

    def mostra_informazioni(self):
        print(f"Veicolo marca {self.marca}, modello {self.modello}")
    
class DotazioniSpeciali:
    def __init__(self, dotazioni):
        self.dotazioni = dotazioni

    def mostra_dotazioni(self):
        print(f"Dotazioni speciali: {', '.join(self.dotazioni)}")
        
"""
MULTIEREDITARIETA'

Ora, creiamo una classe AutomobileSportiva che eredita sia da Veicolo che da
DotazioniSpeciali, dimostrando l'ereditarietà multipla.
Useremo super() per chiamare i costruttori delle classi base e sovrascriveremo
il metodo mostra_informazioni per aggiungere ulteriori dettagli specifici
dell'AutomobileSportiva.
"""

class AutomobileSportiva(Veicolo, DotazioniSpeciali):
    def __init__(self, marca, modello, dotazioni, cavalli):
        Veicolo.__init__(self, marca, modello)
        
        # Alternativa a super per l'ereditarietà multipla
        DotazioniSpeciali.__init__(self, dotazioni)
        self.cavalli = cavalli

    def mostra_informazioni(self):  # puoi usare sia super() che self, funziona uguale
        super().mostra_informazioni()
        
        # Chiamiamo il metodo della prima superclasse
        print(f"Potenza: {self.cavalli} CV")
        self.mostra_dotazioni()
        # Possiamo chiamare metodi di entrambe le superclassi
        
# creazione oggetti

auto_sportiva1 = AutomobileSportiva("Ferrari", "F8", ["ABS", "Controllo trazione", "Airbag passeggero"], 900)
auto_sportiva1.mostra_informazioni()