# Metodo de Jacob

## Definición
  El método de Jacob (también conocido como el método de iteración de Jacobianos o el método de Jacobi) es 
  un algoritmo utilizado para resolver sistemas de ecuaciones lineales. Es un método iterativo que se utiliza 
  para aproximar la solución de sistemas de ecuaciones lineales, especialmente cuando estos sistemas son grandes 
  y sparse (es decir, tienen muchos ceros).
    
  El método de Jacob se basa en descomponer la matriz del sistema en una suma de una matriz diagonal y el resto 
  de la matriz. Luego, iterativamente, se resuelve un sistema de ecuaciones en el que la matriz del sistema es la 
  matriz diagonal y se actualizan las soluciones en cada iteración.
    
  El proceso se repite hasta que se alcanza una precisión deseada o se cumple algún otro criterio de convergencia. 
  Aunque el método de Jacob puede ser relativamente simple y fácil de implementar, puede converger lentamente para 
  ciertos tipos de sistemas de ecuaciones. Sin embargo, es útil como paso en métodos más avanzados como el método de 
  Gauss-Seidel o el método de relajación.
  
  El objetivo del método de Gauss es reducir la matriz aumentada a una forma escalonada o escalonada reducida por 
  filas, lo que facilita la resolución del sistema de ecuaciones mediante sustitución hacia atrás.
  
## Pasos
  ### 1. Preparación inicial: 
  - Antes de comenzar, necesitas tener tu sistema de ecuaciones lineales en forma matricial. Es decir, necesitas tener 
    todas las variables y constantes organizadas en una matriz.

  ### 2. Descomposición de la matriz: 
  - Divide la matriz de coeficientes en dos partes: una matriz diagonal y el resto de la matriz. La matriz diagonal son 
    los elementos de la diagonal principal de la matriz original, y el resto son los elementos que no están en la diagonal 
    principal.

  ### 3. Iniciar con una suposición inicial: 
  - Comienza con una suposición inicial para las soluciones de tus variables. Esto podría ser cualquier valor, pero es 
    común empezar con todos los valores en cero.

  ### 4. Iteración: 
  - Ahora, para cada variable en tu sistema, usa la fila correspondiente en la matriz de coeficientes y las soluciones 
    actuales de las otras variables (usando la suposición inicial para la primera iteración) para calcular una nueva 
    estimación para esa variable. Repite este proceso para cada variable.

  ### 5. Actualización de las soluciones: 
  - Después de calcular una nueva estimación para cada variable, actualiza tus soluciones actuales con estas nuevas estimaciones.

  ### 6. Comprobación de convergencia: 
  - Repite los pasos 4 y 5 hasta que tus soluciones converjan a una precisión aceptable. Esto significa que las soluciones no 
    cambian mucho entre iteraciones.

  ### 7. Verificación de la solución: 
  - Una vez que has alcanzado la convergencia, verifica tus soluciones sustituyéndolas en las ecuaciones originales para asegurarte 
  de que satisfacen todas las ecuaciones.

  ### 8. Finalización: 
  - Si tus soluciones son aceptables, entonces has resuelto tu sistema de ecuaciones utilizando el método de Jacob.

Recuerda que la velocidad de convergencia puede variar dependiendo de la naturaleza del sistema de ecuaciones, y puede que necesites ajustar la precisión o la suposición inicial para obtener resultados satisfactorios.

## Implementación de los metodos en python

### Ejercicio 1
#### Metodología en código
  Sistema de ecuaciones lineales 4x4:
  
  4x_1 + x_2 - x_3 + x_4 = 5
  
  x_1 + 5x_2 + x_3 - x_4 = 7
  
  -x_1 + x_2 + 6x_3 + x_4 = 9
  
  x_1 - x_2 + x_3 + 7x_4 = 11

