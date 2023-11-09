mont=0
gas=0
cos=float(input("Que tantas cosas compraste en tu viaje"))
while mont<cos:
  mont+=1
  din=float(input("cuanto costo esa cosa?  "))
  gas+=din
print("Tu numero total de gastos fueron   $",gas)
