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
