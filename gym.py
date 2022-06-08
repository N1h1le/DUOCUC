import os
# -------------variables------------
nombre=""
lista_nombres=[]
edad=0
lista_edades=[]
peso=0
lista_pesos=[]
estatura=0
lista_estaturas=[]
imc=0
lista_imc=[]
clasificacion=""
lista_clasificaciones=[]
menu=""

# _----------codigo--------
os.system("cls")
while True:
    menu=str(input('''
    ----------MENU-----------
    1.-Ingresar usuario
    2.-Datos de usuarios
    3.-Buscar usuario
    4.-eliminar Usuario
    5.-Modificar Usuario
    6.-salir
    elija opcion: '''))
    if menu=="1":
        os.system("cls")
        print("Ingresar datos de usuario")
        nombre=str(input("Ingrese nombre: ")).strip().capitalize()
        while not len(nombre)>0:
            print("Error...no puede ser vacio")
            nombre=str(input("Ingrese nombre: ")).strip().capitalize()
        lista_nombres.append(nombre)
        edad = int(input("Ingrese edad: "))
        while not 0<=edad<=110:
            print("Error, fuera rango[0 a 110] ")
            edad = int(input("Ingrese edad: "))
        lista_edades.append(edad)
        peso = int(input("Ingrese su peso(kilogramos): "))
        while not 0<peso:
            print("Ingrese su peso}¡¡¡")
            peso = int(input("Ingrese su peso(kilogramos): "))
        lista_pesos.append(peso)
        estatura= float(input("Ingrese su estatura(metros): "))
        while not 0<estatura<4.0:
            print("Ingrese su estatura¡¡¡¡")
            estatura= float(input("Ingrese su estatura(metros): "))
        lista_estaturas.append(estatura)
        imc=peso/estatura**2
        if(imc<16.00):
            clasificacion= "Infrapeso: Delgadez Severa"
        elif(16.00<=imc<=16.99):
            clasificacion="Infrapeso: Delgadez Moderada"
        elif(17.00<=imc<=18.49):
            clasificacion="Infrapeso: Delgadez Aceptable"
        elif(18.50<=imc<=24.99):
            clasificacion="Peso Normal"
        elif(25.00<=imc<=29.99):
            clasificacion="Sobrepeso"
        elif(30.00<=imc<=34.99):
            clasificacion="Obeso: Tipo 1"
        elif(35.00<=imc<=40.00):
            clasificacion="Obeso: Tipo 2"
        elif(imc>40.00):
            clasificacion="Obeso: Tipo 3"
        cl=round(imc,2)
        lista_imc.append(cl)
        lista_clasificaciones.append(clasificacion)
        os.system("pause")
        os.system("cls")
    if menu=="2":
        os.system("cls")
        print("\n----------Usuarios----------")
        for k in range(len(lista_nombres)):
            print(f'''
        Nombre:{lista_nombres[k]}  \tedad:{lista_edades[k]} años
        peso:{lista_pesos[k]}kg\tEstatura:{lista_estaturas[k]}m
        imc:{lista_imc[k]}\tClasificacion:{lista_clasificaciones[k]}
            ''')
        os.system("pause")
        os.system("cls")
    if  menu=="3":
        os.system("cls")
        nombre=str(input("Ingrese nombre: ")).strip().capitalize()
        while not len(nombre)>0:
            print("Error...no puede ser vacio")
            nombre=str(input("Ingrese nombre: ")).strip().capitalize()
        if nombre in lista_nombres:
            n = lista_nombres.index(nombre)
            print(f'''
        Nombre:{lista_nombres[n]}  \tedad:{lista_edades[n]} años
        peso:{lista_pesos[n]}kg\tEstatura:{lista_estaturas[n]}m
        imc:{lista_imc[n]}\tClasificacion:{lista_clasificaciones[n]}
            ''')
        else:
            print("Usuario no resgistrado¡¡¡")
        os.system("pause")
        os.system("cls")
    if menu=="4":
        os.system("cls")
        nombre=str(input("Ingrese nombre: ")).strip().capitalize()
        while not len(nombre)>0:
            print("Error...no puede ser vacio")
            nombre=str(input("Ingrese nombre: ")).strip().capitalize()
        if nombre not in lista_nombres:
            print("EL nombre no esta registrado")
        else:
            # obtenemos la posición a ELIMINAR
            j = lista_nombres.index(nombre)
            op = str(input(f'''
    Esta a punto de eliminar el registro de el
    Usuario: {lista_nombres[j]}.
    ¿Estas seguro de borrar? S/N    ''')).upper()
            if op=="S":
                lista_nombres.pop(j)
                lista_edades.pop(j)
                lista_pesos.pop(j)
                lista_estaturas.pop(j)
                lista_imc.pop(j)
                lista_clasificaciones.pop(j)
        os.system("pause")
        os.system("cls")
    if menu=="5":
            os.system("cls")
            nombre=str(input("Ingrese nombre: ")).strip().capitalize()
            while not len(nombre)>0:
                print("Error...no puede ser vacio")
                nombre=str(input("Ingrese nombre: ")).strip().capitalize()
            if nombre not in lista_nombres:
                print("NO esta el registro!!!!")
            else:
                j = lista_nombres.index(nombre)
                print("\n Cargamos la nueva información:")
                nombre=str(input("Ingrese nombre: ")).strip().capitalize()
                while not len(nombre)>0:
                    print("Error..no puede ser vacio")
                    nombre=str(input("Ingrese nombre: ")).strip().capitalize()
                lista_nombres[j]=nombre
                edad = int(input("Ingrese edad: "))
                while not 0<=edad<=110:
                    print("Error, fuera rango[0 a 110] ")
                    edad = int(input("Ingrese edad: "))
                lista_edades[j]=edad
                peso = int(input("Ingrese su peso(kilogramos): "))
                while not 0<peso:
                    print("Ingrese su peso}¡¡¡")
                    peso = int(input("Ingrese su peso(kilogramos): "))
                lista_pesos[j]=peso
                estatura= float(input("Ingrese su estatura(metros): "))
                while not 0<estatura:
                    print("Ingrese su estatura¡¡¡¡")
                    estatura= float(input("Ingrese su estatura(metros): "))
                lista_estaturas[j]=estatura
                imc=peso/estatura**2
                if(imc<16.00):
                    clasificacion= "Infrapeso: Delgadez Severa"
                elif(16.00<=imc<=16.99):
                    clasificacion="Infrapeso: Delgadez Moderada"
                elif(17.00<=imc<=18.49):
                    clasificacion="Infrapeso: Delgadez Aceptable"
                elif(18.50<=imc<=24.99):
                    clasificacion="Peso Normal"
                elif(25.00<=imc<=29.99):
                    clasificacion="Sobrepeso"
                elif(30.00<=imc<=34.99):
                    clasificacion="Obeso: Tipo 1"
                elif(35.00<=imc<=40.00):
                    clasificacion="Obeso: Tipo 2"
                elif(imc>40.00):
                    clasificacion="Obeso: Tipo 3"
                cl=round(imc,2)
                lista_imc[j]=cl
                lista_clasificaciones[j]=clasificacion
            os.system("pause")
            os.system("cls")
    if menu=="6":
        os.system("cls")
        op=str(input("estas seguro de salir? S/N  ")).upper()
        if op=="S":
            break