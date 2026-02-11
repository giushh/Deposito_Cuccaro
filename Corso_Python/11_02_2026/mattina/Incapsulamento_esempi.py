# mattina 11/02/2026

# esempi incapsulamento
class Computer:
    def __init__(self, nome_proc):
        self.__processore = "Intel i5" # Attributo privato

    def get_processore(self):
        return self.__processore

    def set_processore(self, processore):
        self.__processore = processore

pc = Computer("Intel i5")

print(pc.get_processore())
# Accede all'attributo privato tramite il getter
pc.set_processore("AMD Ryzen 5")
# Modifica l'attributo privato tramite il setter
print(pc.get_processore())


# variabili globali, locali, non-local

# Variabile globale
numero = 10

def funzione_esterna():
    # Variabile locale nella funzione esterna
    numero = 5
    print("Numero dentro funzione_esterna (locale):", numero)

    def funzione_interna():
        # Utilizzo nonlocal per modificare la variabile locale della funzione esterna
        nonlocal numero # non-local dice che il valore di questo numero sovrascrive quello fuori, vale per tutto il blocco
        numero = 3
        print("Numero dentro funzione_interna (nonlocal):", numero)

    funzione_interna()

    print("Numero nel main (globale):", numero)
    funzione_esterna()
    print("Numero nel main dopo chiamata (globale non cambiato):", numero)
    
    
    
class MiaClasse:
    def __init__(self):
        self.__variabile_privata = "Sono privata"

    def __metodo_privato(self):
        return "Questo è un metodo privato"

obj = MiaClasse()
# Stampando direttamente la variabile privata solleverà un'eccezione
# print(obj.__variabile_privata) # AttributeError
# L'accesso corretto (che dovrebbe essere evitato) sarebbe:
print(obj._MiaClasse__variabile_privata) # Funzionerà, ma non è buona prassi

#   ********** ESEMPI MIRKO **********

class Encapsulated:
    def __init__(self, name, age):
        # Imposta gli attributi interni
        self._name = name
        self._age = age

    def __getattribute__(self, attr):
        # Intercetta ogni accesso agli attributi
        print(f"__getattribute__: Accesso a '{attr}'")
        return object.__getattribute__(self, attr)

    def __getattr__(self, attr):
        # Chiamato solo se l'attributo non esiste
        print(f"__getattr__: '{attr}' non trovato, restituisco None")
        return None

    def __setattr__(self, attr, value):
        # Controlla ogni assegnazione agli attributi
        print(f"__setattr__: Impostazione di '{attr}' a {value}")
        object.__setattr__(self, attr, value)

    def __delattr__(self, attr):
        # Controlla l'eliminazione degli attributi
        print(f"__delattr__: Eliminazione dell'attributo '{attr}'")
        object.__delattr__(self, attr)

    @property
    def name(self):
        # Getter per la proprietà 'name'
        print("property getter: Recupero 'name'")
        return self._name

    @name.setter
    def name(self, value):
        # Setter per la proprietà 'name'
        print("property setter: Imposto 'name' a", value)
        self._name = value

    @name.deleter
    def name(self):
        # Deleter per la proprietà 'name'
        print("property deleter: Eliminazione di 'name'")
        del self._name


if __name__ == '__main__':
    print("Creazione dell'oggetto Encapsulated:")
    obj = Encapsulated("Alice", 30)
    print()

    # Accesso diretto tramite property e attributo
    print("Accesso a 'name' tramite property:")
    print(obj.name)  # Attiva __getattribute__ e il getter della property
    print()

    print("Accesso diretto a '_age':")
    print(obj._age)  # Attiva __getattribute__
    print()

    # Accesso ad un attributo inesistente per attivare __getattr__
    print("Tentativo di accesso a 'salary' (non esistente):")
    print(obj.salary)
    print()

    # Uso dei built-in getattr, setattr, hasattr, delattr
    print("Uso di hasattr per 'name':", hasattr(obj, "name"))
    print("Uso di getattr per 'name':", getattr(obj, "name"))
    print()

    print("Uso di setattr per aggiornare 'name' a 'Bob':")
    setattr(obj, "name", "Bob")  # Attiva __setattr__ e il setter della property
    print("Nome aggiornato:", obj.name)
    print()

    print("Uso di delattr per eliminare l'attributo '_age':")
    delattr(obj, "_age")  # Attiva __delattr__
    print("Tentativo di accesso a '_age' dopo eliminazione:",
          getattr(obj, "_age", "Non trovato"))
    print()

    print("Uso del deleter della property 'name':")
    del obj.name  # Attiva il deleter della property, e di conseguenza __delattr__
    print("Tentativo di accesso a 'name' dopo eliminazione:",
          getattr(obj, "name", "Non trovato"))