# Tema 3 - Métodos de solución de Sistemas de Ecuaciones

## ¿Qué es el método de Gauss Jordan?
  Es un algoritmo utilizado en álgebra lineal para encontrar las soluciones de un sistema de ecuaciones lineales o para encontrar la inversa de una matriz. 
  El método consiste en aplicar operaciones elementales de fila a una matriz ampliada que contiene tanto la matriz de coeficientes como el vector de términos 
  constantes en un sistema de ecuaciones lineales. Estas operaciones elementales de fila incluyen intercambio de filas, multiplicación de una fila por un escalar 
  no nulo y sumar un múltiplo de una fila a otra fila. El objetivo es llevar la matriz ampliada a una forma escalonada reducida (forma escalonada reducida por 
  filas) o a una forma diagonal si se busca la inversa de la matriz. Una vez que la matriz está en una de estas formas, se pueden identificar las soluciones del 
  sistema de ecuaciones o la inversa de la matriz directamente. El método de Gauss-Jordan es una extensión del método de eliminación de Gauss, y es especialmente 
  útil cuando se busca la inversa de una matriz o cuando se necesita resolver sistemas de ecuaciones lineales con múltiples soluciones.

## Índice
- [Método de Gauss-Jordan](Gauss_Jordan/Gauss_Jordan.md)
  - [Ejercicios del método de Gauss-Jordan](Gauss_Jordan/Codigos)

------------

## ¿Qué es el método de Gauss Seidel?
  El método de Gauss-Seidel es un algoritmo utilizado para resolver sistemas de ecuaciones lineales de forma iterativa. 
  Este método es una extensión del método de Jacobi y se utiliza comúnmente en álgebra lineal y en problemas de ingeniería, 
  física y matemáticas aplicadas.
  
  La idea básica detrás del método de Gauss-Seidel es resolver el sistema de ecuaciones lineales de manera iterativa, donde 
  en cada iteración se actualizan las soluciones de las ecuaciones utilizando los valores más recientes calculados en las 
  iteraciones anteriores. A diferencia del método de Jacobi, en el que se utilizan los valores de la iteración anterior para 
  actualizar todos los valores simultáneamente, en Gauss-Seidel, los valores actualizados se utilizan inmediatamente después 
  de ser calculados. Esto puede llevar a una convergencia más rápida en algunos casos.

## Índice
- [Método de Gauss-Seidel](Gauss_Seidel/Gauss_Seidel.md)
  - [Ejercicios del método de Gauss-Seidel](Gauss_Seidel/Codigos)

------------

## ¿Qué es el método de Gauss Simple?
  El método de Gauss consiste en transformar un sistema de ecuaciones lineales en uno equivalente pero más simple, utilizando 
  operaciones elementales sobre las filas de una matriz aumentada (una matriz que incluye tanto los coeficientes de las variables 
  como los términos constantes de las ecuaciones). Las operaciones elementales sobre las filas incluyen intercambiar filas, 
  multiplicar una fila por una constante distinta de cero y sumar o restar un múltiplo de una fila a otra fila.
  
  El objetivo del método de Gauss es reducir la matriz aumentada a una forma escalonada o escalonada reducida por filas, lo que 
  facilita la resolución del sistema de ecuaciones mediante sustitución hacia atrás.

## Índice
- [Método de Gauss-Simple](Gauss_Simple/Gauss_Simple.md)
  - [Ejercicios del método de Gauss-Simple](Gauss_Simple/Codigos)

------------

## ¿Qué es el método de Jacob?
  El método de Jacob (también conocido como el método de iteración de Jacobianos o el método de Jacobi) es 
  un algoritmo utilizado para resolver sistemas de ecuaciones lineales. Es un método iterativo que se utiliza 
  para aproximar la solución de sistemas de ecuaciones lineales, especialmente cuando estos sistemas son grandes 
  y sparse (es decir, tienen muchos ceros).
    
  El método de Jacob se basa en descomponer la matriz del sistema en una suma de una matriz diagonal y el resto 
  de la matriz. Luego, iterativamente, se resuelve un sistema de ecuaciones en el que la matriz del sistema es la 
  matriz diagonal y se actualizan las soluciones en cada iteración.
    
  El proceso se repite hasta que se alcanza una precisión deseada o se cumple algún otro criterio de convergencia. 
  Aunque el método de Jacob puede ser relativamente simple y fácil de implementar, puede converger lentamente para 
  ciertos tipos de sistemas de ecuaciones. Sin embargo, es útil como paso en métodos más avanzados como el método de 
  Gauss-Seidel o el método de relajación.
  
  El objetivo del método de Gauss es reducir la matriz aumentada a una forma escalonada o escalonada reducida por 
  filas, lo que facilita la resolución del sistema de ecuaciones mediante sustitución hacia atrás.
  
## Índice
- [Método de Jacob](Jacob/Jacob.md)
  - [Ejercicios del método de Jacob](Jacob/Codigos)
   
