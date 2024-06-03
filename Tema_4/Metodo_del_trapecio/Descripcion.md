# Metodo del trapecio.

## ¿Qué es?
La regla del trapecio es uno de los métodos más utilizados para calcular aproximaciones numéricas de integrales definidas. Es la primera de las fórmulas cerradas de integración de  Newton – Cotes, para el caso cuando el polinomio interpolante es de grado uno.
Para aplicar este método, se debe dividir el intervalo [a, b] en subintervalos de igual medida, aproximar en cada subintervalo la función f(x) por una recta, aproximar el área bajo la curva f en el intervalo [a, b] mediante la suma de las áreas de los trapecios, y aplicar la regla del trapecio compuesta2.




## Algoritmo.

1. Definir la función a integrar.
2. Establecer los límites de integración.
3. Determinar el número de subintervalos.
4. Calcular el ancho de cada subintervalo.
5. Aplicar la fórmula del trapecio para cada subintervalo.
6. Sumar todas las áreas de los trapecios para obtener la aproximación final de la integral.

## Implementación de los metodos en python
### Ejercicio 1
#### Metodologia en codigo

    # Definir las funciones que se van a integrar

import math

def f(x):
   """
   Función f(x) = x * cos(x)
   """
   return x * math.cos(x)

def g(x):
   """
   Función g(x) = e^cos(x)
   """
   return math.exp(math.cos(x))

def integral(f, a, b):
   """
   Calcula la integral definida de una función f(x) entre los límites a y b usando la regla del trapecio compuesta con corrección del error.
   
   Argumentos:
   f -- La función a integrar.
   a -- El límite inferior de la integral.
   b -- El límite superior de la integral.
   
   Retorna:
   La aproximación de la integral definida de f(x) entre a y b.
   """
   n = int((b - a) / 0.001 + 1)  # Número de subintervalos
   h = (b - a) / n  # Ancho de los subintervalos
   x = a  # Inicializar x en el límite inferior
   suma = 0  # Acumulador para el área de los trapecios
   
       # Iterar sobre los subintervalos
   for i in range(n):
       suma += trapecio(f, x, x + h)  # Calcular el área del trapecio y acumularla
       x += h  # Avanzar al siguiente subintervalo
   
   return suma * h  # Multiplicar la suma acumulada por el ancho de los subintervalos

def trapecio(f, a, b):
   """
   Calcula el área de un trapecio bajo la curva f(x) entre los puntos a y b, con corrección del error.
   
   Argumentos:
   f -- La función bajo la curva.
   a -- El límite inferior del trapecio.
   b -- El límite superior del trapecio.
   
   Retorna:
   El área del trapecio bajo la curva f(x) entre a y b, con corrección del error.
   """
   h = b - a  # Ancho del trapecio
   x = (a + b) / 2  # Punto medio del trapecio
   return (h / 2) * (f(a) + f(b)) - (h ** 3 / 12) * d2(f, x)  # Fórmula del trapecio con corrección del error

def d2(f, x):
   """
   Aproxima la segunda derivada de la función f(x) en el punto x usando diferencias finitas.
   
   Argumentos:
   f -- La función a derivar.
   x -- El punto en el cual se aproxima la segunda derivada.
   
   Retorna:
   La aproximación de la segunda derivada de f(x) en el punto x.
   """
   h = 0.001  # Paso para las diferencias finitas
   return (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)  # Fórmula de diferencias finitas

    # Obtener los límites de integración del usuario
a = float(input("Dame el límite inferior: "))
b = float(input("Dame el límite superior: "))

    # Calcular e imprimir las integrales
print("La integral de f(x) = ", integral(f, a, b))
print("La integral de g(x) = ", integral(g, a, b))



### Ejecución:

