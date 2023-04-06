# Ejercicios de Logica de Programacion

### Pseudocodigo: Son las Instrucciones que va a seguir el programa pero sin hacerlo

Estos son unos ejemplos y ejercicios de Pseudocodigo para Mejorar la Logica de Programacion 

1. Encuentra el Numero mas grande
```
Lista Ejemplo = [1,2,10,20,5,3,2,9]
Inicializar max = primer elemento de la lista 
Para cada numero de la lista:
    Si numero > max:
        max = numero
Fin del Bucle        
Imprime max
```
```Python
lista = [1,2,10,20,5,3,2,9]
max = 1 
for numero in lista:
    if numero > max:
        max = numero
print("El numero mas grande de la lista es: " + str(max))
```

2. Promedio de Calificaciones
```
Ejemplo de Lista de Calificaciones = [10,9,7,6,6,10,8]
Inicializamos suma = 0
Para cada calificacion en la lista de calificaciones:
    suma = suma + calificacion
Fin del Bucle 
promedio = suma / numero de calificaciones
Imprime Promedio
```
```Python
lista_calificaciones = [10,9,7,6,6,10,8]
suma = 0
for calificacion in lista_calificaciones:
    suma = suma + calificacion
promedio = suma / len(lista_calificaciones)
print("El promedio de las calificaciones es: " + str(promedio))
```

3. Detector de Palindromos
```
Eliminar espacios de la palabra
Eliminar signos de puntuacion
Covertir la frase a solo minusculas
Inicializamos palabra_invertida igual a en blanco
- Invertir la palabra u oracion
Para cada letra desde la ultima posicion hasta la primera:
    Agrega la letra a palabra_invertida
Si palabra == palabra_invertida:
    imprime "Es palindromo"
Sino:
    Imprimimos "No es palindromo"
```
```Python
palabra = "Anita lava la tina"
palabra_signos = palabra.replace(",", "")
palabra_signos = palabra_signos.replace(".", "")
palabra_espacios = palabra_signos.replace(" ", "")
palabra_min = palabra_espacios.lower()
palabra_invertida = ""
for letra in range(len(palabra_min)-1, -1, -1):
    palabra_invertida += palabra_min[letra]
if palabra_invertida == palabra_min:
    print('"' + palabra_signos + '"' + " es un palindromo")
else:
    print('"' + palabra_signos + '"' + " no es un palindromo")
```

4. Números primos
Un número primo es un número mayor a 1 que tiene únicamente dos divisores positivos: el mismo y 1
El 7 es un número primo porque los únicos dos números enteros que al dividir al 7 nos da un resultado entero y son residuo son el 7 (el mismo número) y el 1
```
Inicializamos numero_usuario igual a Ingresar un numero
Inicializamos numero_divisor = 2
Mientras numero_usuario sea > numero_divisor:
    Si numero_usuario%numero_divisor == 0:
        Imprime El numero_usuario no es primo
            Rompe el bucle
    Por el contrario si numero_usuario%numero_divisor != 0:
            numero_divisor = numero_divisor+1
Si numero_usuario == numero_divisor:
    Imprime El numero_usuario es primo
Por el contrario si numero usuario < 2:
    Imprime El numero_usuario no es primo
```
```Python
numero_usuario = 187237
numero_divisor = 2
while numero_usuario > numero_divisor:
    if numero_usuario%numero_divisor == 0:
        print("El numero " + str(numero_usuario) + " no es primo")
        break
    elif numero_usuario%numero_divisor != 0:
        numero_divisor = numero_divisor + 1
if numero_usuario == numero_divisor:
    print("El numero " + str(numero_usuario) + " es primo")
elif numero_usuario < 2:
    print("El numero " + str(numero_usuario) + " no es primo")
```

