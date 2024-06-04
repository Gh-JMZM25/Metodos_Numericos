# Gauss Jordan

## Definicion
  Es un algoritmo utilizado en álgebra lineal para encontrar las soluciones de un sistema de ecuaciones lineales o para encontrar la inversa de una matriz. 
  El método consiste en aplicar operaciones elementales de fila a una matriz ampliada que contiene tanto la matriz de coeficientes como el vector de términos 
  constantes en un sistema de ecuaciones lineales. Estas operaciones elementales de fila incluyen intercambio de filas, multiplicación de una fila por un escalar 
  no nulo y sumar un múltiplo de una fila a otra fila. El objetivo es llevar la matriz ampliada a una forma escalonada reducida (forma escalonada reducida por 
  filas) o a una forma diagonal si se busca la inversa de la matriz. Una vez que la matriz está en una de estas formas, se pueden identificar las soluciones del 
  sistema de ecuaciones o la inversa de la matriz directamente. El método de Gauss-Jordan es una extensión del método de eliminación de Gauss, y es especialmente 
  útil cuando se busca la inversa de una matriz o cuando se necesita resolver sistemas de ecuaciones lineales con múltiples soluciones.

## Algoritmo
 ### 1. Formar la matriz aumentada: 
 - Toma el sistema de ecuaciones lineales y escribe las coeficientes de las variables en una matriz, junto con 
  los términos constantes. Esta matriz es conocida como la matriz aumentada.

 ### 2. Convertir el primer elemento de la matriz en uno: 
 - Divide toda la primera fila de la matriz aumentada por el valor del primer elemento (el coeficiente de la 
  primera variable en la primera ecuación).

 ### 3. Hacer ceros debajo del primer elemento de la diagonal principal: 3
 - Para cada fila por debajo de la primera fila, resta múltiplos adecuados de la primera fila para hacer cero 
  el elemento que se encuentra directamente debajo 
  del primer elemento de la diagonal principal.

 ### 4. Repetir el proceso para los elementos restantes: 
 - Repite los pasos 2 y 3 para cada elemento de la diagonal principal, convirtiendo cada uno en uno y haciendo 
  ceros debajo de él.

 ### 5. Obtener la forma escalonada reducida: 
 - Continúa los pasos hasta que la matriz se convierta en una forma escalonada reducida, donde todos los elementos 
  por encima y por debajo de la diagonal principal sean cero, y cada elemento de la diagonal principal sea uno.

 ### 6. Interpretar los resultados: 
 - Una vez que tengas la forma escalonada reducida, las soluciones al sistema de ecuaciones están directamente leíbles 
  de la matriz. Si hay filas de ceros en la parte inferior de la matriz, significa que hay infinitas soluciones o que 
  el sistema es inconsistente.

 ### 7. Si es necesario, realiza operaciones adicionales: 
 - Si estás buscando la inversa de una matriz, puedes continuar el algoritmo hasta obtener una matriz identidad en el 
  lado izquierdo de la matriz aumentada.

## Implementación de los metodos en python
### Ejercicio 1
#### Metodologia en codigo
El sistema de ecuaciones que se resuelve es:
- x + y + z = 6
- 2y + 5z = -4
- 2x + 5y - z = 27

```python
import numpy as np

def gauss_jordan(A):
    # Convertir la matriz a tipo float para realizar divisiones
    A = A.astype(float)
    rows, cols = A.shape
    
    # Iterar sobre cada columna
    for i in range(rows):
        # Hacer 1 el pivote dividiendo toda la fila por el elemento A[i, i]
        pivot = A[i, i]
        A[i] = A[i] / pivot
        print(f"Step {i*2+1}: Make pivot A[{i},{i}] = 1")
        print(A)
        
        # Hacer 0 los elementos en la columna i, excepto el pivote
        for j in range(rows):
            if i != j:
                factor = A[j, i]
                A[j] = A[j] - factor * A[i]
        print(f"Step {i*2+2}: Make other elements in column {i} = 0")
        print(A)
    
    return A

# Ejemplo de uso
# Matriz aumentada para el sistema de ecuaciones 3x3:
# x + y + z = 6
# 2y + 5z = -4
# 2x + 5y - z = 27

A = np.array([
    [1, 1, 1, 7],
    [0, 2, 5, -4],
    [2, 5, -1, 27]
])

result = gauss_jordan(A)
print("Final Result:")
print(result)
```

