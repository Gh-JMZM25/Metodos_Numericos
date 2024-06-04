# Metodo de Gauss

## Definición
  El método de Gauss consiste en transformar un sistema de ecuaciones lineales en uno equivalente pero más simple, utilizando 
  operaciones elementales sobre las filas de una matriz aumentada (una matriz que incluye tanto los coeficientes de las variables 
  como los términos constantes de las ecuaciones). Las operaciones elementales sobre las filas incluyen intercambiar filas, 
  multiplicar una fila por una constante distinta de cero y sumar o restar un múltiplo de una fila a otra fila.
  
  El objetivo del método de Gauss es reducir la matriz aumentada a una forma escalonada o escalonada reducida por filas, lo que 
  facilita la resolución del sistema de ecuaciones mediante sustitución hacia atrás.

## Pasos
  ### 1. Formación de la matriz aumentada: 
  - Conviertes este sistema en una matriz. Las columnas representarán los coeficientes de las incógnitas y la última 
    columna los términos constantes. 
  ### 2. Operaciones para obtener la forma escalonada: 
  - Aplicas operaciones simples a las filas para hacer ceros debajo de los elementos principales (el primer número no nulo de 
    cada fila). El objetivo es llevar la matriz a una forma 
    escalonada. Por ejemplo, podrías restar el doble de la primera fila de la segunda fila para hacer cero el primer elemento 
    de la segunda fila. Repites este proceso para cada fila.
  ### 3. Resolución del sistema de ecuaciones: 
  - Una vez que has obtenido la forma escalonada, puedes resolver el sistema de ecuaciones resultante. Empiezas desde la última 
    ecuación y despejas la última incógnita. Luego, sustituyes este valor en la penúltima ecuación y despejas la siguiente incógnita. 
    Repites este proceso hasta haber encontrado todos los valores de las incógnitas.
  ### 4. Comprobación: 
  - Finalmente, sustituyes los valores obtenidos en las ecuaciones originales para asegurarte de que sean soluciones válidas del 
    sistema de ecuaciones.

## Implementación de los metodos en python
### Ejercicio 1
#### Metodologia en codigo
El sistema de ecuaciones que se resuelve es:
- 3x + 2y = 1
- x + 2y = 1

```python
import numpy as np

def gauss_elimination(A, b):
    n = len(b)
    # Matriz aumentada
    Ab = np.hstack([A, b.reshape(-1, 1)])
    
    for i in range(n):
        # Pivoteo parcial
        max_row = np.argmax(np.abs(Ab[i:, i])) + i
        Ab[[i, max_row]] = Ab[[max_row, i]]
        
        # Eliminación hacia adelante
        for j in range(i + 1, n):
            factor = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= factor * Ab[i, i:]
    
    # Sustitución hacia atrás
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:n])) / Ab[i, i]
    
    return x

# Definición del sistema
A = np.array([[3, 2], [1, 2]], dtype=float)
b = np.array([1, 1], dtype=float)

sol = gauss_elimination(A, b)
print('Solución:', sol)

```
Esto significa que:
- x = 0
- y = 0.5

