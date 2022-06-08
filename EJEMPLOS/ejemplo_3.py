import os 
os.system("cls")
Nota_1 = float(input("ingrese Nota_1: "))
Nota_2 = float(input("ingrese Nota_2: "))
Nota_3 = float(input("ingrese Nota_3: "))
promedio = (Nota_1+Nota_2+Nota_3)/3
if promedio>=4:
    estado ="APROBADO"
else:
    estado ="REPROBADO"
os.system("cls")
print (f'''
       -----TICKET-----
       Nota1:{Nota_1} Nota2:{Nota_2} Nota3:{Nota_3}
       Promedio: {promedio}   Estado:{estado}
       ''')
