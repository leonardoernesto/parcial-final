from random import randint
ramen = randint(1,10)
pan=0
flor=3
numero=0
print("Adivina el número del 1-10. Recuerda que tienes 3 intentos")
while pan<flor:
  bugambilla=int(input("Trata de adivinar"))
  pan+=1
  if bugambilla == numero:
    print(f"Haz adivinado en {pan}")
  elif bugambilla != numero:
    print("Numero equivocado, intenta de nuevo")
  else:
    print("Incorrecto.")
  if bugambilla == flor:
    print("No has conseguido adivinar y tus intentos han terminado")
