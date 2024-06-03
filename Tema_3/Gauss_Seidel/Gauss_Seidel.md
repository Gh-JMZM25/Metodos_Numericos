# Gauss Seidel

## ¿Que es?
  El método de Gauss-Seidel es un algoritmo utilizado para resolver sistemas de ecuaciones lineales de forma iterativa. 
  Este método es una extensión del método de Jacobi y se utiliza comúnmente en álgebra lineal y en problemas de ingeniería, 
  física y matemáticas aplicadas.
  
  La idea básica detrás del método de Gauss-Seidel es resolver el sistema de ecuaciones lineales de manera iterativa, donde 
  en cada iteración se actualizan las soluciones de las ecuaciones utilizando los valores más recientes calculados en las 
  iteraciones anteriores. A diferencia del método de Jacobi, en el que se utilizan los valores de la iteración anterior para 
  actualizar todos los valores simultáneamente, en Gauss-Seidel, los valores actualizados se utilizan inmediatamente después 
  de ser calculados. Esto puede llevar a una convergencia más rápida en algunos casos.

## Pasos
  ### 1. Inicialización: 
  - Empieza con una suposición inicial de las soluciones para todas las incógnitas del sistema de ecuaciones.
  
  ### 2. Iteración:
  - Para cada ecuación en el sistema, calcula el valor de la incógnita utilizando los valores actuales de las otras incógnitas 
    (puedes empezar con la primera ecuación y luego seguir con las siguientes, o puedes cambiar el orden dependiendo de tu 
    preferencia).
  
  - Utiliza los nuevos valores calculados para actualizar las soluciones de las incógnitas.
  
  - Repite este proceso para cada ecuación en el sistema.
  
  ### 3. Criterio de parada:
  - Define un criterio de parada, como la diferencia entre los valores de las incógnitas en dos iteraciones sucesivas. Si esta
    diferencia es lo suficientemente pequeña (por debajo de un cierto umbral), detén el proceso iterativo. También puedes
    establecer un número máximo de iteraciones como criterio de parada.
  
  ### 4. Convergencia:
  - Comprueba si las soluciones convergen a una solución estable. Si no es así, es posible que necesites ajustar el sistema, cambiar
    la suposición inicial o utilizar otro método de 
    resolución.
    
  ### 5. Resultados:
  - Una vez que el criterio de parada se cumple, los valores de las incógnitas calculados en la última iteración se consideran las 
    soluciones aproximadas del sistema de ecuaciones.
  
  Este algoritmo se repite hasta que se alcanza el criterio de parada, lo que indica que las soluciones convergen a una solución estable 
  o que se ha alcanzado el número máximo de iteraciones permitidas. Es importante tener en cuenta que la convergencia del método de 
  Gauss-Seidel puede depender de varios factores, como la elección de la suposición inicial y las propiedades de la matriz de coeficientes 
  del sistema de ecuaciones lineales.

## Implementación de los metodos en python
### Ejercicio 1
#### Metodologia en codigo

```python
import numpy as np

def gauss_seidel(A, b, x0, tol, maxiter):
    """
    Función para resolver un sistema de ecuaciones lineales Ax = b
    utilizando el método de Gauss-Seidel.

    Argumentos:
    A -- Matriz de coeficientes del sistema
    b -- Vector de términos independientes
    x0 -- Vector inicial de aproximación
    tol -- Tolerancia para detener las iteraciones
    maxiter -- Número máximo de iteraciones

    Retorna:
    x -- Solución aproximada del sistema
    iters -- Número de iteraciones realizadas
    """
    n = len(b)  # Tamaño del sistema
    x = x0.copy()  # Inicializar vector solución

    for iter in range(maxiter):
        x_old = x.copy()  # Guardar valor anterior de x

        for i in range(n):
            sum = b[i]
            for j in range(n):
                if i != j:
                    sum -= A[i, j] * x[j]
            x[i] = sum / A[i, i]

        # Calcular norma del residuo
        residuo = np.linalg.norm(x - x_old)

        # Verificar criterio de convergencia
        if residuo < tol:
            break

    return x, iter + 1

# Ejemplo de uso
A = np.array([[10, -1, 2, 0],
              [-1, 11, -1, 3],
              [2, -1, 10, -1],
              [0, 3, -1, 8]])
b = np.array([6, 25, -11, 15])
x0 = np.array([0, 0, 0, 0])  # Vector inicial
tol = 1e-6  # Tolerancia
maxiter = 100  # Número máximo de iteraciones

x, iters = gauss_seidel(A, b, x0, tol, maxiter)
print(f"Solución aproximada: {x}")
print(f"Número de iteraciones: {iters}")
```

