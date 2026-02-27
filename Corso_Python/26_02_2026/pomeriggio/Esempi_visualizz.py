import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np



"""Grafico a Linee"""

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.figure()
plt.plot(x, y)
plt.title('Grafico a Linee')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()


"""Grafico a Barre"""

categories = ['A', 'B', 'C', 'D', 'E']
values = [3, 7, 2, 5, 8]

plt.figure()
plt.bar(categories, values)
plt.title('Grafico a Barre')
plt.xlabel('Categorie')
plt.ylabel('Valori')
plt.show()


"""Istogramma"""

data = np.random.randn(1000)

plt.figure()
plt.hist(data, bins=30)
plt.title('Istogramma')
plt.xlabel('Valori')
plt.ylabel('Frequenza')
plt.show()



"""Scatter Plot"""

x = np.random.rand(50)
y = np.random.rand(50)

plt.figure()
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()