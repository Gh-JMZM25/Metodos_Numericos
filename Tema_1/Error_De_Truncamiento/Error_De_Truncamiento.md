# Error de Truncamiento

### Definición
El error de truncamiento es la diferencia entre el valor exacto de una función matemática y su aproximación obtenida al utilizar una serie finita de términos en un método numérico. Este tipo de error se introduce al truncar una serie infinita o al realizar aproximaciones numéricas.

![](https://github.com/Mexta46/Metodos_Numericos_Tema4/blob/main/Imagenes/Imagenes_tema1/truncamiento.jpeg)

## Algoritmo
1. Definir la función f(x) y su aproximación g(x) que introduce el error de truncamiento.
2. Especificar el intervalo de evaluación [a, b].
3. Dividir el intervalo [a, b] en n subintervalos de igual tamaño.
4. Calcular el valor exacto de f(x) en puntos específicos del intervalo.
5. Calcular el valor aproximado de g(x) en los mismos puntos.
6. Comparar los valores exactos y aproximados para determinar el error de truncamiento.
7. Analizar cómo varía el error de truncamiento a lo largo del intervalo.
8. Devolver los valores calculados como análisis del error de truncamiento.

![](https://github.com/Mexta46/Metodos_Numericos_Tema4/blob/main/Imagenes/Imagenes_tema1/truncamientof.png)

## Metodología

### Código en Python para Evaluar el Error de Truncamiento
A continuación, se presenta un ejemplo de código en Python para evaluar el error de truncamiento en la función \( f(x) = e^x \) y su aproximación mediante una serie de Taylor truncada en el intervalo [0, 1].

```python
import numpy as np

def calcular_error_truncamiento(f, g, a, b, n):
    """
    Función para calcular el error de truncamiento en la evaluación de una función f(x) y su aproximación g(x) en el intervalo [a, b].

    Parámetros:
    f (función): Función exacta a evaluar.
    g (función): Función aproximada que introduce el error de truncamiento.
    a (float): Límite inferior del intervalo.
    b (float): Límite superior del intervalo.
    n (int): Número de subintervalos.

    Devuelve:
    list: Lista de errores de truncamiento en los puntos del intervalo.
    """
    h = (b - a) / n  # tamaño del subintervalo
    valores_exactos = []
    valores_aproximados = []
    errores = []

    for i in range(n + 1):
        x = a + i * h
        valor_exacto = f(x)
        valor_aproximado = g(x)
        valores_exactos.append(valor_exacto)
        valores_aproximados.append(valor_aproximado)
        error = abs(valor_exacto - valor_aproximado)
        errores.append(error)

    return errores, valores_exactos, valores_aproximados

# Definición de la función exacta y su aproximación
def f(x):
    return np.exp(x)

def g(x):
    # Aproximación de la serie de Taylor truncada a x^2
    return 1 + x + (x**2) / 2

# Parámetros del intervalo
a = 0
b = 1
n = 10  # número de subintervalos

# Calcular errores de truncamiento
errores, valores_exactos, valores_aproximados = calcular_error_truncamiento(f, g, a, b, n)

# Imprimir resultados
print("x\tValor Exacto\tValor Aproximado\tError de Truncamiento")
for i in range(n + 1):
    x = a + i * h
    print(f"{x:.2f}\t{valores_exactos[i]:.5f}\t{valores_aproximados[i]:.5f}\t{errores[i]:.5f}")
```

### Ejercicio 2: Aproximación de una derivada utilizando diferencias finitas
Aproximar la derivada de una función en un punto utilizando el método de diferencias finitas hacia adelante y analizar el error de truncamiento.

```python
import numpy as np

# Definición de la función
def f(x):
    return np.sin(x)

# Punto donde se evaluará la derivada
x = np.pi / 4

# Incremento pequeño
h = 0.1

# Derivada exacta
derivada_exacta = np.cos(x)

# Aproximación de la derivada usando diferencias finitas hacia adelante
derivada_aproximada = (f(x + h) - f(x)) / h

# Error de truncamiento
error_truncamiento = abs(derivada_exacta - derivada_aproximada)

print(f"Derivada exacta: {derivada_exacta}")
print(f"Derivada aproximada: {derivada_aproximada}")
print(f"Error de truncamiento: {error_truncamiento}")
```

### Ejercicio 3: Aproximación de una integral utilizando la regla del trapecio
Aproximar una integral definida utilizando la regla del trapecio y analizar el error de truncamiento.

```python
# Definición de la función
def f(x):
    return np.exp(-x**2)

# Límites de integración
a = 0
b = 1

# Número de subdivisiones
n = 10

# Ancho de cada subdivisión
h = (b - a) / n

# Integral exacta (para comparación)
integral_exacta = 0.746824  # Aproximación de la integral de 0 a 1 de exp(-x^2) dx

# Aproximación de la integral usando la regla del trapecio
x = np.linspace(a, b, n+1)
y = f(x)
integral_aproximada = (h/2) * (y[0] + 2*sum(y[1:-1]) + y[-1])

# Error de truncamiento
error_truncamiento = abs(integral_exacta - integral_aproximada)

print(f"Integral exacta: {integral_exacta}")
print(f"Integral aproximada: {integral_aproximada}")
print(f"Error de truncamiento: {error_truncamiento}")
```

### Ejercicio 4: Serie de Taylor truncada
Aproximar el valor de \(\sin(x)\) usando una serie de Taylor truncada y analizar el error de truncamiento.

```python
# Definición del valor de x
x = np.pi / 4

# Número de términos de la serie de Taylor
n = 3

# Valor exacto de sin(x)
valor_exacto = np.sin(x)

# Aproximación usando la serie de Taylor truncada
valor_aproximado = 0
for i in range(n):
    valor_aproximado += ((-1)**i * x**(2*i+1)) / np.math.factorial(2*i+1)

# Error de truncamiento
error_truncamiento = abs(valor_exacto - valor_aproximado)

print(f"Valor exacto de sin({x}): {valor_exacto}")
print(f"Valor aproximado usando la serie de Taylor truncada: {valor_aproximado}")
print(f"Error de truncamiento: {error_truncamiento}")
```

### Ejercicio 5: Diferencias finitas para aproximar la segunda derivada
Aproximar la segunda derivada de una función en un punto utilizando diferencias finitas y analizar el error de truncamiento.

```python
# Definición de la función
def f(x):
    return np.exp(x)

# Punto donde se evaluará la segunda derivada
x = 1.0

# Incremento pequeño
h = 0.1

# Segunda derivada exacta
segunda_derivada_exacta = np.exp(x)

# Aproximación de la segunda derivada usando diferencias finitas
segunda_derivada_aproximada = (f(x + h) - 2*f(x) + f(x - h)) / h**2

# Error de truncamiento
error_truncamiento = abs(segunda_derivada_exacta - segunda_derivada_aproximada)

print(f"Segunda derivada exacta: {segunda_derivada_exacta}")
print(f"Segunda derivada aproximada: {segunda_derivada_aproximada}")
print(f"Error de truncamiento: {error_truncamiento}")
```


### Resultados y Análisis
El código anterior genera una tabla que muestra el valor exacto, el valor aproximado (usando una serie de Taylor truncada) y el error de truncamiento en varios puntos del intervalo [0, 1]. Analizando estos resultados, se puede observar cómo el error de truncamiento varía a lo largo del intervalo y entender mejor su comportamiento y magnitud.