5. Serie fibonacci
Es una secuencia de números en la que cada número es la suma de los dos anteriores comenzando con un 0 y un 1. Ejemplo:
0, 1, 1, 2, 3, 5, 8, 13, 21,...
```
Inicializamos primer_elemento = 0
Inicializamos segundo_elemento = 1
Inicializamos tercer_elemento = 0
Para todos los elementos en un rango de 10
    Imprime tercer_elemento segudo de una coma y un espacio
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34,...  
    tercer_elemento = primer_elemento + segundo_elemento
    (0 + 1) = 1, (1 + 1) = 2, (1 + 2) = 3, (2 + 3) = 5, (3 + 5) = 8, (5 + 8) = 13, (8 + 13) = 21, (13 + 21) = 34,...
    primer_elemento = segundo_elemento
    1 = 1, 1 = 1, 2 = 2, 3 = 3, 5 = 5, 8 = 8, 13 = 13, 21 = 21
    segundo_elemento = tercer_elemento
    1 = 1, 2 = 2, 3 = 3, 5 = 5, 8 = 8, 13 = 13, 21 = 21, 34 = 34
Fin del Bucle
```
```Python
primer_elemento = 0
segundo_elemento = 1
tercer_elemento = 0
for elementos in range(10):
    print(tercer_elemento, end = ", ")
    tercer_elemento = primer_elemento + segundo_elemento
    primer_elemento = segundo_elemento
    segundo_elemento = tercer_elemento
print("...")
```

6. Contador de palabras
```
Inicializar palabras = "texto del cual queremos saber el numero de palabras"
Inicializamos lista_palabras = transformar el texto en una lista con el separador espacio " "
Inicializamos contador = el numero de elementos que contiene la lista_palabras
Imprime "El numero de palabras es: " + contador
```
```Python
palabras = "El mar rugía con fuerza mientras las olas se estrellaban contra las rocas. El viento soplaba con intensidad, despeinando el cabello de la joven que observaba el horizonte con nostalgia."
lista_palabras = palabras.split(" ")
contador = len(lista_palabras)
print("El numero de palabras es: " + str(contador))
```

7. Imprimir todas las tablas de multiplicar del 1 al 10 con un bucle
```
Inicializar multiplicando = 1
Inicializar multiplicador = 1
Inicializar producto = 0
Mientras multiplicando sea < 11:
    producto = multiplicando * multiplicador
    Imprime multiplicando * multiplicador = producto
    multiplicador = multiplicador + 1
    Si multiplicador > 10:
        multiplicador = multiplicador - 10
        multiplicando = multiplicando + 1
```
```Python
multiplicando = 1
multiplicador = 1
producto = 0
while multiplicando < 11:
    producto = multiplicando * multiplicador
    print(f"{multiplicando} * {multiplicador} = {producto}")
    multiplicador = multiplicador + 1
    if multiplicador > 10:
        multiplicador = multiplicador - 10
        multiplicando = multiplicando + 1
```

8. Conversión de temperatura de Celsius a Fahrenheit y viceversa dependiendo de lo que el usuario quiera.
```
Inicializamos entrada_usuario = "Celsius" o "Fahrenheit"
entrada_usuario = entrada_usuario en minusculas
Si entrada_usuario == "celsius":
    celsius = "Ingrese los grados Celsius: "
    fahrenheit = (celsius * 1.8) + 32
    Imprime "grados celcius a grados fahrenheit"
Por el Contrario si entrada_usuario == "fahrenheit":
    fahrenheit = "Ingrese los grados Fahrenheit: "
    celsius = (fahrenheit - 32) / 1.8
    Imprime "grados fahrenheit a grados celsius"
Sino:
    Imprime "Error"
```
```Python
entrada_usuario = str(input("Ingrese el nombre del dato conocido 'Celsius' o 'Fahrenheit': "))
entrada_usuario = entrada_usuario.lower()
if entrada_usuario == "celsius":
    celsius = float(input("Ingrese los °C: "))
    fahrenheit = (celsius * 1.8) + 32
    print(f"{celsius}°C es igual a {fahrenheit}°F")
elif entrada_usuario == "fahrenheit":
    fahrenheit = float(input("Ingrese los °F: "))
    celsius = (fahrenheit - 32) / 1.8
    print(f"{fahrenheit} °F es igual a {celsius} °C")
else:
    print("Error")
```