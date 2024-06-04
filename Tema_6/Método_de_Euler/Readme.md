# Metodo de Euler

## ¿Qué es?
El método de Euler es un método numérico simple para aproximar soluciones de ecuaciones diferenciales ordinarias (EDOs) de primer orden. Es uno de los métodos más básicos y fundamentales para resolver EDOs numéricamente.

En esencia, el método de Euler utiliza una aproximación de la derivada utilizando el concepto de la pendiente de la recta tangente a la curva en un punto dado. La idea es avanzar un pequeño paso a lo largo de la recta tangente para obtener una aproximación del siguiente punto en la solución.

## Explicación del pseudocódigo:
1. Se toman como entrada la función f(x, y) que define la ecuación diferencial, los valores iniciales x0 y y0, el valor final xn y el número de subintervalos n.
2. Se calcula el tamaño del paso h dividiendo el intervalo [x0, xn] en n subintervalos iguales.
3. Se inicializan los valores x y y con los valores iniciales x0 y y0, respectivamente.
4. Se realiza un bucle PARA desde i = 0 hasta n-1, donde:
    - Se calcula la pendiente pendiente en el punto actual (x, y) utilizando la función f(x, y).
    - Se actualiza el valor de y sumando h * pendiente al valor anterior de y.
    - Se actualiza el valor de x sumando h al valor anterior de x.
5. Después del bucle, se devuelve el valor final de y, que es la aproximación de la solución en el punto xn.

Este pseudocódigo implementa el método de Euler de forma iterativa. En cada iteración, se calcula la pendiente en el punto actual (x, y) y se utiliza para aproximar el siguiente valor de y utilizando la fórmula y = y + h * pendiente. Luego, se avanza al siguiente punto actualizando x con x = x + h.
Es importante tener en cuenta que este pseudocódigo asume que la ecuación diferencial es de primer orden y que se conocen los valores iniciales x0 y y0. Además, el método de Euler es solo una aproximación numérica, y su precisión dependerá del tamaño del paso h y de la naturaleza de la ecuación diferencial.

### Pseudocodigo
    ENTRADA: f(x, y) (función que define la ecuación diferencial), x0 (valor inicial de x), y0 (valor inicial de y), xn (valor final de x), n (número de subintervalos)
    
    h = (xn - x0) / n (tamaño del paso)
    x = x0
    y = y0
    
    PARA i = 0 HASTA n-1
        pendiente = f(x, y)
        y = y + h * pendiente
        x = x + h
    FIN PARA
    
    SALIDA: y (aproximación de la solución en xn)

## Implementación de los codigos en Python
### Ejercicio 1.py
#### Codigo
En el ejemplo, se resuelve la EDO dy/dt = y con condición inicial y(0) = 1 desde t = 0 hasta t = 2 usando 10 pasos:
    
    def euler(f, y0, t0, t_final, n):
        """
        Resuelve una ecuación diferencial usando el método de Euler.
    
        Argumentos:
        f -- función que define la ecuación diferencial (dy/dt = f(t, y))
        y0 -- condición inicial para y
        t0 -- valor inicial de t
        t_final -- valor final de t
        n -- número de pasos
    
        Retorna:
        t -- lista de valores de t
        y -- lista de valores de y correspondientes a los valores de t
        """
        h = (t_final - t0) / n  # Tamaño del paso
        t = [t0]
        y = [y0]
    
        for i in range(n):
            y_nuevo = y[-1] + h * f(t[-1], y[-1])
            t_nuevo = t[-1] + h
            t.append(t_nuevo)
            y.append(y_nuevo)
    
        return t, y
    
    # Ejemplo de uso
    def ecuacion_diferencial(t, y):
        return y  # dy/dt = y (ecuación diferencial a resolver)
    
    y0 = 1  # Condición inicial
    t0 = 0  # Valor inicial de t
    t_final = 2  # Valor final de t
    n = 10  # Número de pasos
    
    t, y = euler(ecuacion_diferencial, y0, t0, t_final, n)
    
    print("t\ty")
    for t_val, y_val in zip(t, y):
        print(f"{t_val:.2f}\t{y_val:.4f}")

#### Ejecución
El resultado del ejemplo es una tabla de valores de "t" y "y" que representa la solución aproximada de la EDO en el intervalo [0,2] usando el método de Euler con 10 pasos. La salida se vería algo así:
  
