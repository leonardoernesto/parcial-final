patata=0 
tilin=0
while True:
  patata2=0
  tilin+=1
  nombre= input("Cual es tu nombre?")
  print(""" Zona 1 - $ 2000, 
  Zona 2 - $ 1000  
  Zona 3 - $ 700 """)
  z=input(f"en que zona estas,{nombre}? (1,2,3)")
  if z== "1":
    patata2+=2000
    print("Son $2000")
  elif z=="2":
    patata2+=1000
    print("Son $1000")
  elif z=="3":
    patata2+=700
    print("Son $700")
  patata+=patata2 
  caballo=input("Que dia es el concierto?").lower()

  if caballo in ["viernes","sabado","domingo"]: 
    print("No aplica")
  elif caballo in ["lunes","martes","miercoles","jueves"]:
    perro=input("Cupones? (si/no)").lower()
    if perro=="si":
      Ag=input("Cuales tienes? (1.Platino 500, 2.Oro 300 y 3.Plata 200)")
      if Ag=="1":
        patata-=500
      elif Ag=="2":
        patata-=300
      elif Ag=="3":
        patata-=200
      else:
        print("No hay")
    else:
      print("va")
  else: 
    print("No existe")
  print(f"nombre:{nombre}, su total el:{patata}")   
  x=input("Hay otro cliente?: ").lower()
  if x !="si":
    break 
  else: 
    print("")
print(f"reporte:total{tilin}")  
print(f"total ganancias:{patata}")
