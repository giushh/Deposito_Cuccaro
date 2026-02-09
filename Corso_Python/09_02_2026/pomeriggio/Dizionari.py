# pomeriggio 09/02/2026

# Dizionari 

persona = {"nome": "Ilaria", "cognome":"Cuccaro"}

print(f"Nome: {persona["nome"]}, Cognome: {persona["cognome"]}")
print("Prova stampa dizionario intero: ", persona)

persona["età"] = 27
print("Prova stampa dizionario intero: ", persona)


# esempi mirko 
"""
PANORAMICA COMPLETA SUI DIZIONARI IN PYTHON
- Creazione e accesso
- Aggiunta, modifica e rimozione
- Cicli sui dizionari
- Dizionari annidati
- Dizionari con liste
- Funzioni che usano dizionari
- Pattern pratici (conteggi, lookup, aggregazione)
"""

# ==============================================================
# 1. CREAZIONE DI UN DIZIONARIO
# ==============================================================

persona = {
    "nome": "Mario",
    "eta": 30,
    "citta": "Roma"
}

print("Dizionario persona:", persona)


# ==============================================================
# 2. ACCESSO AI VALORI
# ==============================================================

print("Nome:", persona["nome"])
print("Età:", persona.get("eta"))           # get evita errori
print("Telefono:", persona.get("telefono", "Non presente"))


# ==============================================================
# 3. AGGIUNTA E MODIFICA DI ELEMENTI
# ==============================================================

persona["professione"] = "Ingegnere"        # aggiunta
persona["eta"] = 31                         # modifica
print("\nDopo aggiunta/modifica:", persona)


# ==============================================================
# 4. RIMOZIONE DI ELEMENTI
# ==============================================================

del persona["citta"]                        # rimozione diretta
prof = persona.pop("professione")           # rimuove e restituisce
print("\nProfessione rimossa:", prof)
print("Dizionario finale:", persona)


# ==============================================================
# 5. CICLI SUI DIZIONARI
# ==============================================================

print("\n=== Ciclo sulle chiavi ===")
for chiave in persona:
    print(chiave)

print("\n=== Ciclo sui valori ===")
for valore in persona.values():
    print(valore)

print("\n=== Ciclo chiave-valore ===")
for k, v in persona.items():
    print(k, "->", v)


# ==============================================================
# 6. VERIFICA ESISTENZA CHIAVI
# ==============================================================

if "nome" in persona:
    print("\nLa chiave 'nome' esiste")

if "telefono" not in persona:
    print("La chiave 'telefono' NON esiste")


# ==============================================================
# 7. DIZIONARI ANNIDATI
# ==============================================================

studenti = {
    "s1": {"nome": "Anna", "voto": 28},
    "s2": {"nome": "Luca", "voto": 30},
    "s3": {"nome": "Marco", "voto": 25}
}

print("\n=== Dizionario annidato (studenti) ===")
for id_studente, dati in studenti.items():
    print(id_studente, dati["nome"], dati["voto"])


# ==============================================================
# 8. DIZIONARI CON LISTE COME VALORI
# ==============================================================

classe = {
    "presenti": ["Anna", "Luca", "Marco"],
    "assenti": ["Giulia"]
}

classe["presenti"].append("Sara")
print("\nClasse:", classe)


# ==============================================================
# 9. FUNZIONE CHE USA UN DIZIONARIO
# ==============================================================

def stampa_persona(p):
    print("\n--- Persona ---")
    for k, v in p.items():
        print(k.capitalize(), ":", v)

stampa_persona(persona)


# ==============================================================
# 10. FUNZIONE CHE MODIFICA UN DIZIONARIO
# ==============================================================

def compleanno(p):
    p["eta"] += 1

compleanno(persona)
print("\nEtà dopo compleanno:", persona["eta"])


# ==============================================================
# 11. PATTERN PRATICO: CONTEGGIO OCCORRENZE
# ==============================================================

parole = ["python", "java", "python", "c", "java", "python"]
conteggio = {}

for parola in parole:
    if parola in conteggio:
        conteggio[parola] += 1
    else:
        conteggio[parola] = 1

print("\nConteggio parole:", conteggio)


# ==============================================================
# 12. STESSO PATTERN CON get()
# ==============================================================

conteggio2 = {}
for parola in parole:
    conteggio2[parola] = conteggio2.get(parola, 0) + 1

print("Conteggio parole (con get):", conteggio2)


# ==============================================================
# 13. DIZIONARIO COME LOOKUP TABLE
# ==============================================================

operazioni = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b
}

a, b = 5, 3
op = "*"
print(f"\nOperazione {a} {op} {b} =", operazioni[op](a, b))


# ==============================================================
# 14. COPIA DI DIZIONARI
# ==============================================================

originale = {"a": 1, "b": 2}
copia = originale.copy()
copia["a"] = 99

print("\nOriginale:", originale)
print("Copia:", copia)


# ==============================================================
# 15. PULIZIA COMPLETA
# ==============================================================

copia.clear()
print("\nCopia dopo clear():", copia)