# Metodo de Newton

## Definición

El método de interpolación de Newton es una técnica matemática utilizada para encontrar un polinomio que pase a través de un conjunto dado de puntos de datos. Este polinomio se denomina polinomio interpolador de Newton.
La idea básica del método de Newton es construir un polinomio de grado n-1 (donde n es el número de puntos de datos) que coincida con los valores de la función en esos puntos de datos. El polinomio interpolador de Newton se expresa como una suma de términos, donde cada término contiene un coeficiente y una potencia de (x - x₀), siendo x₀ el primer punto de datos.

    P(x) = a₀ + a₁(x - x₀) + a₂(x - x₀)(x - x₁) + ... + aₙ(x - x₀)(x - x₁)...(x - xₙ₋₁)    
Donde:
    P(x) es el polinomio interpolador de Newton.
    x₀, , , ...,  son los valores de la variable independiente (puntos de datos).x₁x₂xₙ
    a₀, , , ...,  son los coeficientes del polinomio interpolador.a₁a₂aₙ
    n es el número de puntos de datos (grado del polinomio es ).n-1

Los coeficientes , , , ...,  se calculan utilizando las diferencias divididas de Newton de la siguiente manera:a₀a₁a₂aₙ
  a₀ = f(x₀)
a₁ = f[x₀, x₁]
a₂ = f[x₀, x₁, x₂]
...
aₙ = f[x₀, x₁, x₂, ..., xₙ]
Donde  representa la diferencia dividida de orden  de la función  en los puntos , , ..., . Las diferencias divididas se calculan recursivamente mediante la fórmula:f[x₀, x₁, ..., xₖ]kfx₀x₁xₖ
    f[x₀, x₁, ..., xₖ] = (f[x₁, x₂, ..., xₖ] - f[x₀, x₁, ..., xₖ₋₁]) / (xₖ - x₀)4
    
## Pseudocodigo
     función NewtonInterpolation(x, y, x_eval):
        # x e y son los vectores de puntos de datos
        # x_eval es el valor de x en el que se desea evaluar el polinomio interpolador
        n = longitud de x
        coeff = vector de longitud n  # Coeficientes del polinomio interpolador

    # Calcular los coeficientes
    para i desde 0 hasta n-1:
        coeff[i] = y[i]  # Inicializar con los valores de y
        para j desde 0 hasta i-1:
            numer = coeff[i] - coeff[j]
            denom = x[i] - x[j]
            if denom != 0:
                temp_denom = denom
                para k desde 0 hasta j-1:
                    temp_denom -= (x[i] - x[k])
                if temp_denom != 0:
                    coeff[i] = numer / temp_denom

    # Evaluar el polinomio en el punto x_eval
    p_val = coeff[n-1]
    para i desde n-2 hasta 0 con paso -1:
        p_val = coeff[i] + (x_eval - x[i]) * p_val

    devolver p_val

## Implementación de los codigos en Python
### Ejercicio1.py
#### Codigo
Este código implementa la interpolación de Newton para aproximar el valor de una función en un punto específico x_val, dado un conjunto de datos de puntos conocidos (x, y).
Usando los siguientes valores:
    x = [20, 10, 30, 45,62]  # Ejemplo con valores repetidos en x
    y = [22,33,14,54,23]
    x_val = 41
    
       from math import factorial
    
    def newton_interpolation(x, y, x_val):
        n = len(x)
        coeff = [0] * n
    
    # Cálculo de los coeficientes
    for i in range(n):
        coeff[i] = y[i]
        for j in range(i):
            numer = coeff[i] - coeff[j]
            denom = x[i] - x[j]
            if denom != 0:  # Verificar si el denominador es distinto de cero
                temp_denom = denom
                for k in range(j):
                    temp_denom -= (x[i] - x[k])
                if temp_denom != 0:  # Verificar si temp_denom no es cero
                    coeff[i] = numer / temp_denom
                else:
                    coeff[i] = 0  # Asignar un valor predeterminado en caso de división por cero
    
    # Evaluación del polinomio en el punto x_val
    p_val = coeff[n-1]
    for i in range(n-2, -1, -1):
        p_val = coeff[i] + (x_val - x[i]) * p_val
    
    # Cálculo de la cota de error
    error_bound = 0
    for i in range(n):
        term = abs(coeff[i])
        for j in range(i):
            term *= abs(x_val - x[j])
        error_bound += term
    
    return p_val, error_bound

    # Ejemplo de uso
    x = [20, 10, 30, 45,62]  # Ejemplo con valores repetidos en x
    y = [22,33,14,54,23]
    x_val = 41
    
    p_val, error_bound = newton_interpolation(x, y, x_val)
    print(f"Valor interpolado en x={x_val}: {p_val}")
    print(f"Cota de error: {error_bound}")
       

