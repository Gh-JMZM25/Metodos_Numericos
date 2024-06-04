# Método de Taylor

## Definición
El método de Taylor es un método numérico utilizado para resolver ecuaciones diferenciales ordinarias (EDOs) de orden superior. Se basa en la expansión en serie de Taylor de la solución alrededor de un punto conocido.

La precisión del método depende del número de términos m retenidos en la serie de Taylor y del tamaño del paso h. Cuantos más términos se incluyan, mejor será la aproximación, pero también será más costoso computacionalmente.

Una de las principales ventajas del método de Taylor es que proporciona una solución analítica aproximada en lugar de simplemente evaluar la función en puntos discretos. Sin embargo, tiene la desventaja de requerir el cálculo de derivadas sucesivas, lo cual puede ser complicado para EDOs no lineales.

El método de Taylor es adecuado para EDOs de orden superior cuando se conocen las condiciones iniciales de todas las derivadas hasta el orden n-1. Para EDOs de primer orden, otros métodos como Euler o Runge-Kutta suelen ser más eficientes.La precisión del método depende del número de términos m retenidos en la serie de Taylor y del tamaño del paso h. Cuantos más términos se incluyan, mejor será la aproximación, pero también será más costoso computacionalmente.

Una de las principales ventajas del método de Taylor es que proporciona una solución analítica aproximada en lugar de simplemente evaluar la función en puntos discretos. Sin embargo, tiene la desventaja de requerir el cálculo de derivadas sucesivas, lo cual puede ser complicado para EDOs no lineales.

El método de Taylor es adecuado para EDOs de orden superior cuando se conocen las condiciones iniciales de todas las derivadas hasta el orden n-1. Para EDOs de primer orden, otros métodos como Euler o Runge-Kutta suelen ser más eficientes.

