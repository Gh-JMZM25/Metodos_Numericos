# Regla de Simpson.

## ¿Que es?

La regla de Simpson es un método de integración numérica que se utiliza para la aproximación numérica de integrales definidas1. El intervalo de integración [a, b] se subdivide en n subintervalos con n siendo un entero par. El ancho de cada subdivisión será: h = (b – a)/n2. La regla de Simpson se utiliza para aproximar el valor de una integral definida, y se basa en la idea de aproximar la curva de la función integrando polinomios de segundo grado2.

## Algoritmo.

1.- Dado un intervalo ([a, b]) y una función (f(x)), la regla de 1/3 de Simpson aproxima el área bajo la curva utilizando un polinomio de segundo orden (interpolante cuadrático).

2.- La fórmula es: [ \int_a^b f(x) , dx \approx \frac{h}{3} \left[ f(a) + 4f\left(\frac{a+b}{2}\right) + f(b) \right] ] donde (h = \frac{b-a}{2}).

3.- Si la función es altamente oscilatoria o carece de derivados en ciertos puntos, se puede usar la regla compuesta de Simpson dividiendo el intervalo en subintervalos pequeños y aplicando la regla de Simpson a cada uno.

## Implementación de los metodos en python
### Ejercicio 1
#### Metodologia en codigo

∫(0 a 1) e^(x^2) dx