#### Comprobacion
[![IMG-20240602-WA0028.jpg](https://i.postimg.cc/1tpFwvcL/IMG-20240602-WA0028.jpg)

### Ejercicio 2
#### Metodologia en codigo

```python
import numpy as np

def gauss_seidel(A, b, x0, tol=1e-6, max_iter=100):
    """
    Resuelve un sistema de ecuaciones lineales Ax = b utilizando el método de Gauss-Seidel.
    
    Argumentos:
    A -- Matriz de coeficientes del sistema (numpy.ndarray)
    b -- Vector de términos independientes (numpy.ndarray)
    x0 -- Vector inicial de aproximación (numpy.ndarray)
    tol -- Tolerancia para detener las iteraciones (float)
    max_iter -- Número máximo de iteraciones (int)
    
    Retorna:
    x -- Solución aproximada del sistema (numpy.ndarray)
    iters -- Número de iteraciones realizadas (int)
    """
    n = len(b)
    x = x0.copy()
    
    for iters in range(max_iter):
        x_prev = x.copy()
        
        for i in range(n):
            sigma = b[i]
            for j in range(n):
                if i != j:
                    sigma -= A[i, j] * x[j]
            x[i] = (1 / A[i, i]) * sigma
        
        # Calcular norma del residuo
        residuo = np.linalg.norm(x - x_prev, ord=np.inf)
        
        # Verificar criterio de convergencia
        if residuo < tol:
            break
    
    return x, iters+1

# Ejemplo de uso
A = np.array([[4, 1, -1, 1],
              [1, 5, 1, 2],
              [-1, 1, 6, 1],
              [1, 2, 1, 4]])

b = np.array([5, 11, 13, 15])
x0 = np.zeros(4)  # Vector inicial lleno de ceros

x, iters = gauss_seidel(A, b, x0)
print(f"Solución aproximada: {x}")
print(f"Número de iteraciones: {iters}")
```

#### Comprobacion
[![IMG-20240602-WA0029.jpg](https://i.postimg.cc/ZqNvzwgC/IMG-20240602-WA0029.jpg)

### Ejercicio 3
#### Metodologia en codigo

```python
import numpy as np

def gauss_seidel(A, b, x0, tol=1e-6, max_iter=100):
    """
    Resuelve un sistema de ecuaciones lineales Ax = b utilizando el método de Gauss-Seidel.
    
    Argumentos:
    A -- Matriz de coeficientes del sistema (numpy.ndarray)
    b -- Vector de términos independientes (numpy.ndarray)
    x0 -- Vector inicial de aproximación (numpy.ndarray)
    tol -- Tolerancia para detener las iteraciones (float)
    max_iter -- Número máximo de iteraciones (int)
    
    Retorna:
    x -- Solución aproximada del sistema (numpy.ndarray)
    iters -- Número de iteraciones realizadas (int)
    """
    n = len(b)
    x = x0.copy()
    
    for iters in range(max_iter):
        x_prev = x.copy()
        
        for i in range(n):
            x[i] = b[i]
            for j in range(n):
                if i != j:
                    x[i] -= A[i, j] * x_prev[j]
            x[i] /= A[i, i]
        
        # Calcular norma del residuo
        residuo = np.linalg.norm(x - x_prev, ord=np.inf)
        
        # Verificar criterio de convergencia
        if residuo < tol:
            break
    
    return x, iters+1

# Ejemplo de uso
A = np.array([[10, -1, 2, 0],
              [-1, 11, -1, 3],
              [2, -1, 10, -1],
              [0, 3, -1, 8]])

b = np.array([6, 25, -11, 15])
x0 = np.zeros(4)  # Vector inicial lleno de ceros

x, iters = gauss_seidel(A, b, x0)
print(f"Solución aproximada: {x}")
print(f"Número de iteraciones: {iters}")
```

#### Comprobacion
[![IMG-20240602-WA0030.jpg](https://i.postimg.cc/JzLzBRd4/IMG-20240602-WA0030.jpg)

### Ejercicio 4
#### Metodologia en codigo

```python
import numpy as np

def gauss_seidel(A, b, x0, tol=1e-6, max_iter=100):
    """
    Resuelve un sistema de ecuaciones lineales Ax = b utilizando el método de Gauss-Seidel.
    
    Argumentos:
    A -- Matriz de coeficientes del sistema (numpy.ndarray)
    b -- Vector de términos independientes (numpy.ndarray)
    x0 -- Vector inicial de aproximación (numpy.ndarray)
    tol -- Tolerancia para detener las iteraciones (float)
    max_iter -- Número máximo de iteraciones (int)
    
    Retorna:
    x -- Solución aproximada del sistema (numpy.ndarray)
    iters -- Número de iteraciones realizadas (int)
    """
    n = len(b)
    x = x0.copy()
    
    for iters in range(max_iter):
        x_prev = x.copy()
        
        for i in range(n):
            x[i] = b[i]
            for j in range(n):
                if i != j:
                    x[i] -= A[i, j] * x[j]
            x[i] /= A[i, i]
        
        # Calcular norma del residuo
        residuo = np.linalg.norm(x - x_prev, ord=np.inf)
        
        # Verificar criterio de convergencia
        if residuo < tol:
            break
    
    return x, iters+1

# Ejemplo de uso
A = np.array([[4, 1, -1, 1],
              [1, 5, 1, 2],
              [-1, 1, 6, 1],
              [1, 2, 1, 4]])

b = np.array([5, 11, 13, 15])
x0 = np.zeros(4)  # Vector inicial lleno de ceros

x, iters = gauss_seidel(A, b, x0)
print(f"Solución aproximada: {x}")
print(f"Número de iteraciones: {iters}")
```

#### Comprobacion
[![IMG-20240602-WA0031.jpg](https://i.postimg.cc/rwjM0xrQ/IMG-20240602-WA0031.jpg)

### Ejercicio 5
#### Metodologia en codigo

```python
import numpy as np
from typing import Callable, Optional, Tuple

def gauss_seidel(
    A: np.ndarray,
    b: np.ndarray,
    x0: np.ndarray,
    tol: float = 1e-6,
    max_iter: int = 100,
    relax: float = 1.0,
    verbose: bool = False,
    stopping_criteria: Optional[Callable[[np.ndarray, np.ndarray], bool]] = None,
) -> Tuple[np.ndarray, int, list]:
    """
    Resuelve un sistema de ecuaciones lineales Ax = b utilizando el método de Gauss-Seidel.

    Argumentos:
    A -- Matriz de coeficientes del sistema (numpy.ndarray)
    b -- Vector de términos independientes (numpy.ndarray)
    x0 -- Vector inicial de aproximación (numpy.ndarray)
    tol -- Tolerancia para detener las iteraciones (float)
    max_iter -- Número máximo de iteraciones (int)
    relax -- Factor de relajación (float)
    verbose -- Imprime información de cada iteración (bool)
    stopping_criteria -- Función personalizada para detener las iteraciones (Callable[[np.ndarray, np.ndarray], bool])

    Retorna:
    x -- Solución aproximada del sistema (numpy.ndarray)
    iters -- Número de iteraciones realizadas (int)
    residuos -- Lista de residuos en cada iteración (list)
    """
    n = len(b)
    x = x0.copy()
    residuos = []

    for iters in range(max_iter):
        x_prev = x.copy()

        for i in range(n):
            sigma = b[i]
            for j in range(n):
                if i != j:
                    sigma -= A[i, j] * x[j]
            x[i] = (1 - relax) * x_prev[i] + relax * (sigma / A[i, i])

        # Calcular norma del residuo
        residuo = np.linalg.norm(x - x_prev, ord=np.inf)
        residuos.append(residuo)

        # Verificar criterio de convergencia
        if residuo < tol:
            break

        if stopping_criteria is not None and stopping_criteria(x, x_prev):
            break

        if verbose:
            print(f"Iteración {iters+1}: Residuo = {residuo:.6f}")

    if iters == max_iter - 1:
        print("Advertencia: Se alcanzó el número máximo de iteraciones.")

    return x, iters + 1, residuos


# Ejemplo de uso
A = np.array([[4, 1, -1, 1], [1, 5, 1, 2], [-1, 1, 6, 1], [1, 2, 1, 4]])
b = np.array([5, 11, 13, 15])
x0 = np.zeros(4)  # Vector inicial lleno de ceros

# Función de criterio de parada personalizada
def my_stopping_criteria(x: np.ndarray, x_prev: np.ndarray) -> bool:
    diff = np.abs(x - x_prev)
    return np.max(diff) < 1e-4  # Detener si la máxima diferencia es menor que 1e-4

x, iters, residuos = gauss_seidel(
    A,
    b,
    x0,
    tol=1e-8,
    max_iter=200,
    relax=1.2,
    verbose=True,
    stopping_criteria=my_stopping_criteria,
)
print(f"\nSolución aproximada: {x}")
print(f"Número de iteraciones: {iters}")
```

#### Comprobacion
[![IMG-20240602-WA0033.jpg](https://i.postimg.cc/5yBZcW5n/IMG-20240602-WA0033.jpg)

## Implementacion y ejercicios
[Ejercicios del metodo de Gauss - Seidel](https://docs.google.com/spreadsheets/d/126d6fVLOEG1j31MZZNvPLMYPxiLwVk9_Ih7ST6xk3Z8/edit?usp=sharing)
