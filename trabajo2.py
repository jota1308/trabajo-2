# trabajo 2 ejercicio 1
zen = """Beautiful is better than ugly.     
Explicit is better than implicit.  
Simple is better than complex.     
Complex is better than complicated.
Flat is better than nested.        
Sparse is better than dense.       
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

vocales = ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]
zen = zen.split("\n")  # Separo el texto en lineas
lista = []  # Creo una lista vacia
for i in zen:  # Recorro las lineas
    lista = i.split(" ")  # Separo las palabras de cada linea
    if lista[1].startswith(tuple(vocales)):  # Si la segunda palabra de la linea empieza con una vocal
        print(i)

print("------------------------------------------------")

# trabajo 2 ejercicio 2
titulos = ["Speedrun de Super Mario en tiempo récord","Charla sobre desarrollo de videojuegos","Jugando al nuevo FPS del momento con amigos","Música en vivo: improvisaciones al piano"]
contador = 0   # Creo un contador
for x in titulos:
    if len(x)>contador:    # Si la longitud de x es mayor al contador
        contador = len(x)   # El contador toma el valor de la longitud de x
        titulo = x    # Guardo el titulo
print(f' el titulo mas largo es: {titulo}')  # Imprimo el titulo mas largo

print("------------------------------------------------")

# trabajo 2 ejercicio 3
reglas = """Respeta a los demás. No se permiten insultos ni lenguaje
ofensivo.
Evita el spam. No publiques enlaces sospechosos o repetitivos.
No compartas información personal.
Usa los canales adecuados para cada tema.
Sigue las instrucciones de los moderadores."""
reglas = reglas.split(".")  # Separo el texto en lineas
clave = (input("Ingrese una palabra clave: "))  # Pido una palabra clave
clave = clave.lower()  # Convierto la palabra clave a minuscula
for i in reglas:  # Recorro las lineas
    i = i.lower()  # Convierto la linea a minuscula
    if clave in i:  # Si la palabra clave esta en la linea
        print(i)  # Imprimo la linea

print("------------------------------------------------")

# trabajo 2 ejercicio 4
nombre = input("ingrese un nombre de usuario: ") # Pido un nombre de usuario
aprobado = False
numero = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
nro = False
while not aprobado: # Mientras no este aprobado
    if len(nombre) < 5: # Si el nombre de usuario tiene menos de 5 caracteres
        nombre = input("El nombre de usuario debe tener al menos 5 caracteres: ")   # Pido un nuevo nombre de usuario
    if not nombre.isalnum(): # Si el nombre de usuario no es alfanumerico
        nombre = input("El nombre de usuario no puede contener caracteres especiales:  ")  # Pido un nuevo nombre de usuario
    for i in numero: # Recorro los numeros
        if i in nombre: # Si no hay un numero en el nombre de usuario
            nro = True
    if not nro:
        nombre = input("El nombre de usuario debe contener al menos un número: ")
    



