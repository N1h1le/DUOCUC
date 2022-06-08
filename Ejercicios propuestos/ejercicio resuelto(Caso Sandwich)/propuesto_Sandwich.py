import os

#_________________________ VARIABLES GLOBALES ______________________________
cant_churrasco=0
cant_completo=0
cant_vegetariano=0
cant_barros_luco=0
valor_churrasco= 1500
valor_completo=1000
valor_vegetariano=1200
valor_barros_luco=3000
cant_total_productos = 0   #--> sera la suma de productos comprados
posee_codigo_descuento=False
#_______________________________________________________________________

os.system("cls")

print(f'''
      
         Producto           Precio
       1 Churrasco          $1500
       2 Completo           $1000
       3 Vegetariano        $1200
       4 Barros Luco        $3000

      
      ''')

cant_churrasco = int(input("ingrese la cantidad de churrascos:  "))
cant_completo = int(input("ingrese la cantidad de completos:  "))
cant_vegetariano = int(input("ingrese la cantidad de vegetarianos:  "))
cant_barros_luco = int(input("ingrese la cantidad de barros luco:  "))

total_pagar = cant_churrasco*valor_churrasco+ cant_completo*valor_completo+cant_vegetariano*valor_vegetariano+cant_barros_luco*valor_barros_luco

os.system("cls")

print("Su pedido consta de:    ")
if cant_churrasco>0:
    print(f"Churrasco X {cant_churrasco}  \t\t ${cant_churrasco*valor_churrasco}  ")
if cant_completo>0:
    print(f"Completo X {cant_completo}  \t\t ${cant_completo*valor_completo}  ")
if cant_vegetariano>0:
    print(f"Vegetariano X {cant_vegetariano}  \t\t ${cant_vegetariano*valor_vegetariano}  ")
if cant_barros_luco>0:
    print(f"Barros Luco X {cant_barros_luco}  \t\t ${cant_barros_luco*valor_barros_luco}  ")
    
print(f'''
    ______________________________
      Total a pagar ${total_pagar}
    ______________________________
      
      
    ''')


codigo =int(input('''
    Posee codigo de descuento:
    1. Si 
    2. No
                  
    '''))

if codigo==1:
    posee_codigo_descuento=True
    
if posee_codigo_descuento:
    monto_descuento= total_pagar*0.1
    


total_pagar = total_pagar - monto_descuento

os.system("cls")
print("Su pedido consta de:    ")
if cant_churrasco>0:
    print(f"Churrasco X {cant_churrasco}  \t\t ${cant_churrasco*valor_churrasco}  ")
if cant_completo>0:
    print(f"Completo X {cant_completo}  \t\t ${cant_completo*valor_completo}  ")
if cant_vegetariano>0:
    print(f"Vegetariano X {cant_vegetariano}  \t\t ${cant_vegetariano*valor_vegetariano}  ")
if cant_barros_luco>0:
    print(f"Barros Luco X {cant_barros_luco}  \t\t ${cant_barros_luco*valor_barros_luco}  ")


if posee_codigo_descuento==True:
    print(f"Descuento de 10%  -${monto_descuento}")
 
print(f'''
    ______________________________
      Total a pagar ${total_pagar}
    ______________________________
      
      
    ''')



reparto =input(" ¿Desea reparto a domicilio: S/N  ")

if reparto=="S":
    total_pagar= total_pagar+1500
    print("Se le suma $1500 al total de la compra")
    
    
    
print(f'''
    ______________________________
      Total a pagar ${total_pagar}
    ______________________________
      
      
    ''')
