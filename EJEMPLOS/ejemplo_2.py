import os  #---> libreria del SISTEMA OPERATIVO


os.system("cls")  #--> clean screen
nombre = str(input("ingrese nombre: "))
edad = int(input("ingrese edad: "))

# imprimir en bloque los datos obtenidos
os.system("cls")
print(f'''
      Nombre: {nombre}
      Edad: {edad}
      ''')