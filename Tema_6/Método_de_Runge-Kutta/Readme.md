# Metodo de Runge-Kutta

## ¿Qué es?
El método de Runge-Kutta es un método numérico utilizado para resolver ecuaciones diferenciales ordinarias (EDOs) de forma más precisa y eficiente que el método de Euler. Este método fue desarrollado por los matemáticos alemanes C. Runge y M.W. Kutta a principios del siglo XX.

El método de Runge-Kutta se basa en evaluar la pendiente (derivada) en varios puntos dentro de un intervalo small y combinar estas evaluaciones para obtener una mejor aproximación de la solución. Existen varios órdenes del método de Runge-Kutta, siendo el de cuarto orden (RK4) uno de los más utilizados debido a su buen equilibrio entre precisión y eficiencia computacional.

## Pasos para su solución
1. Definir la ecuación diferencial y las condiciones iniciales: Supongamos que tenemos una EDO de primer orden de la forma: dy/dx = f(x, y), con la condición inicial y(x0) = y0.

2. Dividir el intervalo de interés [x0, xn] en n subintervalos iguales de tamaño h = (xn - x0) / n.

3. Inicializar los valores iniciales x0 y y0.

4. Para cada subintervalo i = 0, 1, 2, ..., n-1, realizar los siguientes pasos:
   - Calcular k1 = h * f(xi, yi)
   - Calcular k2 = h * f(xi + h/2, yi + k1/2)
   - Calcular k3 = h * f(xi + h/2, yi + k2/2)
   - Calcular k4 = h * f(xi + h, yi + k3)
   - Actualizar yi+1 = yi + (k1 + 2*k2 + 2*k3 + k4)/6
   - Actualizar xi+1 = xi + h

5. Repetir el paso 4 hasta alcanzar el valor final xn.

## Implementación de los codigos en Python

### Ejercicio 1.py
#### Codigo.
En el ejemplo, se resuelve la EDO dy/dt = x−y  con las condiciones iniciales x(0) = 0, y(0) = 1 hasta x = 2 usando 10 pasos:

      def runge_kutta4(f, x0, y0, xn, n):
          # Inicializar variables
          x = x0
          y = y0
          h = (xn - x0) / n
      
          # Vectores para almacenar las soluciones
          x_sol = [x0]
          y_sol = [y0]
      
          # Iterar para encontrar la siguiente solución
          for i in range(1, n + 1):
              k1 = h * f(x, y)
              k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
              k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
              k4 = h * f(x + h, y + k3)
      
              # Calcular la siguiente solución
              y = y + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
              x = x0 + i * h
      
              # Almacenar las soluciones
              x_sol.append(x)
              y_sol.append(y)
      
          return x_sol, y_sol
      
      # Ejemplo de uso
      def f(x, y):
          # Ecuación diferencial dy/dx = f(x, y)
          return x - y
      
      # Condiciones iniciales
      x0 = 0
      y0 = 1
      xn = 2
      n = 10  # Número de pasos
      
      # Llamar a la función runge_kutta4
      x_sol, y_sol = runge_kutta4(f, x0, y0, xn, n)
      
      # Imprimir las soluciones
      print("Soluciones:")
      for i in range(len(x_sol)):
          print(f"x = {x_sol[i]}, y = {y_sol[i]}")
#### Comprobacion
El resultado consiste en dos listas: "x_sol" y "y_sol", que contienen los valores de x e y en cada paso. Al imprimir estas listas, se obtiene una tabla de valores aproximados de y para los correspondientes valores de x.

