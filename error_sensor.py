cont=0
mal=0
d=int(input("Cuantas medidas de temperaturas tomaste"))
while d>cont:
  cont+=1
  print("Ingresa la temperatura numero",cont)
  temp=int(input())
  if 10>temp or temp>40:
    mal+=1
err=(mal/d)*100
print("El termometro se equivoco",mal,"veces")
print("el porcentaje de error fue de", err)