## Pasos para su solución
El procedimiento para aplicar el método de Taylor es el siguiente:
   1. Definir la ecuación diferencial y las condiciones iniciales:
      Supongamos que tenemos una EDO de primer orden de la forma: dy/dx = f(x, y), con la condición inicial y(x0) = y0.
   
   2. Calcular las derivadas sucesivas de y con respecto a x utilizando la ecuación diferencial dada:
      y' = f(x, y)
      y'' = (∂f/∂x) + (∂f/∂y)y'
      y''' = (∂^2f/∂x^2) + 2(∂^2f/∂x∂y)y' + (∂^2f/∂y^2)y'y''
      y así sucesivamente.
   
   3. Construir la serie de Taylor de y(x) alrededor del punto x0 hasta el orden deseado n:
      y(x) = y(x0) + y'(x0)(x - x0) + (y''(x0)/2!)(x - x0)^2 + ... + (y^(n)(x0)/n!)(x - x0)^n
   
   4. Evaluar las derivadas y'(x0), y''(x0), ..., y^(n)(x0) utilizando las expresiones obtenidas en el paso 2 y los valores iniciales y(x0) = y0.
   
   5. Sustituir los valores de las derivadas evaluadas en el paso 4 en la serie de Taylor del paso 3.
   
   6. Elegir un valor para x = x1 cercano a x0 y evaluar y(x1) utilizando la serie de Taylor obtenida.
   
   7. Repetir los pasos 4, 5 y 6 para obtener aproximaciones de y en puntos sucesivos x2, x3, ..., xn.

## Implementación de los códigos en Python

### Ejercicio 1.py
#### Código
Se define la funcion f(x) = e^x y se solicita al usuario que ingrese el valor de a (el punto en el que se evaluará la aproximación), y el número de términos n que se utilizarán en la aproximación.

      import math
      
      print("Funcion es e^x")
      # Definir la función f(x) = e^x
      def f(x):
          return math.exp(x)
      
      # Derivadas de f(x) = e^x son todas e^x
      def f_primera_derivada(x):
          return math.exp(x)
      
      def f_segunda_derivada(x):
          return math.exp(x)
      
      # Podemos generalizar para las derivadas de cualquier orden en este caso
      def f_derivada_orden_n(x, n):
          return math.exp(x)
      
      # Función para calcular el factorial
      def factorial(n):
          return math.factorial(n)
      
      # Serie de Taylor para e^x
      def taylor_series(a, x0, n):
          suma = f(x0)
          for i in range(1, n + 1):
              término = f_derivada_orden_n(x0, i) * ((a - x0) ** i) / factorial(i)
              suma += término
          return suma
      
      # Leer el punto a evaluar (a), el punto de aproximación (x0) y el número de términos (n)
      a = float(input("Ingrese el valor de a: "))
      x0 = 0  # para la serie de Maclaurin
      n = int(input("Ingrese el número de términos (n): "))
      
      # Calcular la aproximación usando la serie de Taylor
      aproximación = taylor_series(a, x0, n)
      
      # Imprimir el resultado
      print(f"La aproximación de e^{a} usando la serie de Taylor con {n} términos es: {aproximación}")
      
#### Comprobación
El resultado impreso es la aproximación de e^x usando la serie de Taylor con el número de términos especificado por el usuario.

Por ejemplo, si ingresamos 
a = 3 y n = 4, la salida podría ser algo así:

[![imagen-2024-05-23-122006934.png](https://i.postimg.cc/KYGjM9mS/imagen-2024-05-23-122006934.png)](https://postimg.cc/FY6htVfD)


### Ejercicio 2.py
#### Código
Se define la funcion f(x) = sen(x) y se solicita al usuario que ingrese el valor de a (el punto en el que se evaluará la aproximación), y el número de términos n que se utilizarán en la aproximación.

      import math
      
      # Definir la función sin(x)
      def f(x):
          return math.sin(x)
      
      # Derivadas de sin(x) en x = 0 alternan entre sin(x), cos(x), -sin(x), -cos(x)
      def f_derivada_orden_n(x, n):
          if n % 4 == 0:
              return math.sin(x)
          elif n % 4 == 1:
              return math.cos(x)
          elif n % 4 == 2:
              return -math.sin(x)
          else:
              return -math.cos(x)
      
      # Función para calcular el factorial
      def factorial(n):
          return math.factorial(n)
      
      # Serie de Taylor para sin(x)
      def taylor_series(a, x0, n):
          suma = 0
          for i in range(n):
              término = ((-1) ** i) * ((a - x0) ** (2 * i + 1)) / factorial(2 * i + 1)
              suma += término
          return suma
      
      # Leer el punto a evaluar (a), el punto de aproximación (x0) y el número de términos (n)
      a = float(input("Ingrese el valor de a: "))
      x0 = 0  # para la serie de Maclaurin
      n = int(input("Ingrese el número de términos (n): "))
      
      # Calcular la aproximación usando la serie de Taylor
      aproximación = taylor_series(a, x0, n)
      
      # Imprimir el resultado
      print(f"La aproximación de sin({a}) usando la serie de Taylor con {n} términos es: {aproximación}")
#### Comprobación
El resultado impreso es la aproximación de sen(x) usando la serie de Taylor con el número de términos especificado por el usuario.

Por ejemplo, si ingresamos 
a = 3 y n = 6, la salida podría ser algo así:

[![imagen-2024-05-23-122224949.png](https://i.postimg.cc/59Tg1rVt/imagen-2024-05-23-122224949.png)](https://postimg.cc/SjLCfDj0)


### Ejercicio 3.py
#### Código    
Se define la funcion f(x) = cos(x) y se solicita al usuario que ingrese el valor de a (el punto en el que se evaluará la aproximación), y el número de términos n que se utilizarán en la aproximación.

      import math
      
      # Definir la función cos(x)
      def f(x):
          return math.cos(x)
      
      # Derivadas de cos(x) en x = 0 alternan entre cos(x), -sin(x), -cos(x), sin(x)
      def f_derivada_orden_n(x, n):
          if n % 4 == 0:
              return math.cos(x)
          elif n % 4 == 1:
              return -math.sin(x)
          elif n % 4 == 2:
              return -math.cos(x)
          else:
              return math.sin(x)
      
      # Función para calcular el factorial
      def factorial(n):
          return math.factorial(n)
      
      # Serie de Taylor para cos(x)
      def taylor_series(a, x0, n):
          suma = 0
          for i in range(n):
              término = ((-1) ** i) * ((a - x0) ** (2 * i)) / factorial(2 * i)
              suma += término
          return suma
      
      # Leer el punto a evaluar (a), el punto de aproximación (x0) y el número de términos (n)
      a = float(input("Ingrese el valor de a: "))
      x0 = 0  # para la serie de Maclaurin
      n = int(input("Ingrese el número de términos (n): "))
      
      # Calcular la aproximación usando la serie de Taylor
      aproximación = taylor_series(a, x0, n)
      
      # Imprimir el resultado
      print(f"La aproximación de cos({a}) usando la serie de Taylor con {n} términos es: {aproximación}")
      
#### Comprobación
El resultado impreso es la aproximación de sen(x) usando la serie de Taylor con el número de términos especificado por el usuario.

Por ejemplo, si ingresamos 
a = 6 y n = 7, la salida podría ser algo así:

[![imagen-2024-05-23-122404912.png](https://i.postimg.cc/FHQxkJ15/imagen-2024-05-23-122404912.png)](https://postimg.cc/1fJFLXpJ)


### Ejercicio 4.py
#### Código
Se define la funcion f(x) = ln(1 + x) y se solicita al usuario que ingrese el valor de a (el punto en el que se evaluará la aproximación), y el número de términos n que se utilizarán en la aproximación.

      import math
      
      # Definir la función ln(1 + x)
      def f(x):
          return math.log(1 + x)
      
      # Derivadas de ln(1 + x) en x = 0 son (-1)^(n+1) * (n-1)! / n! = (-1)^(n+1) / n
      def f_derivada_orden_n(n):
          return (-1) ** (n + 1) / n
      
      # Función para calcular el factorial
      def factorial(n):
          return math.factorial(n)
      
      # Serie de Taylor para ln(1 + x)
      def taylor_series(a, x0, n):
          suma = 0
          for i in range(1, n + 1):
              término = f_derivada_orden_n(i) * ((a - x0) ** i)
              suma += término
          return suma
      
      # Leer el punto a evaluar (a), el punto de aproximación (x0) y el número de términos (n)
      a = float(input("Ingrese el valor de a: "))
      x0 = 0  # para la serie de Maclaurin
      n = int(input("Ingrese el número de términos (n): "))
      
      # Calcular la aproximación usando la serie de Taylor
      aproximación = taylor_series(a, x0, n)
      
      # Imprimir el resultado
      print(f"La aproximación de ln(1 + {a}) usando la serie de Taylor con {n} términos es: {aproximación}")
#### Comprobación
El resultado impreso es la aproximación de ln(1 + a) usando la serie de Taylor con el número de términos especificado por el usuario.

Por ejemplo, si ingresamos 
a = 10 y n = 7, la salida podría ser algo así:

[![imagen-2024-05-23-122451557.png](https://i.postimg.cc/MG6bd2y9/imagen-2024-05-23-122451557.png)](https://postimg.cc/ZWQd5QsN)

### Ejercicio 5.py
#### Código
Se define la funcion f(x) = x^3 + 2x^2 + x + 1 y se solicita al usuario que ingrese el valor de a (el punto en el que se evaluará la aproximación), y el número de términos n que se utilizarán en la aproximación.

      import math
      
      # Definir la función f(x) = x^3 + 2x^2 + x + 1
      def f(x):
          return x**3 + 2*x**2 + x + 1
      
      # Derivadas de f(x) = x^3 + 2x^2 + x + 1
      def f_primera_derivada(x):
          return 3*x**2 + 4*x + 1
      
      def f_segunda_derivada(x):
          return 6*x + 4
      
      def f_tercera_derivada(x):
          return 6
      
      # Función para calcular el factorial
      def factorial(n):
          return math.factorial(n)
      
      # Serie de Taylor para f(x) = x^3 + 2x^2 + x + 1
      def taylor_series(a, x0, n):
          suma = f(x0)
          if n > 0:
              suma += f_primera_derivada(x0) * (a - x0) / factorial(1)
          if n > 1:
              suma += f_segunda_derivada(x0) * (a - x0)**2 / factorial(2)
          if n > 2:
              suma += f_tercera_derivada(x0) * (a - x0)**3 / factorial(3)
          return suma
      
      # Leer el punto a evaluar (a), el punto de aproximación (x0) y el número de términos (n)
      a = float(input("Ingrese el valor de a: "))
      x0 = 0  # para la serie de Maclaurin
      n = int(input("Ingrese el número de términos (n): "))
      
      # Calcular la aproximación usando la serie de Taylor
      aproximación = taylor_series(a, x0, n)
      
      # Imprimir el resultado
      print(f"La aproximación de f({a}) usando la serie de Taylor con {n} términos es: {aproximación}")
#### Comprobación
Solicita al usuario el valor de a, el punto de aproximación x(0) (que en este caso se fija en 0 para la serie de Maclaurin) y el número de términos n para la aproximación.

El resultado arrojado es la aproximación de f(a) utilizando la serie de Taylor con n términos alrededor del punto x(0). Este valor se calcula utilizando los términos de la serie de Taylor hasta el n-ésimo término. Dependiendo del valor de n y de la diferencia entre a y x(0), esta aproximación puede ser más precisa cuanto mayor sea el valor de n.

[![imagen-2024-05-23-122533417.png](https://i.postimg.cc/0jwpb8sy/imagen-2024-05-23-122533417.png)](https://postimg.cc/LgmqWF5c)