#### Comprobacion
[![imagen-2024-06-02-185807041.png](https://i.postimg.cc/Fsdw0Rv5/imagen-2024-06-02-185807041.png)](https://postimg.cc/6yKHXBTY)

---------

### Ejercicio 2
#### Metodologia en codigo
El sistema de ecuaciones que se resuelve es:
- 2x + y - z = 8
- -3x - y + 2z = -11
- -2x + y + 2z = -3
  
```python
import numpy as np

def gauss_elimination(A, b):
    n = len(b)
    Ab = np.hstack([A, b.reshape(-1, 1)])
    
    for i in range(n):
        max_row = np.argmax(np.abs(Ab[i:, i])) + i
        Ab[[i, max_row]] = Ab[[max_row, i]]
        
        for j in range(i + 1, n):
            factor = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= factor * Ab[i, i:]
    
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:n])) / Ab[i, i]
    
    return x

A = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]], dtype=float)
b = np.array([8, -11, -3], dtype=float)

sol = gauss_elimination(A, b)
print('Solución:', sol)

```

#### Comprobacion
Esto significa que:
- x = 2
- y = 3
- z = -1
  
[![imagen-2024-06-02-175335015.png](https://i.postimg.cc/GpYwFpnS/imagen-2024-06-02-175335015.png)](https://postimg.cc/HJphHdxQ)

---------

### Ejercicio 3
#### Metodologia en codigo
El sistema de ecuaciones que se resuelve es:
- w + 2x + y - z = 5
- 3w + 2x + 4y + 4z = 16
- 4w + 4x  + 3y + 4z = 22
- 2w + y + 5z = 15

```python
import numpy as np

def gauss_elimination(A, b):
    n = len(b)
    Ab = np.hstack([A, b.reshape(-1, 1)])
    
    for i in range(n):
        max_row = np.argmax(np.abs(Ab[i:, i])) + i
        Ab[[i, max_row]] = Ab[[max_row, i]]
        
        for j in range(i + 1, n):
            factor = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= factor * Ab[i, i:]
    
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:n])) / Ab[i, i]
    
    return x

A = np.array([[1, 2, 1, -1], [3, 2, 4, 4], [4, 4, 3, 4], [2, 0, 1, 5]], dtype=float)
b = np.array([5, 16, 22, 15], dtype=float)

sol = gauss_elimination(A, b)
print('Solución:', sol)

```

#### Comprobacion
Esto significa que:
- w = 16
- x = -6
- y = -2
- z = -3
  
[![imagen-2024-06-02-190407221.png](https://i.postimg.cc/fbZF4f9D/imagen-2024-06-02-190407221.png)](https://postimg.cc/0zWZDmnB)

---------

### Ejercicio 4
#### Metodologia en codigo
El sistema de ecuaciones que se resuelve es:
- 2v + w - x + 2y + 3z = 5
- 3v + 2w + 2x + y - z = 12
- v + w + x - y + 2z = 6
- -2v - w + 3x + 2y + z = -5
- v + 2w + x - y - z = 3

  
```python
import numpy as np

def gauss_elimination(A, b):
    n = len(b)
    Ab = np.hstack([A, b.reshape(-1, 1)])
    
    for i in range(n):
        max_row = np.argmax(np.abs(Ab[i:, i])) + i
        Ab[[i, max_row]] = Ab[[max_row, i]]
        
        for j in range(i + 1, n):
            factor = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= factor * Ab[i, i:]
    
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:n])) / Ab[i, i]
    
    return x

A = np.array([[2, 1, -1, 2, 3], [3, 2, 2, 1, -1], [1, 1, 1, -1, 2], [-2, -1, 3, 2, 1], [1, 2, 1, -1, -1]], dtype=float)
b = np.array([5, 12, 6, -5, 3], dtype=float)

sol = gauss_elimination(A, b)
print('Solución:', sol)

```

#### Comprobacion
Esto significa que:
- v = 4.82608696
- w = -2.02173913
- x = 1.47826087
- y = -1.06521739
- z = 0.32608696
  
[![imagen-2024-06-02-192850127.png](https://i.postimg.cc/VLqpKhJD/imagen-2024-06-02-192850127.png)](https://postimg.cc/vcm0B3LV)

---------

### Ejercicio 5
#### Metodologia en codigo
El sistema de ecuaciones que se resuelve es:
- u - v + 2w - x + 3y + z = 4
- 2u + 3v - w + 2x - y + 2z = 1
- 3u + 2v + 3w - 3x + 2y + z = 3
- 4u - 2v + w + x + y - 3z = 6
- u + v + w + x + y + z = 10
- 2u - v + w + 2x - y + 3z = 5
  
```python
import numpy as np

def gauss_elimination(A, b):
    n = len(b)
    Ab = np.hstack([A, b.reshape(-1, 1)])
    
    for i in range(n):
        max_row = np.argmax(np.abs(Ab[i:, i])) + i
        Ab[[i, max_row]] = Ab[[max_row, i]]
        
        for j in range(i + 1, n):
            factor = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= factor * Ab[i, i:]
    
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:n])) / Ab[i, i]
    
    return x

A = np.array([[1, -1, 2, -1, 3, 1], [2, 3, -1, 2, -1, 2], [3, 2, 3, -3, 2, 1], [4, -2, 1, 1, 1, -3], [1, 1, 1, 1, 1, 1], [2, -1, 1, 2, -1, 3]], dtype=float)
b = np.array([4, 1, 3, 6, 10, 5], dtype=float)

sol = gauss_elimination(A, b)
print('Solución:', sol)

```

#### Comprobacion
Esto significa que:
- u = -1.81066176
- v = 1.89522059
- w = 6.68014706
- x = 4.72977941
- y = 0.28492647
- z = -1.77941176
  
[![imagen-2024-06-02-193202499.png](https://i.postimg.cc/R0DD35YV/imagen-2024-06-02-193202499.png)](https://postimg.cc/rd5Jbbcv)

## Implementacion y ejercicios
[Ejercicios del metodo de Gauss](https://docs.google.com/spreadsheets/d/1VNyxf74rtmIrbNZXjKSa90xqo4Xoaky72CX9Hhu8SLU/edit?usp=sharing)
