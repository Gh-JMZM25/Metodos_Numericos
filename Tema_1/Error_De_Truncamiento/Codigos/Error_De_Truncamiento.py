import numpy as np

def calcular_error_truncamiento(f, g, a, b, n):
    """
    Función para calcular el error de truncamiento en la evaluación de una función f(x) y su aproximación g(x) en el intervalo [a, b].

    Parámetros:
    f (función): Función exacta a evaluar.
    g (función): Función aproximada que introduce el error de truncamiento.
    a (float): Límite inferior del intervalo.
    b (float): Límite superior del intervalo.
    n (int): Número de subintervalos.

    Devuelve:
    list: Lista de errores de truncamiento en los puntos del intervalo.
    """
    h = (b - a) / n  # tamaño del subintervalo
    valores_exactos = []
    valores_aproximados = []
    errores = []

    for i in range(n + 1):
        x = a + i * h
        valor_exacto = f(x)
        valor_aproximado = g(x)
        valores_exactos.append(valor_exacto)
        valores_aproximados.append(valor_aproximado)
        error = abs(valor_exacto - valor_aproximado)
        errores.append(error)

    return errores, valores_exactos, valores_aproximados

# Definición de la función exacta y su aproximación
def f(x):
    return np.exp(x)

def g(x):
    # Aproximación de la serie de Taylor truncada a x^2
    return 1 + x + (x**2) / 2

# Parámetros del intervalo
a = 0
b = 1
n = 10  # número de subintervalos

# Calcular errores de truncamiento
errores, valores_exactos, valores_aproximados = calcular_error_truncamiento(f, g, a, b, n)

# Imprimir resultados
print("x\tValor Exacto\tValor Aproximado\tError de Truncamiento")
for i in range(n + 1):
    x = a + i * h
    print(f"{x:.2f}\t{valores_exactos[i]:.5f}\t{valores_aproximados[i]:.5f}\t{errores[i]:.5f}")
