import os

#____________________________ VARIABLES __________________________________

opcion_menu= 0          # carga la opción de menú seleccionada por el usuario
valor_entrada = 12000   # el valor unitario por entrada
nombre_funcion = "Sin información"  # carga el nombre de la función
horario_funcion = "Sin información" # carga el horario de la función
cantidad_entradas=0     #carga la cantidad de entradas requeridas
total_pagar=0           # carga el total de la compra de entradas
monto_pagado =0         # el monto pagado por el usuario
monto_vuelto =0         # el monto del vuelto de la compra

#_________________________________________________________________________

os.system("cls")
print('''
    ____________________________________________
        FUNCIONES	HORARIO
        1.-Función matiné	10:00
        2.-Función tarde	15:00
        3.-Función vespertina	21:00
    _____________________________________________
     
''')
opcion_menu= int(input("Ingrese la opción de menú:   "))

if 1<= opcion_menu <= 3:
    # analizamos la opcion y cargamos el nombre y el horario de la función
    if opcion_menu==1:
        nombre_funcion="Función matiné"
        horario_funcion="10:00 hrs"
    elif opcion_menu==2:
        nombre_funcion="Función tarde"    
        horario_funcion="15:00 hrs"
    elif opcion_menu==3:
        nombre_funcion=" Función vespertina"
        horario_funcion="21:00 hrs"
        
    print(f'''
        Ud. seleccionó para la {nombre_funcion} a las {horario_funcion}
          ''')
    print(f"La entrada tiene un valor de ${valor_entrada}")
    cantidad_entradas= int(input("Ingrese la cantidad de entradas:  "))
    
    total_pagar = cantidad_entradas* valor_entrada
    
    monto_pagado = int(input(f'''
                
            Total pagar ${total_pagar}          
            
            Ingrese el monto pagar $'''))
    
    monto_vuelto = monto_pagado-total_pagar
    os.system("cls")
    print(f'''
       
       _____________ Ticket de Compra ___________________
       {nombre_funcion}     -   {horario_funcion}
       Cantidad de entradas: {cantidad_entradas} X ${valor_entrada}
       Total a pagar ${total_pagar}
       
       Dinero ingresado     ${monto_pagado}
       Vuelto       ${monto_vuelto}
       ___________________________________________________      
    
    ''')
    os.system("pause")
    
else:
    print("Error: opción de menú fuera de rango!!! Fin de ejecución...")
    os.system("pause")
    
    