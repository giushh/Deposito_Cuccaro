"""
Dataset autogenerato con 30 temperature giornaliere.

Calcola:
- Temperatura massima
- Temperatura minima
- Temperatura media
- Mediana

Visualizza nella stessa figura:
- Grafico a linee con evidenziazione di max, min e media
  con piccole label sui punti
- Istogramma con linea della mediana
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

""" SPIEGAZIONE
Media → equilibrio numerico
Mediana → punto centrale
Moda → valore più frequente

Media → “in media questo mese ha fatto 22°”
Mediana → “metà dei giorni è sotto 21°, metà sopra”
Moda → “la temperatura più ricorrente è stata 24°”
"""

temperature = np.random.randint(10, 36, 30)
df = pd.DataFrame(temperature, columns=["temperature"])


temperatura_massima = df["temperature"].max()
temperatura_minima = df["temperature"].min()
temperatura_media = df["temperature"].mean()
temperatura_mediana = df["temperature"].median()

giorno_max = df["temperature"].idxmax()
giorno_min = df["temperature"].idxmin()

print("Temperatura massima:", temperatura_massima)
print("Temperatura minima:", temperatura_minima)
print("Temperatura media:", round(temperatura_media, 2))
print("Mediana:", temperatura_mediana)


plt.figure(figsize=(12,5))

# ---- Grafico a linee con annotazioni ----
plt.subplot(1,2,1)
plt.plot(df["temperature"])
plt.title("Andamento Temperature")
plt.xlabel("Giorno")
plt.ylabel("Temperatura")

# punto massimo
plt.scatter(giorno_max, temperatura_massima)
plt.text(giorno_max, temperatura_massima,
         f" Max: {temperatura_massima}",
         verticalalignment="bottom")

# punto minimo
plt.scatter(giorno_min, temperatura_minima)
plt.text(giorno_min, temperatura_minima,
         f" Min: {temperatura_minima}",
         verticalalignment="top")

# linea media
plt.axhline(temperatura_media)
plt.text(0, temperatura_media,
         f" Media: {round(temperatura_media,2)}",
         verticalalignment="bottom")

# ---- Istogramma con mediana ----
plt.subplot(1,2,2)
plt.hist(df["temperature"], bins=8)
plt.axvline(temperatura_mediana)
plt.title("Distribuzione Temperature")
plt.xlabel("Temperatura")
plt.ylabel("Frequenza")

plt.tight_layout()
plt.show()