```python
import numpy as np

# Método regla de Simpson

# La regla de Simpson es una técnica de integración numérica
# que utiliza polinomios de segundo grado (parábolas) 
# para aproximar la curva.
# Divide el intervalo de integración en varios 
# subintervalos y aproxima cada uno de estos subintervalos 
# con una parábola que pasa a través de tres puntos: el punto inicial, 
# el punto medio y el punto final de cada subintervalo.

#Fórmula: 

# ((DeltaX)/3) [f(x0)+ 4 sumatoria de f(x impares)+ 2 sumatoria de f(x pares)]+f(Xn)]

# Significado de la simbología:

#    - f(x0): Funcion evaluada con intervalo a.
#    - f(Xn): Funcion evaluada con intervalo b.
#    - ( DeltaX o h): Funcion evaluada (b-a)/n
#    - ( a ) y ( b ): Extremos del intervalo de integración.
#    - ( n ): Número de subintervalos en los que se divide el intervalo.

String = "f(x) = e^(x^2)"

# Definir integral
def f(x):
    return np.exp(x**2)
    
# Dar intervalos [a,b]
a, b = 0, 1
n = 4

# Aplicacion de la formula
def simpson(a, b, n):

#Si la función es altamente oscilatoria o carece de derivados en ciertos puntos, se puede usar la regla compuesta de Simpson dividiendo el intervalo en subintervalos pequeños y aplicando la regla de Simpson a cada uno. 
    h = (b - a) / n
    suma = f(a) + f(b)
    for i in range(1, n, 2):
        suma += 4 * f(a + i * h)
    for i in range(2, n, 2):
        suma += 2 * f(a + i * h)
    return (h / 3) * suma

resultado_simpson = simpson(a, b, n)

# Resultados

print("")
print("La ecuación ingresada es: ", String)
print("El parámetro a o límite inferior es: ", a)
print("El parámetro b o límite superior es: ", b)
print("El n de interacciones es: ", n)
print("El resultado aplicando el método regla de Simpson:", resultado_simpson)
print("Bibliográfia: https://www.youtube.com/watch?v=ypaNlJTPf9c&list=PLJPaSlai3G9YIgCJq4a3vbK6P3zWNPOWk&index=22&ab_channel=AntonioCedilloHernandez")
print("")
```
### Ejecución:
[![image.png](https://i.postimg.cc/xTnRcFkL/image.png)](https://postimg.cc/MX3RL5mG)

### Ejercicio 2
#### Metodologia en codigo

∫(0 a 5) x^3 dx

```python
# Método regla de Simpson

# La regla de Simpson es una técnica de integración numérica
# que utiliza polinomios de segundo grado (parábolas) 
# para aproximar la curva.
# Divide el intervalo de integración en varios 
# subintervalos y aproxima cada uno de estos subintervalos 
# con una parábola que pasa a través de tres puntos: el punto inicial, 
# el punto medio y el punto final de cada subintervalo.

#Fórmula: 

# ((DeltaX)/3) [f(a)+ 4f(m) +f(b)]

# Significado de la simbología:

#    - f(a): Funcion evaluada con intervalo a.
#    - f(b): Funcion evaluada con intervalo b.
#    - f(m): punto intermedio se calcula con: (a+b)/2.
#    - ( DeltaX o h): Funcion evaluada (b-a)/n

# Define la función que deseas integrar.
String = "f(x) = ∫ x^3 dx  en los puntos a:0   &   b: 5"

def f(x):
    return x**3

# Define los límites del intervalo de integración.
a, b = 0, 5

# Calcula h o deltaX.
def h():
    return ((b - a) / 2) / 3

# Calcula el punto medio del intervalo f(m)
def m():
    return (b + a) / 2

# Calcula los valores de la función en los extremos y en el punto medio.
def sumaFunciones():
    return f(a) + f(m()) + f(b)

# Aplica la fórmula de Simpson.
def simpson():
    return h() * sumaFunciones()

##Margen de error

def margenError():
    error = 625/25
    return abs((error - simpson()) / error) * 100

# Calcular margen de error
mE = margenError()

# Resultados
print("")
print("La ecuación ingresada es: ", String)
print("El parámetro a o límite inferior es: ", a)
print("El parámetro b o límite superior es: ", b)
print("El resultado aplicando el método del trapecio es:", simpson())
print("Bibliografía:https://es.symbolab.com/solver/step-by-step/%5Cint_%7B0%7D%5E%7B5%7D%20x%5E%7B3%7Ddx?or=input")
print("El link anterior demuestra el resultado en Symbolab para confirmar la validez del resultado")
print("El margen de error es: ", mE)
print("")
```
### Ejecución:
[![image.png](https://i.postimg.cc/Z5DFsbwL/image.png)](https://postimg.cc/DSLX8TkW)

### Ejercicio 3
#### Metodologia en codigo

∫(a hasta b) f(x) dx ≈ (h/3) * [f(a) + 4f(a+h) + 2f(a+2h) + 4f(a+3h) + ... + 2f(b-h) + f(b)]

```python
from math import *

def evaluacion(x):
   """
   Evalúa la función ingresada por el usuario, reemplazando las ocurrencias de 'x' por el valor numérico dado.
   
   Argumentos:
   x -- El valor numérico a sustituir en la función.
   
   Retorna:
   El resultado de evaluar la función con el valor de x dado.
   """
   copia = funcion.copy()  # Crea una copia de la lista de la función
   for j in range(len(copia)):
       if copia[j] == "x":
           copia[j] = str(x)  # Reemplaza 'x' por el valor numérico
   return eval("".join(copia))  # Evalúa la función como una expresión

# Obtener la función y los intervalos de integración del usuario
funcion = list(input("Dame la integral/función: "))
b = float(input("Dame el intervalo superior: "))
a = float(input("Dame el intervalo inferior: "))
n = int(input("Dame el número n: "))

h = (b - a) / n  # Ancho de los trapecios
total = 0  # Acumulador para la suma de las áreas de los trapecios

# Aplicar la regla del trapecio compuesto
for i in range(1, n):
   x = a + i * h  # Calcular la coordenada x del punto intermedio
   if i % 2 == 0:
       total += 2 * evaluacion(x)  # Coeficiente 2 para trapecios pares
   else:
       total += 4 * evaluacion(x)  # Coeficiente 4 para trapecios impares

total += evaluacion(a) + evaluacion(b)  # Agregar las evaluaciones en los límites
total = total * (h / 3)  # Ajustar el resultado por el ancho de los trapecios

print(f"Resultado = {total}")
```
### Ejecución:
[![image.png](https://i.postimg.cc/6qwd4yQB/image.png)](https://postimg.cc/N9JyWGTn)

### Ejercicio 4
#### Metodologia en codigo

∫(a a b) f(x) dx ≈ (h/3) * [f(a) + 4f(a+h) + 2f(a+2h) + 4f(a+3h) + ... + 2f(b-h) + f(b)]

```python

from math import *

def evaluacion(x):
   """
   Evalúa la función ingresada por el usuario, reemplazando las ocurrencias de 'x' por el valor numérico dado.
   
   Argumentos:
   x -- El valor numérico a sustituir en la función.
   
   Retorna:
   El resultado de evaluar la función con el valor de x dado.
   """
   copia = funcion.copy()  # Crea una copia de la lista de la función
   for j in range(len(copia)):
       if copia[j] == "x":
           copia[j] = str(x)  # Reemplaza 'x' por el valor numérico
   return eval("".join(copia))  # Evalúa la función como una expresión

# Obtener la función y los intervalos de integración del usuario
funcion = list(input("¿Cuál es la integral/función? "))
a = float(input("¿Cuál es el intervalo inferior? "))
b = float(input("¿Cuál es el intervalo superior? "))
n = float(input("¿Cuál es el valor de n? "))

h = (b - a) / n  # Ancho de los subintervalos
total = 0  # Acumulador para la suma de las áreas de los trapecios

# Aplicar la regla de Simpson un tercio
for i in range(1, int(n)):
   x = a + i * h  # Calcular la coordenada x del punto intermedio
   if i % 2 == 0:
       total += 2 * evaluacion(x)  # Coeficiente 2 para subintervalos pares
   else:
       total += 4 * evaluacion(x)  # Coeficiente 4 para subintervalos impares

total += evaluacion(a) + evaluacion(b)  # Agregar las evaluaciones en los límites
total = total * (h / 3)  # Ajustar el resultado por el ancho de los subintervalos

print(f"Resultado de la aproximación = {total}")
```
### Ejecución:
[![image.png](https://i.postimg.cc/0jf7YP6D/image.png)](https://postimg.cc/jnDWKV4S)

### Ejercicio 5
#### Metodologia en codigo

∫ (3 a 5) (-x^2 + 8x - 12) dx

```python
import numpy as np

# Método regla de Simpson

# La regla de Simpson es una técnica de integración numérica
# que utiliza polinomios de segundo grado (parábolas) 
# para aproximar la curva.
# Divide el intervalo de integración en varios 
# subintervalos y aproxima cada uno de estos subintervalos 
# con una parábola que pasa a través de tres puntos: el punto inicial, 
# el punto medio y el punto final de cada subintervalo.

#Fórmula: 

# ((DeltaX)/3) [f(x0)+ 4 sumatoria de f(x impares)+ 2 sumatoria de f(x pares)]+f(Xn)]

# Significado de la simbología:

#    - f(x0): Funcion evaluada con intervalo a.
#    - f(Xn): Funcion evaluada con intervalo b.
#    - ( DeltaX o h): Funcion evaluada (b-a)/n
#    - ( a ) y ( b ): Extremos del intervalo de integración.
#    - ( n ): Número de subintervalos en los que se divide el intervalo.


String = "(-x^2 + 8x - 12)"

# Paso 2: Definir la función
def f(x):
    return -x**2+8*x-12

#Dar intervalos [a,b] y n.
a, b = 3, 5
n = 2

#Aplicacion de la formula
def simpson(a, b, n):

#Si la función es altamente oscilatoria o carece de derivados en ciertos puntos, se puede usar la regla compuesta de Simpson dividiendo el intervalo en subintervalos pequeños y aplicando la regla de Simpson a cada uno.
    h = (b - a) / n
    suma = f(a) + f(b)
    for i in range(1, n, 2):
        suma += 4 * f(a + i * h)
    for i in range(2, n, 2):
        suma += 2 * f(a + i * h)
    return (h / 3) * suma


resultado_simpson = simpson(a, b, n)

# Resultados

print("")
print("La ecuación ingresada es: ", String)
print("El parámetro a o límite inferior es: ", a)
print("El parámetro b o límite superior es: ", b)
print("El n de interacciones es: ", n)
print("El resultado aplicando el método regla de Simpson:", resultado_simpson)
print("Bibliográfia: https://www.youtube.com/watch?v=ypaNlJTPf9c&list=PLJPaSlai3G9YIgCJq4a3vbK6P3zWNPOWk&index=22&ab_channel=AntonioCedilloHernandez")
print("")
```
### Ejecución:
[![image.png](https://i.postimg.cc/Kv0n4chy/image.png)](https://postimg.cc/BX18V0vh)

### Ejercicio 6 (Extra java)
#### Metodologia en codigo

2 * (n^6 + 15 * n^4 + 15 * n^2 + 1)

```python
// Java program to evaluate the given expression
import java.util.*;
 
class gfg
{
// Function to find the sum
public static double calculateSum(double n)
{
    return 2 * (Math.pow(n, 6) + 15 * Math.pow(n, 4) 
            + 15 * Math.pow(n, 2) + 1);
}
 
// Driver Code
public static void main(String[] args)
{
    double n = 1.4142;
    System.out.println((int)Math.ceil(calculateSum(n)));
}
}
//This code is contributed by mits
```

### Ejecución:

[![image.png](https://i.postimg.cc/nzKmxpGg/image.png)](https://postimg.cc/xJC8yr73)






