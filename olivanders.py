clit=0
fret=input("entro un cliente? si/no:  ")
sac=0
esp=0
sau=0
ace=0
clitcom=0
clitno=0
while fret=="si":
  com=input("Compro algo? si/no:  ")
  clit+=1
  if com=="si":
    clitcom+=1
    print("Hay: Varitas de sauco(1), varita de espino(2), varita de sauce(3) y varita de acebo(4")
    prod=input("que varita compro 1, 2, 3, 4:  ")
    if prod==1:
      sac+=1
    elif prod==2:
      esp+=1
    elif prod==3:
      sau+=1
    elif prod==4:
      ace+=1
  else:
    clitno+=1  
  fret=input("entro un cliente? si/no:  ")
if fret=="no":
  print("Numero de clientes: ",clit)
  print("Numero de clientes que compraron:",clitcom)
  print("Numero de clientes que no compraron:",clitno)
  print("Numero de varitas de sauco vendidas:  " ,sac)
  print("Numero de varitas de espino vendidas:  " ,esp)
  print("Numero de varitas de sauce vendidas:  " ,sau)
  print("Numero de varitas de acebo vendidas:  " ,ace)
  print("Numero de varitas vendidas:  " ,sac+esp+sau+ace)
print("hojala vuelva pronto, joven mago")
