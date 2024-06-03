import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

# Definir los puntos conocidos (x, y)
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 1, 4, 9, 16, 25])

# Crear el polinomio de interpolación
polinomio = lagrange(x, y)

# Definir los puntos donde se desea estimar los valores
x_nuevo = np.linspace(0, 5, 50)
y_nuevo = polinomio(x_nuevo)

# Graficar los puntos conocidos y el polinomio de interpolación
plt.plot(x, y, 'o', label='Puntos conocidos')
plt.plot(x_nuevo, y_nuevo, '-', label='Interpolación polinómica')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Interpolación Polinómica')
plt.show()
