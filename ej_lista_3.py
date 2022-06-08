import os
# VAMOS A EMULAR UNA PEQUEÑA BD USANDO LISTAS

#-------------VARIABLES-------------
opcion_menu=""
nombre=""
lista_nombres=[]
edad=0
lista_edades=[]
lista_sexos=[] 
lista_sueldos=[]
#-------------CODIGO PRINCIPAL------------
while True:
    os.system("cls")
    opcion_menu=str(input('''
    -----------MENÚ-----------
    1.- Cargar datos
    2.- Listar datos
    3.- Salir
    
    Ingrese opción:  '''))
    
    if opcion_menu=="1":
        os.system("cls")
        print("\n-----CARGAR DATOS-----")
        nombre= str(input("Ingrese nombre: ")).strip()
        while not len(nombre)>0:
            print("Error...no puede ser vacío")
            nombre= str(input("Ingrese nombre: ")).strip()
        lista_nombres.append(nombre)
        
        edad= int(input("Ingrese edad: "))
        while not 18<=edad<=100:
            print("Error... valor entre 18 y 100")
            edad= int(input("ingrese edad: "))
        lista_edades.append(edad)
        
        sexo=str(input("Ingrese sexo: F/M ")).upper()
        while sexo not in ["F", "M"]:
            print("Error...solo es F o M")
            sexo=str(input("Ingrese sexo: F/M ")).upper()
        lista_sexos.append(sexo)
            
        sueldo=int(input("Ingrese sueldo $"))
        while not sueldo>=340000:
            print("error..min $340000")
            sueldo=int(input("Ingrese sueldo $"))
            lista_sueldos.append(sueldo)
        
        
        print(f'''
              {lista_nombres}
              {lista_edades}
              {lista_sexos}
              {lista_sueldos}
              ''')
        os.system("pause")
    
    
    if opcion_menu=="2":
        os.system("cls")
        print("\n------ Listar Datos ------")
        for k in range(len(lista_nombres)):
            print(f'''
            {lista_nombres[k]}  {lista_edades[k]} años
            {lista_sexos[k]} {lista_sueldos[k]}
            ''')
        os.system("pause")
    
    if opcion_menu=="3":
        break