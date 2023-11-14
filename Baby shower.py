'''
Algoritmo para calcular el sueldo de “n” vendedores.
Cada sueldo está compuesto de un salario base y una comisión por ventas.
'''


Tvendedores = 0
Tsueldo = 0

flag = 1
while flag < 1:
  pV = input("¿Hay algun vendedor? (Si/No): ").lower().strip()
  print(" ")
  
  if pV != 'si':
    break
    
  else:
    NV = input("Nombre del vendedor: ") #Nombre del vendedor
    print(" ")
    SB = float(input("Salario base: ")) #Salario base 
    VR = float(input("Total de ventas del vendedor: ")) #Ventas realizadas 
    if VR < 3500:
      Com = 0.10*VR
    elif 3500<=VR<= 7000:
      Com = 0.10*VR
    else:
      Com = 0.15*VR

    Stotal  = SB + Com

    Tvendedores += 1
    Tsueldo += Stotal

    print(" ")
    print(f"Nombre del vendedor {NV}")
    print(f"Sueldo total: {Tsueldo}")
    print(" ")

while True:
  V = input("¿Hay algun otro vendedor? (Si/No): ").lower().strip() #Vendedor
  print(" ")
  if V != 'si':
    break
  else:
    NV = input("Nombre del vendedor: ") #Nombre del vendedor
    print(" ")
    SB = float(input('Salario base: ')) #Salario base 
    VR = float(input("Total de ventas del vendedor: ")) #Ventas realizadas 
    if VR < 3500:
      Com = 0.10*VR
    elif 3500<=VR<= 7000:
      Com = 0.10*VR
    else:
      Com = 0.15*VR

    Stotal  = SB + Com

    Tvendedores += 1
    Tsueldo += Stotal

    print(" ")
    print(f"Nombre del vendedor {NV}")
    print(f"Sueldo total: {Tsueldo}")
    print(" ")

print(" ")
print("Resumen:")
print(f"Totoal de vendedores: {Tvendedores}")
print(f"Suma de todos lo sueldos: {Tsueldo}")

'''
Algoritmo para obtener estadísticas de zoológico.
Realiza un algoritmo para obtener las estadísticas en un zoológico donde se requiere un
conteo y porcentaje de “n “ animales dentro de determinado rango de edades:
'''

print("CUantos animales hay e el zoologico y cuales son sus edadess?")
men=0
an=0
ma2y5=0
ma5y10=0
ma10=0
x=input("Hay un animal en el zoologico? si/no  ").lower()
while x=="si":
  men1=int(input("Cual es la edad del animal?  "))
  an=an+1
  if men1<=2 :
    men=men+1
  elif men1<=5 and men1>2:
    ma2y5=ma2y5+1
  elif men1<=10 and men1>5:
    ma5y10=ma5y10+1
  else:
    ma10=ma10+1
  x=input("Hay otro animal en el zoologico? si/no  ")
menf=(men*100)/an
ma2Y5f=(ma2y5*100)/an
ma5Y10f=(ma5y10*100)/an
ma10f=(ma10*100)/an
print("Hay",men,"animales menores a 2 años y representa el",menf,"% de animales")
print("Hay",ma2y5,"animales entre 2 y 5 años",ma2Y5f,"% de animales")
print("Hay",ma5y10,"animales entre 5 y 10 años",ma5Y10f,"% de animales")
print("Hay",ma10,"animales mayores a 10 años",ma10f,"% de animales")

'''
Generar un password de 8 caracteres.
Diseñar un algoritmo que introduzcas un password carácter por carácter hasta completar 8
caracteres y al final te reporte el password completo.
Puntos extras si realizas la validación. El password solo puede tener números y letras
'''

contraseña = ''
intento = 0
p=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9', 'A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R' ,'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
while len(contraseña) <= 7:
  print(" ")
  intento += 1 
  Caracter = input(f"{intento}) Ingresa el caracter de tu contraseña: ") 
  contraseña += Caracter

if all(Caracter in p for Caracter in contraseña):
  print(" ")
  print(f"Tu contraseña {contraseña} es valida")
else:
  print(" ")
  print(f"Tu contraseña {contraseña} es invalida")
