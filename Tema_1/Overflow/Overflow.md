# Overflow

### Definición
El overflow (desbordamiento) ocurre cuando un cálculo produce un resultado que es mayor que el valor máximo que puede ser representado con el tipo de datos numérico utilizado en el sistema de cómputo. Esto puede llevar a resultados incorrectos o a la pérdida de información.

![](https://github.com/Mexta46/Metodos_Numericos_Tema4/blob/main/Imagenes/Imagenes_tema1/overflow.png)

## Algoritmo
1. Definir la función f(x) cuyo cálculo puede llevar al overflow.
2. Especificar el intervalo de evaluación [a, b].
3. Dividir el intervalo [a, b] en n subintervalos de igual tamaño.
4. Calcular el valor de f(x) en puntos específicos del intervalo.
5. Detectar si ocurre overflow y manejarlo adecuadamente.
6. Analizar cómo y dónde ocurre el overflow a lo largo del intervalo.
7. Devolver los valores calculados y las instancias de overflow detectadas.

![](https://github.com/Mexta46/Metodos_Numericos_Tema4/blob/main/Imagenes/Imagenes_tema1/overflowf.png)

## Implementación de los métodos en python
### Ejercicio 1: Evaluar el Overflow
#### Metodología en código

A continuación, se presenta un ejemplo de código en Python para evaluar el problema de overflow en la función \( f(x) = e^x \) en el intervalo [0, 50].

```python
import numpy as np

def calcular_overflow(f, a, b, n):
    """
    Función para detectar overflow en la evaluación de una función f(x) en el intervalo [a, b].

    Parámetros:
    f (función): Función a evaluar.
    a (float): Límite inferior del intervalo.
    b (float): Límite superior del intervalo.
    n (int): Número de subintervalos.

    Devuelve:
    list: Lista de valores calculados y marcas de overflow en los puntos del intervalo.
    """
    h = (b - a) / n  # tamaño del subintervalo
    valores = []
    overflows = []

    for i in range(n + 1):
        x = a + i * h
        try:
            valor = f(x)
            valores.append(valor)
            overflows.append(False)
        except OverflowError:
            valores.append(float('inf'))  # Usar infinito para marcar overflow
            overflows.append(True)

    return valores, overflows

# Definición de la función a evaluar
def f(x):
    return np.exp(x)

# Parámetros del intervalo
a = 0
b = 50
n = 10  # número de subintervalos

# Calcular valores y detectar overflow
valores, overflows = calcular_overflow(f, a, b, n)

# Imprimir resultados
print("x\tValor\t\tOverflow")
h = (b - a) / n
for i in range(n + 1):
    x = a + i * h
    overflow = "Sí" if overflows[i] else "No"
    print(f"{x:.2f}\t{valores[i]:.5e}\t{overflow}")
```
### Comprobación 
![IMG-20240603-WA0106.jpg](https://i.postimg.cc/rpF0K5f9/IMG-20240603-WA0106.jpg)
### Ejercicio 2: Desbordamiento en una operación exponencial
#### Metodología en código

Investigar el desbordamiento al calcular una potencia muy grande.

```python
import numpy as np

# Valor base y exponente
base = 10
exponente = 308

try:
    resultado = np.power(base, exponente)
    print(f"Resultado de {base}^{exponente}: {resultado}")
except OverflowError as e:
    print(f"Error de desbordamiento: {e}")
```
### Comprobación
![IMG-20240603-WA0104.jpg](https://i.postimg.cc/nzGv6nSd/IMG-20240603-WA0104.jpg)
### Ejercicio 3: Desbordamiento en un bucle factorial
#### Metodología en código

Calcular el factorial de un número grande y observar el desbordamiento.

```python
import math

# Número grande para calcular el factorial
numero = 170

try:
    resultado = math.factorial(numero)
    print(f"Factorial de {numero}: {resultado}")
except OverflowError as e:
    print(f"Error de desbordamiento: {e}")
```
### Comprobación 
![IMG-20240603-WA0105.jpg](https://i.postimg.cc/5NTFKHN4/IMG-20240603-WA0105.jpg)
### Ejercicio 4: Desbordamiento en una serie geométrica
#### Metodología en código

Investigar el desbordamiento al sumar una serie geométrica con una razón mayor que 1.

```python
# Parámetros de la serie geométrica
a = 1  # Primer término
r = 1.1  # Razón
n = 100  # Número de términos

try:
    suma = sum(a * r**i for i in range(n))
    print(f"Suma de la serie geométrica: {suma}")
except OverflowError as e:
    print(f"Error de desbordamiento: {e}")
```
### Comprobación 
![IMG-20240603-WA0103.jpg](https://i.postimg.cc/qRvRv0MD/IMG-20240603-WA0103.jpg)
### Ejercicio 5: Desbordamiento en una multiplicación iterativa
#### Metodología en código

Calcular el producto de una serie de números grandes y observar el desbordamiento.

```python
# Lista de números grandes
numeros = [1e154, 2e154, 3e154, 4e154]

try:
    producto = 1
    for numero in numeros:
        producto *= numero
    print(f"Producto de los números: {producto}")
except OverflowError as e:
    print(f"Error de desbordamiento: {e}")
```
### Comprobación 
![IMG-20240603-WA0102.jpg](https://i.postimg.cc/3R8y0m9B/IMG-20240603-WA0102.jpg)


### Resultados y Análisis.
El código anterior genera una tabla que muestra el valor de la función y si ocurrió overflow en varios puntos del intervalo [0, 50]. Analizando estos resultados, se puede observar cómo y dónde ocurre el overflow, lo que ayuda a entender mejor las limitaciones de representación numérica y el comportamiento de la función en estos casos.
