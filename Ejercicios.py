# 1. Encuentra el Numero mas grande
lista = [1,2,10,20,5,3,2,9]
max = 1 
for numero in lista:
    if numero > max:
        max = numero
print("El numero mas grande de la lista es: " + str(max))

# 2. Promedio de Calificaciones
lista_calificaciones = [10,9,7,6,6,10,8]
suma = 0
for calificacion in lista_calificaciones:
    suma = suma + calificacion
promedio = suma / len(lista_calificaciones)
print("El promedio de las calificaciones es: " + str(promedio))

# 3. Detector de Palindromos
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

# 4. Números primos
numero_usuario = 1
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

# 5. Serie fibonacci
primer_elemento = 0
segundo_elemento = 1
tercer_elemento = 0
for elementos in range(10):
    print(tercer_elemento, end = ", ")
    tercer_elemento = primer_elemento + segundo_elemento
    primer_elemento = segundo_elemento
    segundo_elemento = tercer_elemento
print("...")

# 6. Contador de palabras
palabras = "El mar rugía con fuerza mientras las olas se estrellaban contra las rocas. El viento soplaba con intensidad, despeinando el cabello de la joven que observaba el horizonte con nostalgia."
lista_palabras = palabras.split(" ")
contador = len(lista_palabras)
print("El numero de palabras es: " + str(contador))

# 7. Imprimir todas las tablas de multiplicar del 1 al 10 con un bucle
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

# 8. Conversión de temperatura de Celsius a Fahrenheit y viceversa
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