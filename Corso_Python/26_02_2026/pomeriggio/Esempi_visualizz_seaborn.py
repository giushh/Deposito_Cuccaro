
import seaborn as sns
import matplotlib.pyplot as plt


"""Grafico a Barre"""

# Dati di esempio
tips = sns.load_dataset("tips")

# Creare un grafico a barre
sns.barplot(x="day", y="total_bill", data=tips)
plt.title('Conto Totale per Giorno')
plt.show()


"""Grafico a Linee"""

# Dati di esempio
fmri = sns.load_dataset("fmri")

# Creare un grafico a linee
sns.lineplot(x="timepoint", y="signal", data=fmri, hue="region", style="event")
plt.title('Segnale FMRI nel Tempo')
plt.show()


"""Istogramma e KDE"""

# Generare dati casuali
data = sns.load_dataset("penguins")

# Creare un istogramma con KDE
sns.histplot(data=data, x="flipper_length_mm", kde=True)
plt.title('Distribuzione Lunghezza Pinne dei Pinguini')
plt.show()