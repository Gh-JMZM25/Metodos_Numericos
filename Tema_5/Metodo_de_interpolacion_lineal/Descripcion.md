# Metodo de la interpolación lineal

## Definición
La interpolación lineal es un caso en donde se usa un polinomio de primer grado, es decir una función lineal o afín, para adivinar el valor de la función en un punto.

## Pseudocodigo.

    Función InterpolacionLineal(x0, y0, x1, y1, x):
        Entrada: x0, y0: coordenadas del primer punto
            x1, y1: coordenadas del segundo punto
             x: valor de x para el cual se quiere interpolar
        Salida: valor interpolado y en x

        Calcular la pendiente de la recta que pasa por los dos puntos
        pendiente = (y1 - y0) / (x1 - x0)

        Calcular el valor interpolado utilizando la ecuación de la recta
        y = y0 + pendiente * (x - x0)

        Devolver y
    Fin Función

        Programa Principal:
        Leer x0, y0, x1, y1, x

        y = InterpolacionLineal(x0, y0, x1, y1, x)

        Imprimir "El valor interpolado en x =", x, "es:", y
    Fin Programa

## Implementación de los codigos en Python.
### Ejercicio 1.py
#### Codigo.
   
    def lineal_interpolation(x_values, y_values, x):
        for i in range(len(x_values) - 1):
            if x_values[i] <= x <= x_values[i + 1]:
                x0, y0 = x_values[i], y_values[i]
                x1, y1 = x_values[i + 1], y_values[i + 1]
                return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

    #Ejemplo de uso
    x_values = [1, 2, 3, 4, 5]
    y_values = [2, 4, 6, 8, 10]
    x = 3.5

    y = lineal_interpolation(x_values, y_values, x)
    print(f"El valor interpolado en x={x} es: {y}")

#### Comprobacion.
[![Captura-de-pantalla-2024-05-20-224700.png](https://i.postimg.cc/qRBfNB5T/Captura-de-pantalla-2024-05-20-224700.png)](https://postimg.cc/wtr4Pzzf)

### Ejercicio 2.py
#### Codigo.
   
    def lineal_interpolation(x0, y0, x1, y1, x):
        return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

    #Ejemplo de uso
    x0 = 1
    y0 = 2
    x1 = 5
    y1 = 10
    x = 3

    y = lineal_interpolation(x0, y0, x1, y1, x)
    print(f"El valor interpolado en x={x} es: {y}")
    
#### Comprobacion.
[![Captura-de-pantalla-2024-05-20-224745.png](https://i.postimg.cc/yxWwTQKp/Captura-de-pantalla-2024-05-20-224745.png)](https://postimg.cc/K3SqG5Rt)

### Ejercicio 3.py
#### Codigo.
   
     import matplotlib.pyplot as plt

    def lineal_interpolation(x_values, y_values, x):
        for i in range(len(x_values) - 1):
            if x_values[i] <= x <= x_values[i + 1]:
                x0, y0 = x_values[i], y_values[i]
                x1, y1 = x_values[i + 1], y_values[i + 1]
                return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

    #Ejemplo de uso
    x_values = [1, 2, 3, 4, 5]
    y_values = [2, 4, 6, 8, 10]
    x = 3.5

    y = lineal_interpolation(x_values, y_values, x)
    print(f"El valor interpolado en x={x} es: {y}")

    #Gráfica de los puntos y la interpolación lineal
    plt.plot(x_values, y_values, 'o')
    plt.plot([x_values[0], x_values[-1]], [lineal_interpolation(x_values, y_values, x_values[0]), lineal_interpolation(x_values, y_values, x_values[-1])], 'r--')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interpolación Lineal')
        plt.show()
    
#### Comprobacion.
[![Captura-de-pantalla-2024-05-20-224835.png](https://i.postimg.cc/Qx2RpJyS/Captura-de-pantalla-2024-05-20-224835.png)](https://postimg.cc/D8cjhLFb)

### Ejercicio 4.py
#### Codigo.

     def f(x):
    return x**2

        def lineal_interpolation(x0, x1, x):
        y0 = f(x0)
        y1 = f(x1)
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

        #Ejemplo de uso
    x0 = 1
    x1 = 3
    x = 2

    y = lineal_interpolation(x0, x1, x)
    print(f"El valor interpolado en x={x} es: {y}")

   
#### Comprobacion.
[![Captura-de-pantalla-2024-05-20-224911.png](https://i.postimg.cc/Xv8m6S7D/Captura-de-pantalla-2024-05-20-224911.png)](https://postimg.cc/zLy0TQhn)
### Ejercicio 5.py
#### Codigo.

     def lineal_interpolation(x_values, y_values, x):
    for i in range(len(x_values) - 1):
        if x_values[i] <= x <= x_values[i + 1]:
            x0, y0 = x_values[i], y_values[i]
            x1, y1 = x_values[i + 1], y_values[i + 1]
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

        #Leer datos desde un archivo
         with open('datos.txt', 'r') as file:
             data = file.readlines()

                x_values = []
                y_values = []

        for line in data:
            x, y = map(float, line.split())
            x_values.append(x)
            y_values.append(y)

            x = 3.5  # Valor de x para interpolar

            y = lineal_interpolation(x_values, y_values, x)
            print(f"El valor interpolado en x={x} es: {y}")

#### Comprobacion.
[![Captura-de-pantalla-2024-05-20-224955.png](https://i.postimg.cc/MHcFBn0h/Captura-de-pantalla-2024-05-20-224955.png)](https://postimg.cc/hQBsWP5r)