```python
import numpy as np


def jacobi(A, b, x0, tol, N):
    """
    Método de Jacobi para resolver sistemas de ecuaciones lineales.
    
    Argumentos:
    A -- matriz de coeficientes
    b -- vector de términos independientes
    x0 -- vector inicial de aproximación
    tol -- tolerancia
    N -- número máximo de iteraciones
    """
    x = x0.copy()
    n = len(b)
    
    for i in range(N):
        x_prev = x.copy()
        for j in range(n):
            sum = b[j]
            for k in range(n):
                if k != j:
                    sum -= A[j, k] * x_prev[k]
            x[j] = sum / A[j, j]
        
        if np.linalg.norm(x - x_prev, np.inf) < tol:
            break
    
    return x


# Ejemplo de uso
A = np.array([[4, 1, -1, 1], [1, 5, 1, -1], [-1, 1, 6, 1], [1, -1, 1, 7]])
b = np.array([5, 7, 9, 11])
x0 = np.array([0, 0, 0, 0])
tol = 1e-6
N = 100


x = jacobi(A, b, x0, tol, N)
print("Solución aproximada:", x)
```

#### Comprobación
[![image.png](https://i.postimg.cc/HLhfwCWY/image.png)](https://postimg.cc/4KpLGqhq)

### Ejercicio 2
#### Metodología en código
  Implementa un análisis de sensibilidad para observar cómo la solución cambia con variaciones en la matriz A y el vector B:

  4x_1 - x_2 = 15
  
  -x_1 + 4x_2 - x_3 = 10
  
  -x_2 + 4x_3 - x_4 = 10
  
  -x_3 + 3x_4 = 10

```python
import numpy as np

def jacobi(A, b, x0, tol=1e-10, max_iter=1000):
    """
    Método de Jacobi para resolver el sistema de ecuaciones lineales Ax = b.
    
    Parámetros:
    A -- matriz de coeficientes (numpy array de dimensiones n x n)
    b -- vector de términos independientes (numpy array de dimensiones n)
    x0 -- vector inicial (numpy array de dimensiones n)
    tol -- tolerancia para el criterio de convergencia
    max_iter -- número máximo de iteraciones
    
    Devuelve:
    x -- vector solución (numpy array de dimensiones n)
    """
    n = len(b)
    x = x0.copy()
    x_new = np.zeros_like(x)

    for iteration in range(max_iter):
        for i in range(n):
            sum_ = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_) / A[i][i]

        # Verificar la convergencia
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            print(f'Convergencia alcanzada en {iteration + 1} iteraciones.')
            return x_new

        x = x_new.copy()

    print('Número máximo de iteraciones alcanzado.')
    return x

# Ejemplo de uso
A = np.array([[4, -1, 0, 0], 
              [-1, 4, -1, 0], 
              [0, -1, 4, -1], 
              [0, 0, -1, 3]], dtype=float)
b = np.array([15, 10, 10, 10], dtype=float)
x0 = np.zeros(len(b))

solucion = jacobi(A, b, x0)
print('Solución:', solucion)
```

#### Comprobación
[![image.png](https://i.postimg.cc/7PcpG4sm/image.png)](https://postimg.cc/grVMQCPZ)

### Ejercicio 3
#### Metodología en código
  Implementa una versión básica del método de Jacobi para resolver un sistema de ecuaciones lineales Ax=bAx = bAx=b:

   4x₁ - x₂ = 15
   
  -x₁ + 4x₂ - x₃ = 10
  
  -x₂ + 4x₃ - x₄ = 10
  
  -x₃ + 3x₄ = 10

```python
import numpy as np


def jacobi(A, b, x0, tol, max_iterations):
    n = len(b)
    x = x0.copy()
    for k in range(max_iterations):
        x_new = np.zeros_like(x)
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, k + 1
        x = x_new
    return x, max_iterations


# Ejemplo
A = np.array([[4, -1, 0, 0], [-1, 4, -1, 0], [0, -1, 4, -1], [0, 0, -1, 3]])
b = np.array([15, 10, 10, 10])
x0 = np.zeros_like(b)
tol = 1e-10
max_iterations = 100


sol, iterations = jacobi(A, b, x0, tol, max_iterations)
print(f"Solución: {sol}")
print(f"Iteraciones: {iterations}")

```

#### Comprobación
[![image.png](https://i.postimg.cc/v8WNBnnH/image.png)](https://postimg.cc/s1gcHvKt)

### Ejercicio 4
#### Metodología en código
  Sistema de ecuaciones lineales 3x3:

  4x₁ + x₂ + x₃ = 6
  
  x₁ + 3x₂ + x₃ = 4
  
  x₁ + x₂ + 3x₃ = 6

```python
import numpy as np

def jacobi_method(A, b, tol=1e-6, max_iter=1000):
    """
    Resuelve un sistema de ecuaciones lineales Ax = b utilizando el método de Jacobi.
    
    Parámetros:
    A (numpy.ndarray): La matriz de coeficientes del sistema de ecuaciones.
    b (numpy.ndarray): El vector de términos independientes.
    tol (float, opcional): La tolerancia para el criterio de convergencia. Por defecto es 1e-6.
    max_iter (int, opcional): El número máximo de iteraciones. Por defecto es 1000.
    
    Devuelve:
    numpy.ndarray: La solución del sistema de ecuaciones.
    """
    n = len(b)
    x = np.zeros(n)
    
    for iter in range(max_iter):
        x_new = np.copy(x)
        for i in range(n):
            s = b[i]
            for j in range(n):
                if j != i:
                    s -= A[i, j] * x[j]
            x_new[i] = s / A[i, i]
        
        if np.max(np.abs(x_new - x)) < tol:
            return x_new
        
        x = x_new
    
    return x

# Ejemplo de uso
A = np.array([[4, 1, 1], [1, 3, 1], [1, 1, 3]])
b = np.array([6, 4, 6])

x = jacobi_method(A, b)
print("Solución:", x)
```

#### Comprobación
[![image.png](https://i.postimg.cc/rpr9H6CF/image.png)](https://postimg.cc/nsn7sPP6)

### Ejercicio 5
#### Metodología en código
  Sistema de ecuaciones lineales con matriz dispersa:
  
  10x₁ - x₂ + 2x₃ = 6
  
  -x₁ + 11x₂ - x₃ + 3x₄ = 25
  
  2x₁ - x₂ + 10x₃ - x₄ = -11
  
  3x₂ - x₃ + 8x₄ = 15
  
```python
  import numpy as np
  
  def jacobi(A, b, x0, tol, N):
      """
      Método de Jacobi para resolver sistemas de ecuaciones lineales.
      
      Parámetros:
      A (numpy.ndarray): La matriz de coeficientes del sistema.
      b (numpy.ndarray): El vector de términos independientes.
      x0 (numpy.ndarray): Una aproximación inicial de la solución.
      tol (float): La tolerancia para determinar la convergencia.
      N (int): El número máximo de iteraciones.
      
      Devuelve:
      x (numpy.ndarray): La solución aproximada.
      k (int): El número de iteraciones realizadas.
      """
      n = len(b)
      x = x0.copy()
      
      for k in range(N):
          x_new = np.zeros_like(x)
          
          for i in range(n):
              s = b[i]
              for j in range(n):
                  if i != j:
                      s -= A[i, j] * x[j]
              x_new[i] = s / A[i, i]
          
          if np.linalg.norm(x_new - x, np.inf) < tol:
              break
          
          x = x_new
      
      return x, k + 1
  
  # Ejemplo de uso
  A = np.array([[10, -1, 2, 0],
                [-1, 11, -1, 3],
                [2, -1, 10, -1],
                [0, 3, -1, 8]])
  b = np.array([6, 25, -11, 15])
  x0 = np.array([0, 0, 0, 0])  # Aproximación inicial
  tol = 1e-6
  N = 100
  
  x, k = jacobi(A, b, x0, tol, N)
  print(f"Solución aproximada: {x}")
  print(f"Número de iteraciones: {k}")
```


#### Comprobación
[![image.png](https://i.postimg.cc/NjW6mJqh/image.png)](https://postimg.cc/QFJKrqdS)

## Implementacion y ejercicios
[Ejercicios del metodo de Jacob](https://docs.google.com/spreadsheets/d/1pCUyxeDHE9aHkJPAhAWR9iPFlqWY9MG939s1Q2w7AOs/edit?usp=sharing)
