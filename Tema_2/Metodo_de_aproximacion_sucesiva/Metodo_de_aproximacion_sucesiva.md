# Método de Aproximación Sucesiva

## Definición
El método de aproximación sucesiva, también conocido como método de iteración de punto fijo, es una técnica utilizada para encontrar soluciones a ecuaciones no lineales de la forma \( x = g(x) \). El método se basa en una función iterativa \( g(x) \) que genera una secuencia de valores que converge hacia la solución deseada.

![](https://github.com/Mexta46/Metodos_Numericos_Tema4/blob/main/Imagenes/Imagenes_tema2/aprox.png)

## Algoritmo
1. Definir la función iterativa \( g(x) \).
2. Elegir un valor inicial \( x_0 \).
3. Especificar un criterio de convergencia (tolerancia \( \epsilon \) y número máximo de iteraciones \( N_{\text{max}} \)).
4. Iterar utilizando la fórmula \( x_{n+1} = g(x_n) \) hasta que se cumpla el criterio de convergencia.
5. Comprobar la convergencia y devolver la solución aproximada.

![](https://github.com/Mexta46/Metodos_Numericos_Tema4/blob/main/Imagenes/Imagenes_tema2/aproxf.jpg)

## Metodología

### Código en Python para el Método de Aproximación Sucesiva
A continuación, se presenta un ejemplo de código en Python para aplicar el método de aproximación sucesiva para encontrar una raíz de la ecuación \( x = g(x) \).

```python
import numpy as np

def aproximacion_sucesiva(g, x0, tol, Nmax):
    """
    Función para encontrar una raíz de la ecuación x = g(x) utilizando el método de aproximación sucesiva.

    Parámetros:
    g (función): Función iterativa.
    x0 (float): Valor inicial.
    tol (float): Tolerancia para la convergencia.
    Nmax (int): Número máximo de iteraciones.

    Devuelve:
    float: Solución aproximada.
    int: Número de iteraciones realizadas.
    bool: Indicador de convergencia.
    """
    x_n = x0
    for n in range(1, Nmax + 1):
        x_n1 = g(x_n)
        if abs(x_n1 - x_n) < tol:
            return x_n1, n, True
        x_n = x_n1
    return x_n, Nmax, False

# Definición de la función iterativa
def g(x):
    return np.cos(x)

# Parámetros del método
x0 = 0.5  # valor inicial
tol = 1e-6  # tolerancia
Nmax = 100  # número máximo de iteraciones

# Aplicar el método de aproximación sucesiva
solucion, iteraciones, convergencia = aproximacion_sucesiva(g, x0, tol, Nmax)

# Imprimir resultados
if convergencia:
    print(f"Solución encontrada: {solucion:.6f} en {iteraciones} iteraciones")
else:
    print(f"No se alcanzó la convergencia en {iteraciones} iteraciones")
```

### Ejercicio 2: Resolver \(x = \cos(x)\) mediante aproximación sucesiva
Utiliza el método de aproximación sucesiva para encontrar la solución de \(x = \cos(x)\).

```python
import numpy as np

# Definición de la función g(x) = cos(x)
def g(x):
    return np.cos(x)

# Valor inicial
x0 = 0.5

# Número máximo de iteraciones
max_iter = 100

# Tolerancia
tolerancia = 1e-6

# Aproximación sucesiva
for i in range(max_iter):
    x1 = g(x0)
    if abs(x1 - x0) < tolerancia:
        break
    x0 = x1

print(f"Solución aproximada: {x1}")
print(f"Iteraciones: {i+1}")
```

### Ejercicio 3: Resolver \(x = \sqrt{3 - x}\) mediante aproximación sucesiva
Utiliza el método de aproximación sucesiva para encontrar la solución de \(x = \sqrt{3 - x}\).

```python
# Definición de la función g(x) = sqrt(3 - x)
def g(x):
    return np.sqrt(3 - x)

# Valor inicial
x0 = 1.0

# Número máximo de iteraciones
max_iter = 100

# Tolerancia
tolerancia = 1e-6

# Aproximación sucesiva
for i in range(max_iter):
    x1 = g(x0)
    if abs(x1 - x0) < tolerancia:
        break
    x0 = x1

print(f"Solución aproximada: {x1}")
print(f"Iteraciones: {i+1}")
```

### Ejercicio 4: Resolver \(x = \frac{1}{1 + x}\) mediante aproximación sucesiva
Utiliza el método de aproximación sucesiva para encontrar la solución de \(x = \frac{1}{1 + x}\).

```python
# Definición de la función g(x) = 1 / (1 + x)
def g(x):
    return 1 / (1 + x)

# Valor inicial
x0 = 0.5

# Número máximo de iteraciones
max_iter = 100

# Tolerancia
tolerancia = 1e-6

# Aproximación sucesiva
for i in range(max_iter):
    x1 = g(x0)
    if abs(x1 - x0) < tolerancia:
        break
    x0 = x1

print(f"Solución aproximada: {x1}")
print(f"Iteraciones: {i+1}")
```

### Ejercicio 5: Resolver \(x = \sin(x) + 0.5\) mediante aproximación sucesiva
Utiliza el método de aproximación sucesiva para encontrar la solución de \(x = \sin(x) + 0.5\).

```python
# Definición de la función g(x) = sin(x) + 0.5
def g(x):
    return np.sin(x) + 0.5

# Valor inicial
x0 = 0.5

# Número máximo de iteraciones
max_iter = 100

# Tolerancia
tolerancia = 1e-6

# Aproximación sucesiva
for i in range(max_iter):
    x1 = g(x0)
    if abs(x1 - x0) < tolerancia:
        break
    x0 = x1

print(f"Solución aproximada: {x1}")
print(f"Iteraciones: {i+1}")
```


### Resultados y Análisis
El código anterior aplica el método de aproximación sucesiva para encontrar una solución de la ecuación \( x = \cos(x) \) a partir de un valor inicial de \( x_0 = 0.5 \). El resultado muestra si el método ha convergido a una solución dentro de un número máximo de iteraciones y una tolerancia especificada.