#### Comprobacion
![image](https://github.com/J-2014/Metodo-Numericos/assets/164060185/24706c86-af2c-4768-a363-f95bb1b023fd)
### Ejercicio 2.py
#### Codigo
Este código implementa la interpolación de Newton para aproximar el valor de una función en un punto específico x_val, dado un conjunto de datos de puntos conocidos (x, y).
Usando los siguientes valores:

    from math import factorial
    
    def newton_interpolation(x, y, x_val):
        n = len(x)
        coeff = [0] * n
    
    # Cálculo de los coeficientes
    for i in range(n):
        coeff[i] = y[i]
        for j in range(i):
            numer = coeff[i] - coeff[j]
            denom = x[i] - x[j]
            if denom != 0:  # Verificar si el denominador es distinto de cero
                temp_denom = denom
                for k in range(j):
                    temp_denom -= (x[i] - x[k])
                if temp_denom != 0:  # Verificar si temp_denom no es cero
                    coeff[i] = numer / temp_denom
                else:
                    coeff[i] = 0  # Asignar un valor predeterminado en caso de división por cero
    
    # Evaluación del polinomio en el punto x_val
    p_val = coeff[n-1]
    for i in range(n-2, -1, -1):
        p_val = coeff[i] + (x_val - x[i]) * p_val
    
    # Cálculo de la cota de error
    error_bound = 0
    for i in range(n):
        term = abs(coeff[i])
        for j in range(i):
            term *= abs(x_val - x[j])
        error_bound += term
    
    return p_val, error_bound

    # Ejemplo de uso
    x = [0,1,2,3]  # Ejemplo con valores repetidos en x
    y = [1,2,4,8]
    x_val = 1.5
    
    p_val, error_bound = newton_interpolation(x, y, x_val)
    print(f"Valor interpolado en x={x_val}: {p_val}")
    print(f"Cota de error: {error_bound}")
    
#### Comprobacion
![image](https://github.com/J-2014/Metodo-Numericos/assets/164060185/72371790-42c3-4949-95d5-56e4666f28c2)

### Ejercicio 3.py
#### Codigo
Este código implementa la interpolación de Newton para aproximar el valor de una función en un punto específico x_val, dado un conjunto de datos de puntos conocidos (x, y).
Usando los siguientes valores:

    from math import factorial
    
    def newton_interpolation(x, y, x_val):
        n = len(x)
        coeff = [0] * n
    
    # Cálculo de los coeficientes
    for i in range(n):
        coeff[i] = y[i]
        for j in range(i):
            numer = coeff[i] - coeff[j]
            denom = x[i] - x[j]
            if denom != 0:  # Verificar si el denominador es distinto de cero
                temp_denom = denom
                for k in range(j):
                    temp_denom -= (x[i] - x[k])
                if temp_denom != 0:  # Verificar si temp_denom no es cero
                    coeff[i] = numer / temp_denom
                else:
                    coeff[i] = 0  # Asignar un valor predeterminado en caso de división por cero
    
    # Evaluación del polinomio en el punto x_val
    p_val = coeff[n-1]
    for i in range(n-2, -1, -1):
        p_val = coeff[i] + (x_val - x[i]) * p_val
    
    # Cálculo de la cota de error
    error_bound = 0
    for i in range(n):
        term = abs(coeff[i])
        for j in range(i):
            term *= abs(x_val - x[j])
        error_bound += term
    
    return p_val, error_bound

    # Ejemplo de uso
    x = [13,46,79,80]  # Ejemplo con valores repetidos en x
    y = [73,81,42,20]
    x_val = 25
    
    p_val, error_bound = newton_interpolation(x, y, x_val)
    print(f"Valor interpolado en x={x_val}: {p_val}")
    print(f"Cota de error: {error_bound}")
    
#### Comprobacion
![image](https://github.com/J-2014/Metodo-Numericos/assets/164060185/bd2aebd1-5f19-402d-b8eb-a6a2e71e1706)

### Ejercicio 4.py
#### Codigo
Este código implementa la interpolación de Newton para aproximar el valor de una función en un punto específico x_val, dado un conjunto de datos de puntos conocidos (x, y).
Usando los siguientes valores:

    from math import factorial
    
    def newton_interpolation(x, y, x_val):
        n = len(x)
        coeff = [0] * n
    
    # Cálculo de los coeficientes
    for i in range(n):
        coeff[i] = y[i]
        for j in range(i):
            numer = coeff[i] - coeff[j]
            denom = x[i] - x[j]
            if denom != 0:  # Verificar si el denominador es distinto de cero
                temp_denom = denom
                for k in range(j):
                    temp_denom -= (x[i] - x[k])
                if temp_denom != 0:  # Verificar si temp_denom no es cero
                    coeff[i] = numer / temp_denom
                else:
                    coeff[i] = 0  # Asignar un valor predeterminado en caso de división por cero
    
    # Evaluación del polinomio en el punto x_val
    p_val = coeff[n-1]
    for i in range(n-2, -1, -1):
        p_val = coeff[i] + (x_val - x[i]) * p_val
    
    # Cálculo de la cota de error
    error_bound = 0
    for i in range(n):
        term = abs(coeff[i])
        for j in range(i):
            term *= abs(x_val - x[j])
        error_bound += term
    
    return p_val, error_bound

    # Ejemplo de uso
    x = [12,41,23,21,63]  # Ejemplo con valores repetidos en x
    y = [12,23,34,45,56]
    x_val = 49
    
    p_val, error_bound = newton_interpolation(x, y, x_val)
    print(f"Valor interpolado en x={x_val}: {p_val}")
    print(f"Cota de error: {error_bound}")
   
#### Comprobacion
![image](https://github.com/J-2014/Metodo-Numericos/assets/164060185/d7e25481-f890-4c87-b639-e95f1f01e3af)

### Ejercicio 5.py
#### Codigo
Este código implementa la interpolación de Newton para aproximar el valor de una función en un punto específico x_val, dado un conjunto de datos de puntos conocidos (x, y).
Usando los siguientes valores:
    x = [10,98,23,78,54]  # Ejemplo con valores repetidos en x
    y = [14,25,36,20,58]
    x_val = 35

    from math import factorial

    def newton_interpolation(x, y, x_val):
        n = len(x)
        coeff = [0] * n
    
    # Cálculo de los coeficientes
    for i in range(n):
        coeff[i] = y[i]
        for j in range(i):
            numer = coeff[i] - coeff[j]
            denom = x[i] - x[j]
            if denom != 0:  # Verificar si el denominador es distinto de cero
                temp_denom = denom
                for k in range(j):
                    temp_denom -= (x[i] - x[k])
                if temp_denom != 0:  # Verificar si temp_denom no es cero
                    coeff[i] = numer / temp_denom
                else:
                    coeff[i] = 0  # Asignar un valor predeterminado en caso de división por cero
    
    # Evaluación del polinomio en el punto x_val
    p_val = coeff[n-1]
    for i in range(n-2, -1, -1):
        p_val = coeff[i] + (x_val - x[i]) * p_val
    
    # Cálculo de la cota de error
    error_bound = 0
    for i in range(n):
        term = abs(coeff[i])
        for j in range(i):
            term *= abs(x_val - x[j])
        error_bound += term
    
    return p_val, error_bound

    # Ejemplo de uso
    x = [10,98,23,78,54]  # Ejemplo con valores repetidos en x
    y = [14,25,36,20,58]
    x_val = 35
    
    p_val, error_bound = newton_interpolation(x, y, x_val)
    print(f"Valor interpolado en x={x_val}: {p_val}")
    print(f"Cota de error: {error_bound}")
#### Comprobacion
![image](https://github.com/J-2014/Metodo-Numericos/assets/164060185/3d4bdc6f-500d-4c2b-8e31-313eeb36bd4f)
