##1

nombres=[]
contador = 0
while (contador <3):
    nombres.append(input("ingrese un nombre →"))
    contador = contador +1    
aux = 0 
largo = 0
for i in range(3):
    if (i == 0 ):
        largo = len(nombres[i])
    
    else:
        if (largo < len(nombres[i])):
            aux = i
            largo = len(nombres[i])
print (nombres[aux])
"""

##2
""" 
nombres = []
apellidos = []

for i in range (3):
    nombres.append(input("ingrese nombre →"))
    apellidos.append(input("ingrese apellido →"))

for i in range (3):
    print(f"{i+1}) {nombres[i]} {apellidos[i]}")





