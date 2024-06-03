import numpy as np

def calcular_overflow(f, a, b, n):
    """
    Función para detectar overflow en la evaluación de una función f(x) en el intervalo [a, b].

    Parámetros:
    f (función): Función a evaluar.
    a (float): Límite inferior del intervalo.
    b (float): Límite superior del intervalo.
    n (int): Número de subintervalos.

    Devuelve:
    list: Lista de valores calculados y marcas de overflow en los puntos del intervalo.
    """
    h = (b - a) / n  # tamaño del subintervalo
    valores = []
    overflows = []

    for i in range(n + 1):
        x = a + i * h
        try:
            valor = f(x)
            valores.append(valor)
            overflows.append(False)
        except OverflowError:
            valores.append(float('inf'))  # Usar infinito para marcar overflow
            overflows.append(True)

    return valores, overflows

# Definición de la función a evaluar
def f(x):
    return np.exp(x)

# Parámetros del intervalo
a = 0
b = 50
n = 10  # número de subintervalos

# Calcular valores y detectar overflow
valores, overflows = calcular_overflow(f, a, b, n)

# Imprimir resultados
print("x\tValor\t\tOverflow")
for i in range(n + 1):
    x = a + i * h
    overflow = "Sí" if overflows[i] else "No"
    print(f"{x:.2f}\t{valores[i]:.5e}\t{overflow}")
