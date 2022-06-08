import os

#____________________________ VARIABLES ______________________________________________
# Estamos creando las variables y las inicializamos, es decir, cargamos un valor
# inicial (" de arranque") para cada variable

opcion_menu=0        # Almacena la opción de menú seleccionada por el usuario
nombre_producto = "Sin información"   # carga el nombre del producto
precio_producto =0   # carga el valor  unitario del producto
cantidad_producto=0  # carga la cantidad requerida del producto
total_compra =0      # carga el total de la compra

con_delivery = "N"   # N indica que NO requiere servicio de delivery
monto_delivery =0    # carga el monto a agregar por concepto de despacho

#______________________________________________________________________________________
os.system("cls")
print('''
    _________________________________________
    |  Producto	Precio                      |
    | 1.-Mascarilla simple\t\t$1000           |
    | 2.-Mascarilla con diseño\t\t$1300       |
    |_______________________________________|
    

    ''')

opcion_menu = int(input("Ingrese opción de menú:  "))

if opcion_menu==1:
    nombre_producto="Mascarilla simple"
    precio_producto= 1000
elif opcion_menu==2:
    nombre_producto="Mascarilla con diseño"
    precio_producto= 1300


cantidad_producto = int(input(f"Ingrese la cantidad de {nombre_producto}:   "))

total_compra = precio_producto* cantidad_producto


#____________________________INICIO cobro delivery ________________________________________________
'''
Si la compra es superior a $15.000 el envío es gratis, en caso contrario:
-	Si es de la misma comuna el envío es de $1.000
-	En otro caso es de $3.000

'''
opcion_delivery = input('''
        ¿Desea servicio de delivery?  S/N   ''').upper()


if opcion_delivery=="S":
    if total_compra>15000:
        monto_delivery=0
        print("Libre de cobro de despacho por monto de la compra")
    else:
        despacho_misma_comuna= input('''
            ¿El despacho es en la misma comuna?  S/N   ''').upper()
        if despacho_misma_comuna=="S":
            monto_delivery=1000
        else:
            monto_delivery=3000

total_compra = total_compra + monto_delivery

#____________________________FIN cobro delivery ________________________________________________
            
os.system("cls")
print(f'''
    ===================== BOLETA =========================
    Nombre producto: {nombre_producto}  
    Cantidad: {cantidad_producto}
    Precio unitario ${precio_producto}
    
    Subtotal\t\t\t ${cantidad_producto*precio_producto}
    Cargo por delivery\t\t\t ${monto_delivery}
    
    
    Total a pagar\t\t\t ${total_compra}
      
    ''')
os.system("pause")


