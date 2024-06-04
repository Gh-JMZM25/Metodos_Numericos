# Método de cuadratico

## Definición
La interpolación consiste en hallar un dato dentro de un intervalo en el que conocemos los valores en los extremos.
El problema general de la interpolación se nos presenta cuando nos dan una función de la cual solo conocemos una serie de puntos de la misma:
(xo, yo), (x1, y1),........., (xn, yn)
## Algoritmo 
Dados tres puntos (x0, y0), (x1, y1) y (x2, y2)

Paso 1: Calcular los coeficientes de la ecuación cuadrática 
         a = (y2 - y0) / ((x2 - x0) * (x2 - x1))
         b = (y1 - y0) / ((x1 - x0) * (x1 - x2))
         c = y0

Paso 2: El polinomio de interpolación cuadrática es:
         P(x) = a*(x - x0)*(x - x1) + b*(x - x0)*(x - x2) + c

Paso 3: Para interpolar un valor y en un punto x, evaluar:
         y = P(x)

## Implementación de los métodos en python

### Ejercicio 1: realiza una interpolación cuadrática de un conjunto de datos representados por puntos (x, y), donde x es el año y y es la población en millones.
#### Metodología en código

    import numpy as np

    # x= año, y= población en millones
    x_points = np.array([1986, 1994, 2001])
    y_points = np.array([4936, 5660, 6226])

    # Matriz de Vandermonde para la interpolación cuadrática
    A = np.vander(x_points, 3)
    coefficients = np.linalg.solve(A, y_points)

    # Polinomio cuadrático
    def quadratic_polynomial(x, coeffs):
        return coeffs[0]*x**2 + coeffs[1]*x + coeffs[2]

    # Punto a interpolar
    x_to_interpolate = 1997
    y_interpolated = quadratic_polynomial(x_to_interpolate, coefficients)

    print(f"El valor interpolado de y para x = {x_to_interpolate} es     {y_interpolated}")

    # Visualización
    x_range = np.linspace(0, 4, 400)
    y_range = quadratic_polynomial(x_range, coefficients)
#### Comprobación
[![imagen-2024-05-20-192826114.png](https://i.postimg.cc/FFwVVLKY/IMG-20240520-234632.png)


### Ejercicio 2: Programa que calcula el precio del dolar en 2016 tomando en cuenta los años 2008, 2012 y 2020
#### Metodología en código
   
    import numpy as np

    # x= año, y= población en millones
    x_points = np.array([2008, 2012, 2020])
    y_points = np.array([11.13, 12.96, 21.64])

    # Matriz de Vandermonde para la interpolación cuadrática
    A = np.vander(x_points, 3)
    coefficients = np.linalg.solve(A, y_points)

    # Polinomio cuadrático
    def quadratic_polynomial(x, coeffs):
        return coeffs[0]*x**2 + coeffs[1]*x + coeffs[2]

    # Punto a interpolar
    x_to_interpolate = 2016
    y_interpolated = quadratic_polynomial(x_to_interpolate, coefficients)

    print(f"El valor interpolado de y para x = {x_to_interpolate} es {y_interpolated}")

    # Visualización
    x_range = np.linspace(0, 200, 400)
    y_range = quadratic_polynomial(x_range, coefficients)
#### Comprobación
[![imagen-2024-05-20-193210020.png](https://i.postimg.cc/1zRG30vj/IMG-20240520-234653.png)


### Ejercicio 3: Programa que calcula la integral x^3 donde x es 4 y 0
#### Metodología en código


    import numpy as np

    # x= intervalo, y= resultado de la integral
    x_points = np.array([2, 3, 5])
    y_points = np.array([4, 20.25, 156.25])

    # Matriz de Vandermonde para la interpolación cuadrática
    A = np.vander(x_points, 3)
    coefficients = np.linalg.solve(A, y_points)

    # Polinomio cuadrático
    def quadratic_polynomial(x, coeffs):
        return coeffs[0]*x**2 + coeffs[1]*x + coeffs[2]

    # Punto a interpolar
    x_to_interpolate = 4
    y_interpolated = quadratic_polynomial(x_to_interpolate, coefficients)

    print(f"El valor interpolado de y para x = {x_to_interpolate} es {y_interpolated}")

    # Visualización
    x_range = np.linspace(0, 4, 400)
    y_range = quadratic_polynomial(x_range, coefficients)
    
#### Comprobación
[![imagen-2024-05-20-194023521.png](https://i.postimg.cc/0Q8BxJSk/IMG-20240520-235820.png)


### Ejercicio 4: Programa que calcula el promedio de vida en años en México durante 1980
#### Metodología en código
   
    import numpy as np

    # x= año, y= edad promedio
    x_points = np.array([1930, 1970, 2000])
    y_points = np.array([34, 61, 74])

    # Matriz de Vandermonde para la interpolación cuadrática
    A = np.vander(x_points, 3)
    coefficients = np.linalg.solve(A, y_points)

    # Polinomio cuadrático
    def quadratic_polynomial(x, coeffs):
        return coeffs[0]*x**2 + coeffs[1]*x + coeffs[2]

    # Punto a interpolar
    x_to_interpolate = 1980
    y_interpolated = quadratic_polynomial(x_to_interpolate, coefficients)

    print(f"El valor interpolado de y para x = {x_to_interpolate} es {y_interpolated}")

    # Visualización
    x_range = np.linspace(0, 4, 400)
    y_range = quadratic_polynomial(x_range, coefficients)
#### Comprobación
[![imagen-2024-05-20-194230153.png](https://i.postimg.cc/Fz0dZ1PS/IMG-20240520-234709.png)


### Ejercicio 5: Programa que calcula el porcentaje de inflación en México en 2014
#### Metodología en código
   
    import numpy as np

    # x= año, y= población en millones
    x_points = np.array([2005, 2007, 2021])
    y_points = np.array([3.33, 3.6, 4.65])

    # Matriz de Vandermonde para la interpolación cuadrática
    A = np.vander(x_points, 3)
    coefficients = np.linalg.solve(A, y_points)

    # Polinomio cuadrático
    def quadratic_polynomial(x, coeffs):
        return coeffs[0]*x**2 + coeffs[1]*x + coeffs[2]

    # Punto a interpolar
    x_to_interpolate = 2014
    y_interpolated = quadratic_polynomial(x_to_interpolate, coefficients)

    print(f"El valor interpolado de y para x = {x_to_interpolate} es {y_interpolated}")

    # Visualización
    x_range = np.linspace(0, 4, 400)
    y_range = quadratic_polynomial(x_range, coefficients)

#### Comprobación
[![imagen-2024-05-20-194355297.png](https://i.postimg.cc/1RFqPY9z/IMG-20240520-234727.png)
