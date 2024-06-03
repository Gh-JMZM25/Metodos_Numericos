# Método de Bisección

## Algoritmo
1. Definir la función \( f(x) \) y los extremos del intervalo \([a, b]\) tal que \( f(a) \cdot f(b) < 0 \).
2. Calcular el punto medio \( c = \frac{a + b}{2} \).
3. Evaluar \( f(c) \).
4. Si \( f(c) = 0 \) o el intervalo es suficientemente pequeño (criterio de convergencia), entonces \( c \) es la raíz.
5. Si \( f(a) \cdot f(c) < 0 \), entonces la raíz está en el intervalo \([a, c]\). De lo contrario, la raíz está en \([c, b]\).
6. Repetir el proceso con el nuevo intervalo hasta que se cumpla el criterio de convergencia.

![](https://github.com/Mexta46/Metodos_Numericos_Tema4/blob/main/Imagenes/Imagenes_tema2/biseccionf.jpg)

## Metodología

### Código en Python para el Método de Bisección
A continuación, se presenta un ejemplo de código en Python para aplicar el método de bisección para encontrar una raíz de la ecuación \( f(x) = 0 \).

```python
def biseccion(f, a, b, tol, Nmax):
    """
    Función para encontrar una raíz de la ecuación f(x) = 0 utilizando el método de bisección.

    Parámetros:
    f (función): Función a evaluar.
    a (float): Extremo inferior del intervalo.
    b (float): Extremo superior del intervalo.
    tol (float): Tolerancia para la convergencia.
    Nmax (int): Número máximo de iteraciones.

    Devuelve:
    float: Solución aproximada.
    int: Número de iteraciones realizadas.
    bool: Indicador de convergencia.
    """
    if f(a) * f(b) >= 0:
        print("La función debe cambiar de signo en el intervalo [a, b]")
        return None, 0, False

    for n in range(1, Nmax + 1):
        c = (a + b) / 2
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            return c, n, True
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

    return c, Nmax, False

# Definición de la función a evaluar
def f(x):
    return x**3 - x - 2

# Parámetros del método
a = 1  # extremo inferior del intervalo
b = 2  # extremo superior del intervalo
tol = 1e-6  # tolerancia
Nmax = 100  # número máximo de iteraciones

# Aplicar el método de bisección
solucion, iteraciones, convergencia = biseccion(f, a, b, tol, Nmax)

# Imprimir resultados
if convergencia:
    print(f"Solución encontrada: {solucion:.6f} en {iteraciones} iteraciones")
else:
    print(f"No se alcanzó la convergencia en {iteraciones} iteraciones")
```

### Ejercicio 2: Resolver \(f(x) = x^2 - 3\) mediante el método de bisección
Utiliza el método de bisección para encontrar la raíz de \(f(x) = x^2 - 3\) en el intervalo [1, 2].

```python
# Definición de la función f(x) = x^2 - 3
def f(x):
    return x**2 - 3

# Intervalo inicial
a = 1
b = 2

# Tolerancia y número máximo de iteraciones
tolerancia = 1e-6
max_iter = 100

# Método de bisección
for i in range(max_iter):
    c = (a + b) / 2
    if f(c) == 0 or (b - a) / 2 < tolerancia:
        break
    if f(c) * f(a) > 0:
        a = c
    else:
        b = c

print(f"Raíz aproximada: {c}")
print(f"Iteraciones: {i+1}")
```

### Ejercicio 3: Resolver \(f(x) = x^3 + x - 1\) mediante el método de bisección
Utiliza el método de bisección para encontrar la raíz de \(f(x) = x^3 + x - 1\) en el intervalo [0, 1].

```python
# Definición de la función f(x) = x^3 + x - 1
def f(x):
    return x**3 + x - 1

# Intervalo inicial
a = 0
b = 1

# Tolerancia y número máximo de iteraciones
tolerancia = 1e-6
max_iter = 100

# Método de bisección
for i in range(max_iter):
    c = (a + b) / 2
    if f(c) == 0 or (b - a) / 2 < tolerancia:
        break
    if f(c) * f(a) > 0:
        a = c
    else:
        b = c

print(f"Raíz aproximada: {c}")
print(f"Iteraciones: {i+1}")
```

### Ejercicio 4: Resolver \(f(x) = \cos(x) - x\) mediante el método de bisección
Utiliza el método de bisección para encontrar la raíz de \(f(x) = \cos(x) - x\) en el intervalo [0, 1].

```python
import numpy as np

# Definición de la función f(x) = cos(x) - x
def f(x):
    return np.cos(x) - x

# Intervalo inicial
a = 0
b = 1

# Tolerancia y número máximo de iteraciones
tolerancia = 1e-6
max_iter = 100

# Método de bisección
for i in range(max_iter):
    c = (a + b) / 2
    if f(c) == 0 or (b - a) / 2 < tolerancia:
        break
    if f(c) * f(a) > 0:
        a = c
    else:
        b = c

print(f"Raíz aproximada: {c}")
print(f"Iteraciones: {i+1}")
```

### Ejercicio 5: Resolver \(f(x) = e^{-x} - x\) mediante el método de bisección
Utiliza el método de bisección para encontrar la raíz de \(f(x) = e^{-x} - x\) en el intervalo [0, 1].

```python
import numpy as np

# Definición de la función f(x) = e^(-x) - x
def f(x):
    return np.exp(-x) - x

# Intervalo inicial
a = 0
b = 1

# Tolerancia y número máximo de iteraciones
tolerancia = 1e-6
max_iter = 100

# Método de bisección
for i in range(max_iter):
    c = (a + b) / 2
    if f(c) == 0 or (b - a) / 2 < tolerancia:
        break
    if f(c) * f(a) > 0:
        a = c
    else:
        b = c

print(f"Raíz aproximada: {c}")
print(f"Iteraciones: {i+1}")
```


### Resultados y Análisis
El código anterior aplica el método de bisección para encontrar una solución de la ecuación \( x^3 - x - 2 = 0 \) en el intervalo \([1, 2]\). El resultado muestra si el método ha convergido a una solución dentro de un número máximo de iteraciones y una tolerancia especificada.
