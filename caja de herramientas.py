import random

def pedir_numero():
    try:
        herramienta = int(input())
        boolean = 1
    except ValueError:
        boolean = 0
        herramienta = 1000000
        print("Jaja, eso no es un numero")
    return herramienta, boolean

print("Caja de herramientas de [tu nombre]")
print("Dile adios al Syntax Error!")
print("Que deseas hacer?")
print("0 - Imprimir una variable")
print("1 - Pedirle algo al usuario")
print("2 - Crear un condicional")
print("3 - Crear un ciclo while")
print("4 - Crear un ciclo for")
print("5 - Crear una lista")
print("6 - Divertirme")

boolean = 0
while boolean == 0:
    herramienta, boolean=pedir_numero()

while boolean not in list(range(7)):
    print("Escribe un numero valido.")
    print(list(range(7)))
    herramienta, boolean=pedir_numero()
    while boolean == 0:
        herramienta, boolean=pedir_numero()

if boolean == 0:
    print("Usa la función:")
    print("    print()")
    print("Dentro del paréntesis puedes poner ya sea un texto que quieras entre comillas (dobles o simples funciona bien) o una variable, yeii")
    print("Ejemplos:")
    print("    print('Que ondiux')")
    print("    print('Elegiste el número',numero)")
elif boolean == 1:
    print("Usa la función:")
    print("    input()")
    print("Dentro del paréntesis puedes poner un texto indicando al usuario que debe de escribir, yeii")
    print("OJO: para usar el dato hay que meterlo dentro de una variable, y no olvides convertirlo al tipo de dato adecuado, awesome!")
    print("Los tipos de datos son número entero int(), número decimal float() y texto str()")
    print("Ejemplos:")
    print("    numero_entero = int(input())")
    print("    numero_decimal = float(input())")
    print("    texto = str(input())")
elif boolean == 2:
    print("Para crear un condicional usa if")
    print("Ejemplo:")
    print("__if numero <10:")
    print("_____print('El número es menor que 10'")
    print("__elif numero==10")
    print("_____print('El número es igual a 10')")
    print("___else:")
    print("_____print('El número es mayor a 10'")
    print("(elif) para la segunda opcion de respuesta")
    print("else para cualquier respuesta")
    #que el usuario coloque pero no se encuentra ni en (if) o (elif)) 
elif boolean==3:
  print("Para crear un ciclo while usa while")
  print("Primero definimos la variable")
  print("Ejemplo:")
  print("numero=0")
  print("Luego ponemos el while como condición")
  print("While numero>=9")
  print("Ahora se pone el lo que queremos que se repita")
  print("numero=numero+1")
  print("Ahora se imprime el resultado")
  print("print(numero)")
elif boolean == 4:
  print("el bucle for se utiliza para realizar listas en python,un ejemplo seria lo siguiente")
  print("fruit = [banana, pera , uva]")
elif boolean==5:
  print("Para crear una lista necesitamos poner cual es la lista")
  print("thislist=['apple' , 'banana' , 'cherry']")
  print("Ahora se imprime la lista, pedimos el resultado")
  print("print(thislist)") 

elif boolean== 6:
  aleatorio = random.randint(1,3)
  if aleatorio == 1:
      print("Las variables tipo float se llaman así porque en los decimales el punto flota, ja, que gracioso, no?")
  elif aleatorio == 2:
      print("Sabías que las computadoras no entienden las letras ni las palabras, solo entienden 0 y 1, imaginate hablar así, 000111000 jajaja que gracioso.")
