ret=0
amen=0
ah=float(input("Cuanto dinero tienes ahorrado en tu cuenta?  "))
tilin=int(input("Cuantos retiros vas a realizar?  "))
sal= ah
while tilin <= 3:
  ret+=1
  es=float(input("de cuanto sera su primer retiro?  "))
  sal=ah-es
  amen+=es
if tilin>3:
  print("el numero maximo de retiros es 3")
print("Contabas con un saldo de:",ah)
print("Tu nuevo saldo es de: ", sal)
print("Tus retirosnetos fueron de,",amen)
