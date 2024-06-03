def biseccion(f, a, b, tol, Nmax):
    """
    Función para encontrar una raíz de la ecuación f(x) = 0 utilizando el método de bisección.

    Parámetros:
    f (función): Función a evaluar.
    a (float): Extremo inferior del intervalo.
    b (float): Extremo superior del intervalo.
    tol (float): Tolerancia para la convergencia.
    Nmax (int): Número máximo de iteraciones.

    Devuelve:
    float: Solución aproximada.
    int: Número de iteraciones realizadas.
    bool: Indicador de convergencia.
    """
    if f(a) * f(b) >= 0:
        print("La función debe cambiar de signo en el intervalo [a, b]")
        return None, 0, False

    for n in range(1, Nmax + 1):
        c = (a + b) / 2
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            return c, n, True
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

    return c, Nmax, False

# Definición de la función a evaluar
def f(x):
    return x**3 - x - 2

# Parámetros del método
a = 1  # extremo inferior del intervalo
b = 2  # extremo superior del intervalo
tol = 1e-6  # tolerancia
Nmax = 100  # número máximo de iteraciones

# Aplicar el método de bisección
solucion, iteraciones, convergencia = biseccion(f, a, b, tol, Nmax)

# Imprimir resultados
if convergencia:
    print(f"Solución encontrada: {solucion:.6f} en {iteraciones} iteraciones")
else:
    print(f"No se alcanzó la convergencia en {iteraciones} iteraciones")
