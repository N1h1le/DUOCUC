from ast import Str
from cgi import print_form
from operator import index
import os
#---------VARIABLES-----------
opción_menu=""
código=""
lista_códigos=[]
nombre=""
lista_nombres=[]
precio=0
lista_precios=[]
país_origen=""
lista_país_origen=[]
estilo=""
lista_estilos=[]
avb=0
lista_avb=[]
observación=""
lista_observaciones=[]

#---------CÓDIGO PRINCIPAL-----------
while True:
    os.system("cls")
    opción_menu=str(input('''
    -------MENÚ-------
    1.- Registrar cerveza
    2.- Listar cervezas
    3.- Buscar cerveza por código 
    4.- Eliminar registro cerveza
    5.- Modificar registro cerveza
    6.- Buscar cervezas por estilo
    7.- Ingresar observaciones a cerveza 
    8.- Salir
                      
    Ingrese opción:   '''))
    
    if opción_menu=="1":        
        os.system("cls")
        print("\n-----REGISTRAR CERVEZA---------")
        código=str(input("Ingrese código: ")).strip().upper()
        while not len(código)==3:
            print("Error..debe ser 3 caracteres")
            código=str(input("Ingrese código: ")).strip().upper()
        lista_códigos.append(código)    
        
        nombre=str(input("Ingrese nombre: ")).strip().capitalize()
        while not len(nombre)>0:
            print("Error..no puede ser vacío")
            nombre=str(input("Ingrese nombre: ")).strip().capitalize()
        lista_nombres.append(nombre)
        
        precio=int(input("Ingrese precio $"))
        while not precio>0:
            print("Error..debe ser mayor a cero")
            precio=int(input("Ingrese precio $"))
        lista_precios.append(precio)    
        
        país_origen=str(input("Ingrese país origen: ")).strip().capitalize()
        while not len(país_origen)>0:
            print("Error..no puede ser vacío")
            país_origen=str(input("Ingrese país origen: ")).strip().capitalize()
        lista_país_origen.append(país_origen)    
            
        estilo=str(input("Ingrese estilo: ")).strip().lower()
        while estilo not in ["frutal","ale", "amber"]:
            print("Error..solo permite: frutal, ale o amber")
            estilo=str(input("Ingrese estilo: ")).strip().lower()
        lista_estilos.append(estilo)    
            
        avb=float(input("Ingrese avb:  "))
        while not avb>=0:
            print("Error..no puede ser negativo")
            avb=float(input("Ingrese avb:  "))
        lista_avb.append(avb)    
        
        op=str(input("¿Desea agregar observación? S/N")).strip().upper()
        if op=="S":
            fecha=str(input("Ingrese fecha dd/mm/aaaa:  "))
            observación=str(input("Ingrese observación: "))
            obs= f'''
                ------------OBS-----------
                Fecha: {fecha}
                Observación: {observación}
                 '''
        else:
            obs="Sin observación"    
        lista_observaciones.append(obs)    
        os.system("pause")
        
    if opción_menu=="2":
        os.system("cls")
        print("\n----------LISTAR----------")
        for k in range(len(lista_nombres)):
            print(f'''
            {lista_nombres[k]}  {lista_avb[k]}%      
                  ''')
        os.system("pause")
        
    if opción_menu=="3":
        os.system("cls")
        print("\n-----Buscar cerveza por código----")
        código=str(input("Ingrese código: ")).strip().upper()
        while not len(código)==3:
            print("Error..debe ser 3 caracteres")
            código=str(input("Ingrese código: ")).strip().upper()
        
        if código in lista_códigos:
            j = lista_códigos.index(código)
            print(f'''
            ----------Ficha Cerveza----------
            Código: {código}
            Nombre: {lista_nombres[j]}    AVB:{lista_avb[j]}%
            País Origen: {lista_país_origen[j]}
            Estilo: {lista_estilos[j]}
            Precio ${lista_precios[j]}
            Observaciones:
            {lista_observaciones[j]}
                  ''')
        else:
            print("NO ESTA REGISTRADO!!")
           
        
        os.system("pause")
        
    if opción_menu=="4":
        os.system("cls")
        print("\n------ELiminar un registro-------")
        código=str(input("Ingrese código: ")).strip().upper()
        while not len(código)==3:
            print("Error..debe ser 3 caracteres")
            código=str(input("Ingrese código: ")).strip().upper()
            
        if código not in lista_códigos:
            print("EL código no esta registrado")
        else:
            # obtenemos la posición a ELIMINAR
            j = lista_códigos.index(código)
            op = str(input(f'''
            Esta a punto de eliminar el registro de la 
            cerveza  {lista_nombres[j]}.
            ¿Estas seguro de borrar? S/N    ''')).upper()
            if op=="S":
                lista_códigos.pop(j)
                lista_nombres.pop(j)
                lista_precios.pop(j)
                lista_avb.pop(j)
                lista_país_origen.pop(j)
                lista_estilos.pop(j)
                lista_observaciones.pop(j)
            
        os.system("pause")
        
    if opción_menu=="5":
        os.system("cls")
        print("\n-----MODIFICAR REGISTRO CERVEZA---------")
        código=str(input("Ingrese código: ")).strip().upper()
        while not len(código)==3:
            print("Error..debe ser 3 caracteres")
            código=str(input("Ingrese código: ")).strip().upper()
        
        if código not in lista_códigos:
            print("NO esta el registro!!!!")    
        else:
            # averiguamos la posición
            j = lista_códigos.index(código)
            print("\n Cargamos la nueva información:")
            nombre=str(input("Ingrese nombre: ")).strip().capitalize()
            while not len(nombre)>0:
                print("Error..no puede ser vacío")
                nombre=str(input("Ingrese nombre: ")).strip().capitalize()
            lista_nombres[j]=nombre
            
            precio=int(input("Ingrese precio $"))
            while not precio>0:
                print("Error..debe ser mayor a cero")
                precio=int(input("Ingrese precio $"))
            lista_precios[j]= precio   
            
            país_origen=str(input("Ingrese país origen: ")).strip().capitalize()
            while not len(país_origen)>0:
                print("Error..no puede ser vacío")
                país_origen=str(input("Ingrese país origen: ")).strip().capitalize()
            lista_país_origen[j]=país_origen
                
            estilo=str(input("Ingrese estilo: ")).strip().lower()
            while estilo not in ["frutal","ale", "amber"]:
                print("Error..solo permite: frutal, ale o amber")
                estilo=str(input("Ingrese estilo: ")).strip().lower()
            lista_estilos[j]=estilo
                
            avb=float(input("Ingrese avb:  "))
            while not avb>=0:
                print("Error..no puede ser negativo")
                avb=float(input("Ingrese avb:  "))
            lista_avb[j]=avb  
            
            op=str(input("¿Desea agregar observación? S/N")).strip().upper()
            if op=="S":
                fecha=str(input("Ingrese fecha dd/mm/aaaa:  "))
                observación=str(input("Ingrese observación: "))
                obs= f'''
                    ------------OBS-----------
                    Fecha: {fecha}
                    Observación: {observación}
                    '''
            else:
                obs="Sin observación" 
            
            lista_observaciones[j]=obs
            
        os.system("pause")
        
    if opción_menu=="6":
        os.system("cls")
        print("\n-----Buscar cervezas por estilo--------")
        estilo=str(input("Ingrese estilo: ")).strip().lower()
        while estilo not in ["frutal","ale", "amber"]:
            print("Error..solo permite: frutal, ale o amber")
            estilo=str(input("Ingrese estilo: ")).strip().lower()
        
        print(f"----Cervezas tipo: {estilo.upper()}----")
        for k in range(len(lista_códigos)):
            if estilo== lista_estilos[k]:
                print(f'''
                {lista_nombres[k]}  {lista_avb[k]}%      
                    ''')            
            
        os.system("pause")
        
    if opción_menu=="7":
        os.system("cls")
        print("\n--------INGRESAR OBSERVACIÓN--------")
        código=str(input("Ingrese código: ")).strip().upper()
        while not len(código)==3:
            print("Error..debe ser 3 caracteres")
            código=str(input("Ingrese código: ")).strip().upper()
        
        if código in lista_códigos:
            j = lista_códigos.index(código)
            print(f'''
            ----------Ficha Cerveza----------
            Código: {código}
            Nombre: {lista_nombres[j]}    AVB:{lista_avb[j]}%
            País Origen: {lista_país_origen[j]}
            Estilo: {lista_estilos[j]}
            Precio ${lista_precios[j]}
            Observaciones:
            {lista_observaciones[j]}
                  ''')
            
            print("\n-----NUEVA OBSERVACIÓN---------")
            fecha=str(input("Ingrese fecha dd/mm/aaaa:  "))
            observación=str(input("Ingrese observación: "))
            obs= f'''
            ------------OBS-----------
                Fecha: {fecha}
                Observación: {observación}
                 ''' + lista_observaciones[j]
            lista_observaciones.pop(j)
            lista_observaciones.insert(j, obs)
        else:
            print("NO ESTA REGISTRADO!!")
                        
        os.system("pause")
        
    if opción_menu=="8":
        break
        
# Propuesto....listar las cervezas desde la de mayor
# grado alcohólico a la menor...nombre - avb        