condicion="dormido"
while condicion =="dormido":
  print("o no snolrax esta dormido en el camino, no puedes pasar")
  opcion=input("que deseas acer? 1atraparlo 2 tocar la flauta")
  if opcion=="1":
    condicion="dormido"
  elif opcion=="2":
    condicion= "despierto"
  else:
    condicion="dormido"
  print("Genial, snorlax a despertado tio")