[![image.png](https://i.postimg.cc/rm2yq4hF/image.png)](https://postimg.cc/2qTNw1RP)



### Ejercicio 2
#### Metodologia en codigo

import math
import numpy as np

def f(x):
   """
   Función f(x) = x * cos(x)
   """
   return x * math.cos(x)

def g(x):
   """
   Función g(x) = e^cos(x)
   """
   return math.exp(math.cos(x))

def integral(f, a, b, n):
   """
   Calcula la integral definida de una función f(x) entre los límites a y b usando el método del trapecio múltiple.
   
   Argumentos:
   f -- La función a integrar.
   a -- El límite inferior de la integral.
   b -- El límite superior de la integral.
   n -- El número de trapecios a utilizar en el método.
   
   Retorna:
   La aproximación de la integral definida de f(x) entre a y b.
   """
   h = (b - a) / n  # Ancho de los trapecios
   x = np.linspace(a, b, n + 1)  # Vector de puntos en el intervalo [a, b]
   suma = np.sum(f(x[1:-1]))  # Suma de las evaluaciones de la función en los puntos interiores
   
   return (h / 2) * (f(a) + 2 * suma + f(b))  # Fórmula del trapecio múltiple

    # Obtener los límites de integración y el número de trapecios del usuario
a = float(input("Dame el límite inferior: "))
b = float(input("Dame el límite superior: "))
n = int(input("Dame el número de trapecios: "))

    # Calcular e imprimir las integrales
print("La integral de f(x) = ", integral(f, a, b, n))
print("La integral de g(x) = ", integral(g, a, b, n))


### Ejecución:

[![image.png](https://i.postimg.cc/XvS65b9s/image.png)](https://postimg.cc/5X3rcD7z)

### Ejercicio 3
#### Metodologia en codigo

# Método del trapecio

    # Concepto:
    # Este método se basa en la aproximación del área bajo la curva mediante trapecios. 
    # Divide el área bajo la curva en varios trapecios y luego -
    # calcula la suma de las áreas de estos trapecios para aproximar la integral definida.

#Fórmula: 
    # [(DeltaX]* f(a)+f(b) para solo una interaccion
    # [(DeltaX)* [f(x0)+2f(x1)+2f(x2)+...+ 2f(xn-1)+f(xn)+] para varias interacciones

    # Significado de la simbología:

    #    - f(x0): Funcion evaluada con intervalo a.
    #    - f(x1,x2): Funciom evaludada con n.
    #    - ( DeltaX o h): Funcion evaluada (b-a)/n
    #    - ( a ) y ( b ): Extremos del intervalo de integración.
    #    - ( n ): Número de subintervalos en los que se divide el intervalo.


import numpy as np

String = "(-x^2 + 8x - 12)"

    # Definir la función
def f(x):
    return -x**2+8*x-12
    # Establecer limites de integracion
a, b = 3, 5

    # Determinar numero de intervalos
n = 2

def DeltaX(a, b, n):
    # Calcular ancho de los intervalos
    h = (b - a) / n
    
    # Aplicacion de la formula 
    suma = (f(a) + f(b)) / 2

#suma de todas las areas

    for i in range(1, n):
        suma += f(a + i * h)
    return h * suma

resultado_trapecio = DeltaX(a, b, n)


    # Resultados
print("")
print("La ecuación ingresada es: ", String)
print("El parámetro a o límite inferior es: ", a)
print("El parámetro b o límite superior es: ", b)
print("El n de interacciones es: ", n)
print("El resultado aplicando el método del trapecio es:", resultado_trapecio)
print("Bibliográfia: https://www.youtube.com/watch?v=6A6dtNJbdT0&ab_channel=Matem%C3%A1ticasPi%C3%B1a%2aProfePi%C3%B1a%2a")
print("")


### Ejecución:

[![image.png](https://i.postimg.cc/Zq8tFMc4/image.png)](https://postimg.cc/wtjG9FZG)

### Ejercicio 4
#### Metodologia en codigo

    # Método del trapecio

    # Concepto:
    # Este método se basa en la aproximación del área bajo la curva mediante trapecios. 
    # Divide el área bajo la curva en varios trapecios y luego -
    # calcula la suma de las áreas de estos trapecios para aproximar la integral definida.

#Fórmula: 
    # [(DeltaX]* f(a)+f(b) para solo una interaccion
    # [(DeltaX)* [f(x0)+2f(x1)+2f(x2)+...+ 2f(xn-1)+f(xn)+] para varias interacciones

    # Significado de la simbología:

    #    - f(x0): Funcion evaluada con intervalo a.
    #    - f(x1,x2): Funciom evaludada con n.
    #    - ( DeltaX o h): Funcion evaluada (b-a)/n
    #    - ( a ) y ( b ): Extremos del intervalo de integración.
    #    - ( n ): Número de subintervalos en los que se divide el intervalo.


import numpy as np

String = "f(x) = e^(x^2)"

    # Definir funcion.
def f(x):
    return np.exp(x**2)

    # Establecer limites de integracion
a, b = 0, 1
n = 5

def DeltaX(a, b, n):
    # Calcular ancho de los intervalos
    h = (b - a) / n
    
    # Aplicacion de la formula
    suma = (f(a) + f(b)) / 2
    
    # Suma de todas las areas

    for i in range(1, n):
        suma += f(a + i * h)
    return h * suma

resultado_trapecio = DeltaX(a, b, n)


    # Resultados
print("")
print("La ecuación ingresada es: ", String)
print("El parámetro a o límite inferior es: ", a)
print("El parámetro b o límite superior es: ", b)
print("El n de interacciones es: ", n)
print("El resultado aplicando el método del trapecio es:", resultado_trapecio)
print("Bibliográfia: https://www.youtube.com/watch?v=rREhW5wjkUI&list=PLJPaSlai3G9YIgCJq4a3vbK6P3zWNPOWk&index=21&ab_channel=AntonioCedilloHernandez")
print("")

### Ejecución:

[![image.png](https://i.postimg.cc/0jHLyR8d/image.png)](https://postimg.cc/RJKPgYJN)


### Ejercicio 5
#### Metodologia en codigo

# Método del trapecio

    # Concepto:
    # Este método se basa en la aproximación del área bajo la curva mediante trapecios. 
    # Divide el área bajo la curva en varios trapecios y luego -
    # calcula la suma de las áreas de estos trapecios para aproximar la integral definida.

#Fórmula: 
    # [(DeltaX o H]* [f(a)+f(b)]/2 para solo una interaccion

    # Significado de la simbología:
    
    #    - f(x0): Funcion evaluada con intervalo a.
    #    - f(x1,x2): Funciom evaludada con n.
    #    - ( DeltaX o h): Funcion evaluada (b-a)/n
    #    - ( a ) y ( b ): Extremos del intervalo de integración.

String = "f(x) = ∫x^3+6x^2+11x-6 dx  en los puntos a:1.3   &   b: 1.8"

    # 1) Definir ecuacion
def f(x):
    return x**3 + 6*x**2 + 11*x - 6

    # 2) Definir limites y numero de intervalos n = 1
a , b = 1.3, 1.8

    # 3) Implementacion de la formula

    # 3.1) calculo del ancho
def deltax():
    return b - a
    # Aplicacion de la formula
def Suma():
    return (f(a) + f(b)) / 2

def metodoResultado():
    H = deltax()
    S = Suma()
    return H * S

    # Calcular el resultado
mR = metodoResultado()

#Calcular el margen de error

def margenError():
    error = 14.705395
    return abs ((error - mR)/error)*100

    # Calcular margen de error
mE = margenError()

    # Resultados
print("")
print("La ecuación ingresada es: ", String)
print("El parámetro a o límite inferior es: ", a)
print("El parámetro b o límite superior es: ", b)
print("El resultado aplicando el método del trapecio es:", mR)
print("Bibliografía:https://es.symbolab.com/solver/step-by-step/%5Cint_%7B1.3%7D%5E%7B1.8%7D%20x%5E%7B3%7D%2B6x%5E%7B2%7D%2B11x-6dx?or=input")
print("El link anterior demuestra el resultado en Symbolab para confirmar la validez del resultado")
print("El margen de error es: ",mE)
print("")

### Ejecución:

[![image.png](https://i.postimg.cc/W1ZQTHxg/image.png)](https://postimg.cc/4YJ81Bfx)


