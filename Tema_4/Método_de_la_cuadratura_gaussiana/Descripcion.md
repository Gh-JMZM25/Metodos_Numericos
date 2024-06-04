# Metodo de la Cuadratura Gaussiana

## Definición
La cuadratura de Gauss es un método numérico utilizado para aproximar la integral definida de una función. Se basa en la idea de seleccionar puntos de evaluación y pesos de manera óptima para obtener resultados precisos al integrar polinomios de grado 2n-1 o menos S1.

## Algoritmo

1. Determinar los puntos de Gauss y los pesos correspondientes para el intervalo y el orden de precisión deseados. Los puntos de Gauss y los pesos se calculan utilizando la teoría de polinomios ortogonales y la fórmula de cuadratura de Gauss.
2. Evaluar la función en los puntos de Gauss obtenidos en el paso anterior.
3. Calcular el valor aproximado de la integral como la suma ponderada de los valores de la función en los puntos de Gauss, utilizando los pesos correspondientes.

## Implementación de los metodos en python
### Ejercicio 1
#### Metodologia en codigo

∫(0 a 1) e^(-x^2) dx

```python
import math

# Definimos la función que queremos integrar
def funcion(x):
    """
    Función a integrar.
    
    Parámetros:
        x (float): Valor en el que se evalúa la función.
    
    Retorna:
        float: Valor de la función evaluada en x.
    """
    return math.exp(-x**2)

# Definimos la función que realiza la cuadratura gaussiana
def cuadratura_gaussiana(a, b, n):
    """
    Aproxima el valor de una integral definida utilizando el método de cuadratura gaussiana.
    
    Parámetros:
        a (float): Límite inferior de integración.
        b (float): Límite superior de integración.
        n (int): Número de puntos de Gauss.
    
    Retorna:
        float: Aproximación de la integral definida.
    """
    # Coeficientes y nodos de los puntos de Gauss predefinidos
    coeficientes = {2: [1.0, 1.0], 
                    3: [0.5555555556, 0.8888888889, 0.5555555556], 
                    4: [0.3478548451, 0.6521451549, 0.6521451549, 0.3478548451], 
                    5: [0.2369268851, 0.4786286705, 0.5688888889, 0.4786286705, 0.2369268851], 
                    6: [0.1713244924, 0.3607615730, 0.4679139346, 0.4679139346, 0.3607615730, 0.1713244924]}
    nodos = {2: [-0.5773502692, 0.5773502692], 
             3: [0.0, -0.7745966692, 0.7745966692],
             4: [-0.3399810436, 0.3399810436, -0.8611363116, 0.8611363116], 
             5: [0.0, -0.5384693101, 0.5384693101, -0.9061798459, 0.9061798459], 
             6: [0.6612093865, -0.6612093865, -0.2386191861, 0.2386191861, -0.9324695142, 0.9324695142]}
    
    suma = 0
    # Iteramos sobre los puntos de Gauss
    for i in range(n):
        # Transformamos los nodos de Gauss al intervalo [a, b]
        xi = ((b - a) * nodos[n][i] + a + b) / 2
        # Sumamos la contribución de cada punto ponderada por su coeficiente
        suma += coeficientes[n][i] * funcion(xi)
    
    # Multiplicamos por el factor de escala y devolvemos el resultado
    return (b - a) / 2 * suma

# Definimos los límites de integración y el número de puntos de Gauss
limite_inferior = 0
limite_superior = 1
numero_puntos_gauss = 4

# Calculamos el resultado de la integral utilizando cuadratura gaussiana
resultado_integral = cuadratura_gaussiana(limite_inferior, limite_superior, numero_puntos_gauss)

# Imprimimos el resultado
print("El resultado de la integral es:", resultado_integral)
```
### Ejecución
[![image.png](https://i.postimg.cc/1XTjZGHv/image.png)](https://postimg.cc/30XBXDzG)

### Ejercicio 2
#### Metodologia en codigo

∫(0 a 1) (1 - x^2) dx

```python
import numpy as np

def f(x):
   """
   Función a integrar: f(x) = 1 - x^2
   """
   return 1 - x**2

# Definir los límites de integración
a = 0
b = 1

# Puntos y pesos de la cuadratura gaussiana de orden 2
x = np.array([np.sqrt(1/3), -np.sqrt(1/3)])
w = np.array([1, 1])

# Cambio de variable para ajustar el intervalo de integración
u = (b - a) * x / 2 + (a + b) / 2

# Calcular la integral aproximada utilizando la cuadratura gaussiana
i = (b - a) * np.sum(w * f(u)) / 2

print(i)
```
### Ejecución
[![image.png](https://i.postimg.cc/SxctwzzG/image.png)](https://postimg.cc/SnNr9RdX)

### Ejercicio 3
#### Metodologia en codigo

∫ {0.2}^{1.2} e^{x^2} \, dx \]

```python
import numpy as np
from scipy.special import roots_legendre

#Metodo  Cuadratura Gaussiana:

# La cuadratura Gaussiana es un método numérico para aproximar integrales definidas.
# La idea es utilizar pesos y nodos específicos para mejorar la precisión de la aproximación.


#Fórmula:

# ∫[a,b] f(x) dx ≈ ∑[i=1,n] w_i * f((b-a)/2 * x_i + (a+b)/2)

# Simbologia:

#    - f(x) es la función a integrar
#    - [a, b] es el intervalo de integración
#    - n es el número de nodos
#    - x_i son los nodos de integración
#    - w_i son los pesos asociados a los nodos de integración

String = "f(x) = e^(x^2)"

# Paso 2: Define la función

def f(x):
    return np.exp(x**2)

# 1.1 Determinar puntos de gauss

a, b = 0.2, 1.2
n = 2

# 1.2 Determinar los pesos y nodos

def gauss_legendre_nodes_weights(n):
    nodes, weights = roots_legendre(n)
    return nodes, weights


def cuadratura_gaussiana():
    x, w = gauss_legendre_nodes_weights(n)

    # Aplica la fórmula de Cuadratura Gaussiana
    integral = sum(w * f((b-a)/2 * x + (a+b)/2))

    # Calculo del valor [a, b]
    integral *= (b-a)/2
    return integral

resultado_cuadratura_gaussiana = cuadratura_gaussiana()

# Resultados
print("")
print("La ecuación ingresada es: ", String)
print("El parámetro a o límite inferior es: ", a)
print("El parámetro b o límite superior es: ", b)
print("El n de interacciones es: ", n)
print("Método de la Cuadratura Gaussiana:", resultado_cuadratura_gaussiana)
print("")
print("Bibliografía: https://www.youtube.com/watch?v=7fHyO8nfPIU&ab_channel=AlejandroSandovalRamos")
```
### Ejecución
[![image.png](https://i.postimg.cc/rm7PBGgQ/image.png)](https://postimg.cc/7GM972F2)

### Ejercicio 4
#### Metodologia en codigo

∫{-1}^{1} e^{-x^2} \, dx \]

```python
import numpy as np

def calcular_pesos_y_abscisas(n):
    # Función para calcular los pesos y las abscisas de los puntos de Gauss
    # Utilizaremos la fórmula de los polinomios de Legendre para obtener estos valores
    # Aquí solo se muestra una implementación simple para n=2 y n=3, pero pueden definirse para más nodos
    if n == 2:
        return np.array([1, 1]), np.array([-1/np.sqrt(3), 1/np.sqrt(3)])
    elif n == 3:
        return np.array([5/9, 8/9, 5/9]), np.array([-np.sqrt(3/5), 0, np.sqrt(3/5)])
    else:
        raise ValueError("Número de nodos no soportado")

def cuadratura_gaussiana(f, a, b, n):
    """
    Aproxima la integral definida de la función f en el intervalo [a, b] utilizando el método de cuadratura Gaussiana.

    Parámetros:
        f: función a integrar
        a: límite inferior del intervalo de integración
        b: límite superior del intervalo de integración
        n: número de puntos de Gauss (2 o 3 para este ejemplo)

    Retorna:
        Aproximación de la integral definida de f en [a, b]
    """
    # Paso 1: Calcular los pesos y las abscisas de los puntos de Gauss
    w, x = calcular_pesos_y_abscisas(n)

    # Paso 2: Transformar el intervalo [a, b] al intervalo estándar [-1, 1]
    x_transformed = ((b - a) * x + (a + b)) / 2

    # Paso 3: Calcular la suma ponderada
    suma = 0
    for i in range(n):
        suma += w[i] * f(x_transformed[i])

    # Paso 4: Devolver la aproximación de la integral
    return (b - a) / 2 * suma

# Ejemplo de uso
def funcion_ejemplo(x):
    return np.exp(-x**2)  # Función de ejemplo, en este caso la distribución Gaussiana

a = -1
b = 1
n = 3

resultado = cuadratura_gaussiana(funcion_ejemplo, a, b, n)
print("Aproximación de la integral:", resultado)
```
### Ejecución
[![image.png](https://i.postimg.cc/65fMcNsH/image.png)](https://postimg.cc/1f40R236)

### Ejercicio 5
#### Metodologia en codigo

∫ \int_{0}^{2} x^2 \, dx \]

```python
import numpy as np

def cuadratura_gaussiana(f, a, b, n):
    """
    Aproxima el valor de una integral definida utilizando el método de cuadratura gaussiana.

    Parámetros:
        f (función): La función a integrar.
        a (float): Límite inferior de integración.
        b (float): Límite superior de integración.
        n (int): Número de puntos de Gauss.

    Retorna:
        float: Aproximación de la integral definida de f(x) desde a hasta b.
    """
    # Paso 1: Preparación
    # Calculamos los pesos y las abscisas de los puntos de Gauss
    weights, nodes = np.polynomial.legendre.leggauss(n)

    # Paso 2: Transformar el intervalo [a, b] al intervalo estándar [-1, 1]
    x_transformed = ((b - a) * nodes + (a + b)) / 2

    # Paso 3: Calcular la suma ponderada
    suma = 0
    for i in range(n):
        suma += weights[i] * f(x_transformed[i])

    # Paso 4: Devolver la aproximación de la integral
    return (b - a) / 2 * suma

# Ejemplo de uso
def funcion_ejemplo(x):
    return x**2

a = 0
b = 2
n = 3
resultado = cuadratura_gaussiana(funcion_ejemplo, a, b, n)
print("Aproximación de la integral:", resultado)
```
### Ejecución
[![image.png](https://i.postimg.cc/nhV0wwpn/image.png)](https://postimg.cc/WhKGd8dy)