[![imagen-2024-05-28-195541032.png](https://i.postimg.cc/PqVkWD3T/imagen-2024-05-28-195541032.png)](https://postimg.cc/Z9NgZWzM)


### Ejercicio 2.py
#### Codigo
El ejemplo de uso de este método se ilustra con una ecuación diferencial específica dy —y + x^2, y se resuelve para x en el intervalo [0, 2] con y(0) = 1 utilizando 20 pasos.

      import numpy as np
      
      def runge_kutta4(f, x0, y0, xn, n):
          # Inicializar variables
          x = x0
          y = y0
          h = (xn - x0) / n
      
          # Vectores para almacenar las soluciones
          x_sol = [x0]
          y_sol = [y0]
      
          # Iterar para encontrar la siguiente solución
          for i in range(1, n + 1):
              k1 = h * f(x, y)
              k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
              k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
              k4 = h * f(x + h, y + k3)
      
              # Calcular la siguiente solución
              y = y + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
              x = x0 + i * h
      
              # Almacenar las soluciones
              x_sol.append(x)
              y_sol.append(y)
      
          return np.array(x_sol), np.array(y_sol)
      
      # Ejemplo de uso
      def f(x, y):
          # Ecuación diferencial dy/dx = f(x, y)
          return -y + x**2
      
      # Condiciones iniciales
      x0 = 0
      y0 = 1
      xn = 2
      n = 20  # Número de pasos
      
      # Llamar a la función runge_kutta4
      x_sol, y_sol = runge_kutta4(f, x0, y0, xn, n)
      
      # Imprimir las soluciones
      print("Soluciones:")
      for i in range(len(x_sol)):
          print(f"x = {x_sol[i]}, y = {y_sol[i]}")
          
#### Comprobacion
El resultado impreso son las soluciones aproximadas para x e y en cada paso de la iteración.

[![imagen-2024-05-28-200545335.png](https://i.postimg.cc/W3V07DhY/imagen-2024-05-28-200545335.png)](https://postimg.cc/2qHqkSdn)

### Ejercicio 3.py
#### Codigo
La función f define la EDO que se va a resolver (dy/dx = f(x, y) en este caso dy/dx = y * sin(x) + x), y las condiciones iniciales son x0 = 0 y y0 = 1. El intervalo de integración va desde x0 hasta xn = 10, dividido en n = 100 pasos.

      import numpy as np
      import matplotlib.pyplot as plt
      
      def runge_kutta4(f, x0, y0, xn, n):
          # Inicializar variables
          x = x0
          y = y0
          h = (xn - x0) / n
      
          # Vectores para almacenar las soluciones
          x_sol = [x0]
          y_sol = [y0]
      
          # Iterar para encontrar la siguiente solución
          for i in range(1, n + 1):
              k1 = h * f(x, y)
              k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
              k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
              k4 = h * f(x + h, y + k3)
      
              # Calcular la siguiente solución
              y = y + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
              x = x0 + i * h
      
              # Almacenar las soluciones
              x_sol.append(x)
              y_sol.append(y)
      
          return np.array(x_sol), np.array(y_sol)
      
      # Ejemplo de uso
      def f(x, y):
          # Ecuación diferencial dy/dx = f(x, y)
          return y * np.cos(x) - 2 * x * y
      
      # Condiciones iniciales
      x0 = 0
      y0 = 1
      xn = 10
      n = 100  # Número de pasos
      
      # Llamar a la función runge_kutta4
      x_sol, y_sol = runge_kutta4(f, x0, y0, xn, n)
      
      # Graficar las soluciones
      plt.plot(x_sol, y_sol)
      plt.xlabel('x')
      plt.ylabel('y')
      plt.title('Solución de la ecuación diferencial por el método de Runge-Kutta')
      plt.grid()
      plt.show()
      
#### Comprobacion
Finalmente, el código grafica las soluciones, mostrando cómo la solución y varía con respecto a x a lo largo del intervalo especificado.

El resultado de la ejecución de este código será una gráfica que muestra la solución de la ecuación diferencial especificada por el método de Runge-Kutta de cuarto orden.

[![imagen-2024-05-28-201429064.png](https://i.postimg.cc/tTVC7DXL/imagen-2024-05-28-201429064.png)](https://postimg.cc/1nsZjGVH)

### Ejercicio 4.py
#### Codigo
En el ejemplo, se resuelve la EDO dy/dt = y * sin(x) + x  con las condiciones iniciales x(0) = 0, y(0) = 1 hasta x = 10 usando 100 pasos:

      import numpy as np
      import matplotlib.pyplot as plt
      
      def runge_kutta4(f, x0, y0, xn, n):
          # Inicializar variables
          x = x0
          y = y0
          h = (xn - x0) / n
      
          # Vectores para almacenar las soluciones
          x_sol = [x0]
          y_sol = [y0]
      
          # Iterar para encontrar la siguiente solución
          for i in range(1, n + 1):
              k1 = h * f(x, y)
              k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
              k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
              k4 = h * f(x + h, y + k3)
      
              # Calcular la siguiente solución
              y = y + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
              x = x0 + i * h
      
              # Almacenar las soluciones
              x_sol.append(x)
              y_sol.append(y)
      
          return np.array(x_sol), np.array(y_sol)
      
      # Ejemplo de uso
      def f(x, y):
          # Ecuación diferencial dy/dx = f(x, y)
          return y * np.sin(x) + x
      
      # Condiciones iniciales
      x0 = 0
      y0 = 1
      xn = 10
      n = 100  # Número de pasos
      
      # Llamar a la función runge_kutta4
      x_sol, y_sol = runge_kutta4(f, x0, y0, xn, n)
      
      # Graficar las soluciones
      plt.figure(figsize=(10, 6))
      plt.plot(x_sol, y_sol, 'r-', label='Solución numérica')
      plt.xlabel('x')
      plt.ylabel('y')
      plt.title('Solución de la ecuación diferencial por el método de Runge-Kutta')
      plt.grid()
      plt.legend()
      plt.show()

#### Comprobacion
El resultado es una gráfica que muestra la solución numérica de la EDO en el intervalo dado de x. La solución se muestra en función de x en el eje horizontal y de y en el eje vertical.

[![imagen-2024-05-28-202722014.png](https://i.postimg.cc/KcNCBBRV/imagen-2024-05-28-202722014.png)](https://postimg.cc/PNC6kLbz)


### Ejercicio 5.py
#### Codigo
En el ejemplo, se resuelve la EDO dy/dt = y * e^-x  con las condiciones iniciales x(0) = 0, y(0) = 1 hasta x = 5 usando 100 pasos:

      import numpy as np
      import matplotlib.pyplot as plt
      
      def runge_kutta4(f, x0, y0, xn, n):
          # Inicializar variables
          x = x0
          y = y0
          h = (xn - x0) / n
      
          # Vectores para almacenar las soluciones
          x_sol = [x0]
          y_sol = [y0]
      
          # Iterar para encontrar la siguiente solución
          for i in range(1, n + 1):
              k1 = h * f(x, y)
              k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
              k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
              k4 = h * f(x + h, y + k3)
      
              # Calcular la siguiente solución
              y = y + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
              x = x0 + i * h
      
              # Almacenar las soluciones
              x_sol.append(x)
              y_sol.append(y)
      
          return np.array(x_sol), np.array(y_sol)
      
      # Ejemplo de uso
      def f(x, y):
          # Ecuación diferencial dy/dx = f(x, y)
          return y * np.exp(-x)
      
      # Condiciones iniciales
      x0 = 0
      y0 = 1
      xn = 5
      n = 100  # Número de pasos
      
      # Llamar a la función runge_kutta4
      x_sol, y_sol = runge_kutta4(f, x0, y0, xn, n)
      
      # Graficar las soluciones
      plt.figure(figsize=(10, 6))
      plt.plot(x_sol, y_sol, 'g--', label='Solución numérica')
      plt.xlabel('x')
      plt.ylabel('y')
      plt.title('Solución de la ecuación diferencial por el método de Runge-Kutta')
      plt.grid()
      plt.legend()
      plt.show()

#### Comprobacion
El resultado que arroja es una gráfica que muestra la solución numérica de la ecuación diferencial 
dx/dy y * e^-x en el intervalo [0, 5], dada la condición inicial y(0) = 1. La solución se calcula utilizando el método de Runge-Kutta de cuarto orden y se muestra en la gráfica como una línea discontinua verde.

[![imagen-2024-05-28-203926909.png](https://i.postimg.cc/HnGtcpMd/imagen-2024-05-28-203926909.png)](https://postimg.cc/N94XZvbz)