#### Comprobación
![Ejercici1](https://github.com/Gh-JMZM25/Metodos_Numericos/assets/164206749/7741d8b5-b204-4169-9922-8fa10c46e0f3)


### Ejercicio 2
#### Metodologia en codigo
El sistema de ecuaciones que se resuelve es:
- 2x + 3y + 6z = 7
- y + z = 2
- x + 5y + 2 = 4

```python
import numpy as np

def gauss_jordan(A):
    # Convertir la matriz a tipo float para realizar divisiones
    A = A.astype(float)
    rows, cols = A.shape
    
    # Iterar sobre cada columna
    for i in range(rows):
        # Hacer 1 el pivote dividiendo toda la fila por el elemento A[i, i]
        pivot = A[i, i]
        A[i] = A[i] / pivot
        print(f"Step {i*2+1}: Make pivot A[{i},{i}] = 1")
        print(A)
        
        # Hacer 0 los elementos en la columna i, excepto el pivote
        for j in range(rows):
            if i != j:
                factor = A[j, i]
                A[j] = A[j] - factor * A[i]
        print(f"Step {i*2+2}: Make other elements in column {i} = 0")
        print(A)
    
    return A

# Ejemplo de uso
# Matriz aumentada para el sistema de ecuaciones 3x3:
# 2x + 3y + 6z = 7
# y + z = 2
# x + 5y + 2 = 4

A = np.array([
    [2, 3, 6, 7],
    [0, 1, 1, 2],
    [1, 5, 2, 4]
])

result = gauss_jordan(A)
print("Final Result:")
print(result)
```
#### Comprobación
![Ejercici2](https://github.com/Gh-JMZM25/Metodos_Numericos/assets/164206749/f5c39fab-cb1f-42c6-b461-eaed3b25f3fa)


### Ejercicio 3
#### Metodologia en codigo
El sistema de ecuaciones que se resuelve es:
- 3x + 2y = 6
- 2x + 2y = 7

```python
import numpy as np

def gauss_jordan(A):
    # Convertir la matriz a tipo float para realizar divisiones
    A = A.astype(float)
    rows, cols = A.shape
    
    # Iterar sobre cada columna
    for i in range(rows):
        # Hacer 1 el pivote dividiendo toda la fila por el elemento A[i, i]
        pivot = A[i, i]
        A[i] = A[i] / pivot
        print(f"Step {i*2+1}: Make pivot A[{i},{i}] = 1")
        print(A)
        
        # Hacer 0 los elementos en la columna i, excepto el pivote
        for j in range(rows):
            if i != j:
                factor = A[j, i]
                A[j] = A[j] - factor * A[i]
        print(f"Step {i*2+2}: Make other elements in column {i} = 0")
        print(A)
    
    return A

# Ejemplo de uso
# Matriz aumentada para el sistema de ecuaciones 2x2:
# 3x + 2y = 6
# 2x + 2y = 7

A = np.array([
    [3, 2, 6],
    [2, 2, 7],
])

result = gauss_jordan(A)
print("Final Result:")
print(result)
```

#### Comprobación
![Ejercici3](https://github.com/Gh-JMZM25/Metodos_Numericos/assets/164206749/03919ef4-b29a-401c-9766-2b1c303ede97)



### Ejercicio 4
#### Metodologia en codigo
El sistema de ecuaciones que se resuelve es:
- 2x + 5y = 14
- x + 7y = 7

```python
import numpy as np

def gauss_jordan(A):
    # Convertir la matriz a tipo float para realizar divisiones
    A = A.astype(float)
    rows, cols = A.shape
    
    # Iterar sobre cada columna
    for i in range(rows):
        # Hacer 1 el pivote dividiendo toda la fila por el elemento A[i, i]
        pivot = A[i, i]
        A[i] = A[i] / pivot
        print(f"Step {i*2+1}: Make pivot A[{i},{i}] = 1")
        print(A)
        
        # Hacer 0 los elementos en la columna i, excepto el pivote
        for j in range(rows):
            if i != j:
                factor = A[j, i]
                A[j] = A[j] - factor * A[i]
        print(f"Step {i*2+2}: Make other elements in column {i} = 0")
        print(A)
    
    return A

# Ejemplo de uso
# Matriz aumentada para el sistema de ecuaciones 2x2:
# 2x + 5y = 14
# x + 7y = 7

A = np.array([
    [ 2, 5, 14],
    [1, 7, 7]
])

result = gauss_jordan(A)
print("Final Result:")
print(result)
```

#### Comprobación
![Ejercici4](https://github.com/Gh-JMZM25/Metodos_Numericos/assets/164206749/930c1a18-ac41-4dda-b0c9-f1c743e5d41f)



### Ejercicio 5
#### Metodologia en codigo
El sistema de ecuaciones que se resuelve es:
- 2x + 1y + 3z + w = 3
- x + 2y + 5z + w = -2
- 2x + 5y - z + w = 1
- 4x + 3y - 2z + w = 0

```python
import numpy as np

def gauss_jordan(A):
    # Convertir la matriz a tipo float para realizar divisiones
    A = A.astype(float)
    rows, cols = A.shape
    
    # Iterar sobre cada columna
    for i in range(rows):
        # Hacer 1 el pivote dividiendo toda la fila por el elemento A[i, i]
        pivot = A[i, i]
        A[i] = A[i] / pivot
        print(f"Step {i*2+1}: Make pivot A[{i},{i}] = 1")
        print(A)
        
        # Hacer 0 los elementos en la columna i, excepto el pivote
        for j in range(rows):
            if i != j:
                factor = A[j, i]
                A[j] = A[j] - factor * A[i]
        print(f"Step {i*2+2}: Make other elements in column {i} = 0")
        print(A)
    
    return A

# Ejemplo de uso
# Matriz aumentada para el sistema de ecuaciones 4x4:
# 2x + 1y + 3z + w = 3
# x + 2y + 5z + w = -2
# 2x + 5y - z + w = 1
# 4x + 3y - 2z + w = 0

A = np.array([
    [2, 1, 3, 1, -3],
    [1, 2, 5, 1, -2],
    [1, 4, -3, 1, 5],
    [4, 3, -2, 1, 0]
])

result = gauss_jordan(A)
print("Final Result:")
print(result)
```

#### Comprobación
![Ejercici5](https://github.com/Gh-JMZM25/Metodos_Numericos/assets/164206749/c852e9d7-01c9-4898-b55b-81d3e332673f)

## Ejercicios en excel
[Ejercicios del metodo de Gauss Jordan](https://docs.google.com/spreadsheets/d/13LaG-yuZGNyTcdEdCONMtDpY-dnTvp2FBTZWmA-gCLY/edit?usp=sharing)



  
