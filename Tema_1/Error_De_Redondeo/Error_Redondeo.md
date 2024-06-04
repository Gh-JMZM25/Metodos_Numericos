# Error de Redondeo

## Definición
El error de redondeo es la diferencia entre el valor numérico exacto y su aproximación debido a la limitación en la representación de números en sistemas de cómputo. Este tipo de error ocurre cuando se redondean números a un número fijo de dígitos significativos o decimales. Los errores de redondeo pueden acumularse en cálculos repetidos y afectar la precisión de los resultados.

![](https://github.com/Mexta46/Metodos_Numericos_Tema4/blob/main/Imagenes/Imagenes_tema1/error.png)


## Algoritmo
1. Definir la función f(x) cuya evaluación puede introducir errores de redondeo.
2. Especificar el intervalo de evaluación [a, b].
3. Dividir el intervalo [a, b] en n subintervalos de igual tamaño.
4. Calcular el valor exacto de f(x) en puntos específicos del intervalo.
5. Calcular el valor aproximado de f(x) usando una precisión limitada en puntos específicos del intervalo.
6. Comparar los valores exactos y aproximados para determinar el error de redondeo.
7. Analizar cómo varía el error de redondeo a lo largo del intervalo.
8. Devolver los valores calculados como análisis del error de redondeo.

![](https://github.com/Mexta46/Metodos_Numericos_Tema4/blob/main/Imagenes/Imagenes_tema1/errorf.png)

## Metodología

### Ejercicio 1: Evaluar el Error de Redondeo
A continuación, se presenta un ejemplo de código en Python para evaluar el error de redondeo en la función \( f(x) = e^x \) en el intervalo [0, 1].

```python
import numpy as np

def calcular_error_redondeo(f, a, b, n, precision):
    """
    Función para calcular el error de redondeo en la evaluación de una función f(x) en el intervalo [a, b].

    Parámetros:
    f (función): Función a evaluar.
    a (float): Límite inferior del intervalo.
    b (float): Límite superior del intervalo.
    n (int): Número de subintervalos.
    precision (int): Número de decimales para la aproximación.

    Devuelve:
    list: Lista de errores de redondeo en los puntos del intervalo.
    """
    h = (b - a) / n  # tamaño del subintervalo
    valores_exactos = []
    valores_aproximados = []
    errores = []

    for i in range(n + 1):
        x = a + i * h
        valor_exacto = f(x)
        valor_aproximado = round(f(x), precision)  # Redondear a la precisión especificada
        valores_exactos.append(valor_exacto)
        valores_aproximados.append(valor_aproximado)
        error = abs(valor_exacto - valor_aproximado)
        errores.append(error)

    return errores, valores_exactos, valores_aproximados

# Definición de la función a evaluar
def f(x):
    return np.exp(x)

# Parámetros del intervalo y precisión
a = 0
b = 1
n = 10  # número de subintervalos
precision = 5  # número de decimales para la aproximación

# Calcular errores de redondeo
errores, valores_exactos, valores_aproximados = calcular_error_redondeo(f, a, b, n, precision)

# Imprimir resultados
print("x\tValor Exacto\tValor Aproximado\tError de Redondeo")
for i in range(n + 1):
    x = a + i * h
    print(f"{x:.2f}\t{valores_exactos[i]:.5f}\t{valores_aproximados[i]:.5f}\t{errores[i]:.5f}")
```

### Ejercicio 2: Redondeo de números flotantes
Dado un número flotante, redondearlo a diferentes cantidades de cifras decimales.

```python
# Número flotante original
numero = 123.456789

# Redondear a 2 cifras decimales
redondeado_2 = round(numero, 2)

# Redondear a 3 cifras decimales
redondeado_3 = round(numero, 3)

# Redondear a 4 cifras decimales
redondeado_4 = round(numero, 4)

print(f"Número original: {numero}")
print(f"Redondeado a 2 cifras decimales: {redondeado_2}")
print(f"Redondeado a 3 cifras decimales: {redondeado_3}")
print(f"Redondeado a 4 cifras decimales: {redondeado_4}")
```

### Ejercicio 3: Redondeo de elementos en un array
Dado un array de números flotantes, redondear cada elemento a una cantidad específica de cifras decimales.

```python
import numpy as np

# Array de números flotantes
numeros = np.array([1.123456, 2.654321, 3.987654, 4.321098])

# Redondear cada elemento a 3 cifras decimales
redondeados = np.round(numeros, 3)

print("Array original:")
print(numeros)
print("Array redondeado a 3 cifras decimales:")
print(redondeados)
```

### Ejercicio 4: Propagación del error de redondeo en una suma
Analizar la propagación del error de redondeo al sumar una serie de números flotantes.

```python
# Serie de números flotantes
numeros = [0.123456, 0.234567, 0.345678, 0.456789, 0.567890]

# Sumar los números sin redondeo
suma_sin_redondeo = sum(numeros)

# Sumar los números redondeados a 3 cifras decimales
suma_con_redondeo = sum(round(num, 3) for num in numeros)

print(f"Suma sin redondeo: {suma_sin_redondeo}")
print(f"Suma con redondeo a 3 cifras decimales: {suma_con_redondeo}")
```

### Ejercicio 5: Error de redondeo en una multiplicación
Investigar cómo el error de redondeo afecta el resultado de una multiplicación de números flotantes.

```python
# Números flotantes a multiplicar
a = 1.123456
b = 2.345678

# Multiplicación sin redondeo
resultado_sin_redondeo = a * b

# Multiplicación con redondeo a 3 cifras decimales
a_redondeado = round(a, 3)
b_redondeado = round(b, 3)
resultado_con_redondeo = a_redondeado * b_redondeado

print(f"Multiplicación sin redondeo: {resultado_sin_redondeo}")
print(f"Multiplicación con redondeo a 3 cifras decimales: {resultado_con_redondeo}")
```


### Resultados y Análisis
El código anterior genera una tabla que muestra el valor exacto, el valor aproximado (redondeado a 5 decimales) y el error de redondeo en varios puntos del intervalo [0, 1]. Analizando estos resultados, se puede observar cómo el error de redondeo varía a lo largo del intervalo y entender mejor su comportamiento y magnitud.

