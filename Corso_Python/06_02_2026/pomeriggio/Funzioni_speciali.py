# pomeriggio 06/02/2026

# esempi di funzioni generatori e decoratori

# GENERATORI - yield

def fibonacci(n):
    a, b = 0, 1

    while a < n:
        yield a
        # qui la funzione si ferma, passa il controllo a chi l'ha chiamata, "salva" lo stato corrente per poter riprendere quando gli torna il controllo
        a, b = b, a+b
        
        
n = int(input("Dimmi un numero: "))

print(list(fibonacci(n))) # crea la lista un elemento alla volta che prende dalla funzione fibonacci(n)

# alternativa

for x in list(fibonacci(n)):        # è come uno splat, ma non tutto insieme, lo fa un pezzo alla volta, ogni singola iterazione
    print(x)
    

def conta_fino_a(n):
    i = 1
    while i <= n:
        yield i
        i += 1
        
print(list(conta_fino_a(n)))        # il print rimane aperto, aspetta che ritornano i valori dal yield
# questa lista non viene salvata, viene solo stampata, ottimo per non salvare dati sensibili

# catena di generatori 
def catena_generatori():
    # Prima produce 1..3, poi 10..12
    yield from range(1, 4)
    # from serve a dire prendi i valori da quello che segue
    # altrimenti avresti dovuto fare due liste con splat e range e prendere i lavori da là
    yield from range(10, 13)

print("\nEsempio catena generatori")   
print(list(catena_generatori()))
# finisce prima tutti i ritorni del primo yield e poi inizia l'altro
# in questo modo posso andare a fare dei controlli e modifiche PRIMA del secondo yield



# DECORATORI

x = input("Come ti chiami?")

def decoratore(funzione):
    def wrapper(nome):
        print("[PRIMA] - eseguo prima")
        funzione(nome)
        print("[DOPO] - eseguo dopo")
    return wrapper

# applico il decoratore che ho creato alla funzione saluta
@decoratore
def saluta(nome):
    print("Ciao", nome,"!")
    
saluta(x)

# esempio con parametri generici *args e **kwargs

def decoratore_con_argomenti(funzione):
    def wrapper(*args, **kwargs):
        print("\nPrima")
        risultato = funzione(*args, **kwargs)
        print("Dopo")
        return risultato
    return wrapper

@decoratore_con_argomenti
def somma(a, b):
    print(a+b)
    return a + b

print("risultato è ", somma(3, 4))


# esempio decoratore log
print("\nEsempio log\n")
def logger(funzione):
    def wrapper(*args, **kwargs):
        print(f"[PRIMA] Chiamata a {funzione.__name__} con argomenti: {args} e {kwargs}")
        risultato = funzione(*args, **kwargs)
        print(risultato)
        print(f"[DOPO] Risultato di {funzione.__name__}: {risultato}")
        # return risultato
    return wrapper

@logger
def moltiplica(a, b):
    return a * b

# Chiamata alla funzione decorata
moltiplica(3, 4)