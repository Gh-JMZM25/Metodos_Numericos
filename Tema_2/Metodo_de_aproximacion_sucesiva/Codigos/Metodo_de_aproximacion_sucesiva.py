import numpy as np

def aproximacion_sucesiva(g, x0, tol, Nmax):
    """
    Función para encontrar una raíz de la ecuación x = g(x) utilizando el método de aproximación sucesiva.

    Parámetros:
    g (función): Función iterativa.
    x0 (float): Valor inicial.
    tol (float): Tolerancia para la convergencia.
    Nmax (int): Número máximo de iteraciones.

    Devuelve:
    float: Solución aproximada.
    int: Número de iteraciones realizadas.
    bool: Indicador de convergencia.
    """
    x_n = x0
    for n in range(1, Nmax + 1):
        x_n1 = g(x_n)
        if abs(x_n1 - x_n) < tol:
            return x_n1, n, True
        x_n = x_n1
    return x_n, Nmax, False

# Definición de la función iterativa
def g(x):
    return np.cos(x)

# Parámetros del método
x0 = 0.5  # valor inicial
tol = 1e-6  # tolerancia
Nmax = 100  # número máximo de iteraciones

# Aplicar el método de aproximación sucesiva
solucion, iteraciones, convergencia = aproximacion_sucesiva(g, x0, tol, Nmax)

# Imprimir resultados
if convergencia:
    print(f"Solución encontrada: {solucion:.6f} en {iteraciones} iteraciones")
else:
    print(f"No se alcanzó la convergencia en {iteraciones} iteraciones")