[![imagen-2024-05-23-100443131.png](https://i.postimg.cc/bYnjTQCZ/imagen-2024-05-23-100443131.png)](https://postimg.cc/7bqcPTy4)

### Ejercicio 2.py
#### Codigo
En el ejemplo, se resuelve la EDO dy/dt = t * y con condición inicial y(0) = 1 desde t = 0 hasta t = 4 usando 90 pasos:

    import numpy as np
    import matplotlib.pyplot as plt
    
    def euler(f, y0, t0, t_final, n):
        """
        Resuelve una ecuación diferencial usando el método de Euler.
    
        Argumentos:
        f -- función que define la ecuación diferencial (dy/dt = f(t, y))
        y0 -- condición inicial para y
        t0 -- valor inicial de t
        t_final -- valor final de t
        n -- número de pasos
    
        Retorna:
        t -- arreglo de valores de t
        y -- arreglo de valores de y correspondientes a los valores de t
        """
        h = (t_final - t0) / n  # Tamaño del paso
        t = np.linspace(t0, t_final, n + 1)
        y = np.zeros_like(t)
        y[0] = y0
    
        for i in range(n):
            y[i + 1] = y[i] + h * f(t[i], y[i])
    
        return t, y
    
    # Ejemplo de uso
    def ecuacion_diferencial(t, y):
        return t * y  # dy/dt = t * y (ecuación diferencial a resolver)
    
    y0 = 1  # Condición inicial
    t0 = 0  # Valor inicial de t
    t_final = 4  # Valor final de t
    n = 90  # Número de pasos
    
    t, y = euler(ecuacion_diferencial, y0, t0, t_final, n)
    
    # Graficar la solución
    plt.plot(t, y)
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title('Solución de la ecuación diferencial dy/dt = t * y')
    plt.show()
    
#### Ejecución
El resultado es una gráfica que muestra la solución de la ecuación diferencial dy/dt = t * y con la condición inicial y(0) = 1. El método de Euler aproxima esta solución en el intervalo de t = 0 a t = 4 usando 90 pasos. La gráfica ilustra cómo `y` evoluciona con respecto a `t` según la EDO definida.

La ecuación dy/dt = t * y tiene una solución analítica conocida y = e^(t^2/2), que se puede usar para comparar la precisión de la solución numérica obtenida mediante el método de Euler.
      
[![imagen-2024-05-23-100537150.png](https://i.postimg.cc/c4NG5r2X/imagen-2024-05-23-100537150.png)](https://postimg.cc/bdL5ZNzt)

### Ejercicio 3.py
#### Codigo    
En el ejemplo, se resuelve la EDO dy/dt = -2y con condición inicial y(0) = 1 desde t = 0 hasta t = 5 usando 25 pasos:

        def euler(f, y0, t0, t_final, n):
        """
        Resuelve una ecuación diferencial usando el método de Euler.
    
        Argumentos:
        f -- función que define la ecuación diferencial (dy/dt = f(t, y))
        y0 -- condición inicial para y
        t0 -- valor inicial de t
        t_final -- valor final de t
        n -- número de pasos
    
        Retorna:
        t -- lista de valores de t
        y -- lista de valores de y correspondientes a los valores de t
        """
        h = (t_final - t0) / n  # Tamaño del paso
        t = [t0]
        y = [y0]
    
        for i in range(n):
            y_nuevo = y[-1] + h * f(t[-1], y[-1])
            t_nuevo = t[-1] + h
            t.append(t_nuevo)
            y.append(y_nuevo)
    
        return t, y
    
    # Ejemplo de uso
    def ecuacion_diferencial(t, y):
        return -2 * y  # dy/dt = -2y (ecuación diferencial a resolver)
    
    y0 = 1  # Condición inicial
    t0 = 0  # Valor inicial de t
    t_final = 5  # Valor final de t
    n = 25  # Número de pasos
    
    t, y = euler(ecuacion_diferencial, y0, t0, t_final, n)
    
    # Imprimir resultados
    print("t\ty")
    for t_val, y_val in zip(t, y):
        print(f"{t_val:.2f}\t{y_val:.4f}")
        
#### Ejecución
En esta salida, se puede observar cómo el valor de y decrece exponencialmente conforme t aumenta, lo cual es consistente con la solución de la ecuación diferencial dy/dt = -2y. La solución exacta de esta ecuación diferencial con la condición inicial y(0) = 1 es y(t) = e^(-2t), y el método de Euler aproxima esta solución.
      
[![imagen-2024-05-23-100625349.png](https://i.postimg.cc/Ls5cZfg6/imagen-2024-05-23-100625349.png)](https://postimg.cc/R3rskWTj)

### Ejercicio 4.py
#### Codigo
En el ejemplo, se resuelve la EDO dy/dt = y^2 + t^2 con condición inicial y(0) = 1 desde t(0) = 0 hasta t_final = 6 usando 10 pasos:

    def euler(f, y0, t0, t_final, n):
        """
        Resuelve una ecuación diferencial usando el método de Euler.
    
        Argumentos:
        f -- función que define la ecuación diferencial (dy/dt = f(t, y))
        y0 -- condición inicial para y
        t0 -- valor inicial de t
        t_final -- valor final de t
        n -- número de pasos
    
        Retorna:
        t -- lista de valores de t
        y -- lista de valores de y correspondientes a los valores de t
        """
        h = (t_final - t0) / n  # Tamaño del paso
        t = [t0]
        y = [y0]
    
        for i in range(n):
            y_nuevo = y[-1] + h * f(t[-1], y[-1])
            t_nuevo = t[-1] + h
            t.append(t_nuevo)
            y.append(y_nuevo)
    
        return t, y
    
    # Ejemplo de uso
    def ecuacion_diferencial(t, y):
        return y**2 + t**2  # dy/dt = y^2 + t^2 (ecuación diferencial a resolver)
    
    y0 = 1  # Condición inicial
    t0 = 0  # Valor inicial de t
    t_final = 6  # Valor final de t
    n = 10  # Número de pasos
    
    t, y = euler(ecuacion_diferencial, y0, t0, t_final, n)
    
    # Imprimir resultados
    print("t\ty")
    for t_val, y_val in zip(t, y):
        print(f"{t_val:.2f}\t{y_val:.4f}")
        
#### Ejecución
La tabla muestra cómo "y" cambia con respecto a "t" desde t(0) hasta t_final = 6 usando 10 pasos.
Se observa que los valores de y crecen rápidamente, lo que indica que la solución de la ecuación diferencial tiene un comportamiento exponencial o incluso más rápido en este intervalo.
      
[![imagen-2024-05-23-100724206.png](https://i.postimg.cc/brxWj9WL/imagen-2024-05-23-100724206.png)](https://postimg.cc/xNdtvM0b)

### Ejercicio 5.py
#### Codigo
En el ejemplo, se resuelve la EDO dy/dt = 4t^3 - 6y con condición inicial y(0) = 1 desde t(0) = 0 hasta t_final = 3 usando 41 pasos:

    import numpy as np
    
    def euler(f, y0, t0, t_final, n):
        """
        Resuelve una ecuación diferencial usando el método de Euler.
    
        Argumentos:
        f -- función que define la ecuación diferencial (dy/dt = f(t, y))
        y0 -- condición inicial para y
        t0 -- valor inicial de t
        t_final -- valor final de t
        n -- número de pasos
    
        Retorna:
        t -- arreglo de valores de t
        y -- arreglo de valores de y correspondientes a los valores de t
        """
        h = (t_final - t0) / n  # Tamaño del paso
        t = np.linspace(t0, t_final, n + 1)
        y = np.zeros_like(t)
        y[0] = y0
    
        for i in range(n):
            y[i + 1] = y[i] + h * f(t[i], y[i])
    
        return t, y
    
    # Ejemplo de uso
    def ecuacion_diferencial(t, y):
        return 4 * t**3 - 6 * y  # dy/dt = 4t^3 - 6y (ecuación diferencial a resolver)
    
    y0 = 1  # Condición inicial
    t0 = 0  # Valor inicial de t
    t_final = 3  # Valor final de t
    n = 41  # Número de pasos
    
    t, y = euler(ecuacion_diferencial, y0, t0, t_final, n)
    
    # Imprimir resultados
    print("t\ty")
    for t_val, y_val in zip(t, y):
        print(f"{t_val:.2f}\t{y_val:.4f}")
      
#### Ejecución
El código imprimirá los valores de t y los correspondientes valores aproximados de y calculados mediante el método de Euler. El intervalo de t es de 0 a 3, dividido en 41 pasos (por lo tanto, con un tamaño de paso h de 0.07317). Cada fila de la salida contiene un valor de t y el valor aproximado de y en ese punto, formateados con dos decimales para t y cuatro decimales para y.
      
[![imagen-2024-05-23-100811985.png](https://i.postimg.cc/nhc567kY/imagen-2024-05-23-100811985.png)](https://postimg.cc/0bFcSzhb)
