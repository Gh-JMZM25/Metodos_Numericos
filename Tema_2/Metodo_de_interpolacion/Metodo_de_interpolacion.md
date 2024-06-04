# Interpolación

## Definición
La interpolación es un método numérico utilizado para estimar valores desconocidos de una función a partir de un conjunto de puntos conocidos. Los métodos de interpolación crean una función continua que pasa a través de todos los puntos dados y se utiliza para estimar valores entre estos puntos.

![](https://github.com/Mexta46/Metodos_Numericos_Tema4/blob/main/Imagenes/Imagenes_tema2/interpolacion.jpg)

## Algoritmo
1. Definir el conjunto de puntos \((x_i, y_i)\) donde \( y_i = f(x_i) \).
2. Elegir el método de interpolación adecuado (e.g., interpolación lineal, interpolación polinómica).
3. Construir la función de interpolación que pase a través de todos los puntos dados.
4. Utilizar la función de interpolación para estimar valores en puntos desconocidos.

![](https://github.com/Mexta46/Metodos_Numericos_Tema4/blob/main/Imagenes/Imagenes_tema2/interpolacionf.png)

## Metodología

### Código en Python para Interpolación Lineal
A continuación, se presenta un ejemplo de código en Python para aplicar la interpolación lineal para estimar valores de una función desconocida a partir de un conjunto de puntos conocidos.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Definir los puntos conocidos (x, y)
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 1, 4, 9, 16, 25])

# Crear la función de interpolación lineal
f_interpolada = interp1d(x, y, kind='linear')

# Definir los puntos donde se desea estimar los valores
x_nuevo = np.linspace(0, 5, 50)
y_nuevo = f_interpolada(x_nuevo)

# Graficar los puntos conocidos y la función de interpolación
plt.plot(x, y, 'o', label='Puntos conocidos')
plt.plot(x_nuevo, y_nuevo, '-', label='Interpolación lineal')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Interpolación Lineal')
plt.show()
```

### Ejercicio 2: Código en Python para Interpolación Polinómica
También se puede utilizar la interpolación polinómica para ajustar un polinomio que pase por todos los puntos conocidos.

```python
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
```
### Ejercicio 3: Interpolación Lineal
Utiliza la interpolación lineal para aproximar el valor de \(f(2.5)\) dados los puntos \((1, 1)\), \((2, 4)\) y \((3, 9)\).

```python
import numpy as np

# Puntos dados
x = np.array([1, 2, 3])
y = np.array([1, 4, 9])

# Valor a interpolar
x_interp = 2.5

# Función de interpolación lineal
def interpolacion_lineal(x, y, x_interp):
    for i in range(len(x) - 1):
        if x[i] <= x_interp <= x[i+1]:
            return y[i] + (y[i+1] - y[i]) * (x_interp - x[i]) / (x[i+1] - x[i])

y_interp = interpolacion_lineal(x, y, x_interp)
print(f"Valor interpolado de f(2.5): {y_interp}")
```

### Ejercicio 4: Interpolación Cuadrática
Utiliza la interpolación cuadrática para aproximar el valor de \(f(2.5)\) dados los puntos \((1, 1)\), \((2, 4)\), \((3, 9)\) y \((4, 16)\).

```python
# Puntos dados
x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])

# Valor a interpolar
x_interp = 2.5

# Función de interpolación cuadrática
def interpolacion_cuadratica(x, y, x_interp):
    n = len(x)
    A = np.zeros((n, n))
    b = y.copy()

    # Construir la matriz de Vandermonde
    for i in range(n):
        A[i] = [x[i]**j for j in range(n)]

    # Resolver el sistema de ecuaciones
    coeficientes = np.linalg.solve(A, b)

    # Evaluar el polinomio en x_interp
    y_interp = sum(coeficientes[j] * x_interp**j for j in range(n))
    return y_interp

y_interp = interpolacion_cuadratica(x, y, x_interp)
print(f"Valor interpolado de f(2.5): {y_interp}")
```

### Ejercicio 5: Interpolación de Lagrange
Utiliza la interpolación de Lagrange para aproximar el valor de \(f(2.5)\) dados los puntos \((1, 1)\), \((2, 8)\), \((3, 27)\) y \((4, 64)\).

```python
# Puntos dados
x = np.array([1, 2, 3, 4])
y = np.array([1, 8, 27, 64])

# Valor a interpolar
x_interp = 2.5

# Función de interpolación de Lagrange
def interpolacion_lagrange(x, y, x_interp):
    n = len(x)
    y_interp = 0

    for i in range(n):
        L = 1
        for j in range(n):
            if i != j:
                L *= (x_interp - x[j]) / (x[i] - x[j])
        y_interp += y[i] * L

    return y_interp

y_interp = interpolacion_lagrange(x, y, x_interp)
print(f"Valor interpolado de f(2.5): {y_interp}")
```


### Resultados y Análisis.
Los códigos anteriores aplican la interpolación lineal y polinómica a un conjunto de puntos conocidos. Los resultados se muestran en gráficos que ilustran cómo la función de interpolación pasa a través de todos los puntos conocidos y estima valores en puntos intermedios.
