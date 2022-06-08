import os
# ----------Variables---------
nombre="" # nombre del usuario
sexo=""   # puede ser F o M
edad=0     # edad del usuario
valor_hora=0 # valor de la hora de trabjao
hrs_trabajadas=0
# -------MAIN CODE-------
os.system("cls")
nombre = str(input("Ingrese nombre:  "))
sexo = str(input("ingrese sexo F/M:  "))
edad = int(input("Ingrese edad:   "))
valor_hora = int(input("ingrese valor hora $:   "))
hrs_trabajadas = float(input("ingrese hrs trabajadas:   "))

sueldo_bruto= valor_hora*hrs_trabajadas
salud = sueldo_bruto*0.07
pension = sueldo_bruto*0.13
liquido = sueldo_bruto-salud-pension
print (f'''
    ============LIQUIDACIÓN SUELDO============
       
       Nombre:{nombre}
       Edad:{edad} años         Sexo:{sexo}   
       Valor Hora ${valor_hora} Hrs. Traba.{hrs_trabajadas}
       Sueldo bruto ${sueldo_bruto}
       Dscto. salud ${salud}
       Dscto. pensión ${pension}
       Liquido pagar ${liquido}
       ''')






