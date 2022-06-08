import os
import time

# -------------------- Variables -----------------------------------------------
opcion_menu = 0   # almacena la opción de menú que eligio el usuario
nombre_cafe = "sin información"   # guarda el nombre del café
precio_cafe = 0
cantidad_cafe = 0  # guarda la cantidad de productos que solicita el user


opcion_agregado = "N"  # "N" indica que el user no desea agregado, "S" lo contrario
opcion_menu_agregado = 0  # almacena la opción de menú entre los agregados
# guarda el o los agregados seleccionados por el user
nombre_agregado = "sin información"
precio_agregado = 0


total_compra = 0   # guarda el monto total de compra
# esto será:  (precio_cafe + precio_agregado)*cantidad_cafe

# -------------------------------------------------------------------------------


os.system("cls")
print('''
       ============= MENU ==================
        1.- Espresso $750 
        2.- Cappuccino $850 
        3.- Latte $800
        4.- Mocha $830
        
       ''')
opcion_menu = int(input("Ingrese su opción de menú:  "))

if opcion_menu == 1:
    nombre_cafe = "Espresso"
    precio_cafe = 750

if opcion_menu == 2:
    nombre_cafe = "Cappuccino"
    precio_cafe = 850

if opcion_menu == 3:
    nombre_cafe = "Latte"
    precio_cafe = 800

if opcion_menu == 4:
    nombre_cafe = "Mocha"
    precio_cafe = 830


cantidad_cafe = int(input(f'''
                          
   Ingrese la cantidad de {nombre_cafe} que desea:      '''))

opcion_agregado = str(input('''
                          
   Desea agregados:  S/N   '''))

if opcion_agregado.upper() == "S":
    print('''
       ============= MENÚ Agregados ==================
        1.- Leche $300 
        2.- Chocolate $200 
        3.- Ambos (Leche + chocolate) $500
        
       ''')
    opcion_menu_agregado = int(input("Ingrese opción agregado:  "))
    if opcion_menu_agregado == 1:
        nombre_agregado = "Leche"
        precio_agregado = 300
    elif opcion_agregado == 2:
        nombre_agregado = "Chocolate"
        precio_agregado = 200
    else:
        nombre_agregado = "Ambos (Leche + chocolate)"
        precio_agregado = 500


total_compra = (precio_cafe + precio_agregado)*cantidad_cafe

print(f'''
      Total compra: ${total_compra}
      
      ''')
os.system("pause")


os.system("cls")
if opcion_agregado.upper() == "S":
    print(f'''
        
        =============== TICKET ===============
        Tipo café: {nombre_cafe}  ${precio_cafe} C/U 
        Agregados: {nombre_agregado}   ${precio_agregado} --> ${precio_cafe+precio_agregado} C/U
        Cantidad:{cantidad_cafe}
        Total compra:$ {total_compra}
        
        ''')
else:
    print(f'''
        
        =============== TICKET ===============
        Tipo café: {nombre_cafe}  ${precio_cafe} C/U 
        Cantidad: {cantidad_cafe}
        Total compra:$ {total_compra}
        
        ''')
