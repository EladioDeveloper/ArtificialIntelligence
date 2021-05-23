import msvcrt
import os
print("BIENVENIDO A BANCO GAFAPEMA")




diccApellidos = {"peña": "12345", "aracena": "23456" , "matos": "34567"}
diccCtas = {"12345": 10000, "23456": 5000 , "34567": 50000}

listaTran1 = ("12345", "D")
listaTran1 = ("23456", "R")
listaTran1 = ("34567", "C")

#Cliente1 = {'apellido': "peña", 'numCta': "1234", 'balance': "5000"}
#del(diccCtas['34567'])#para eliminar cualquier entrada
#diccCtas['234546'] = '4000'#para modificar el valor

opcion=0
while opcion != 4:

    apellido=input("escribir apellido:==> ")
    cuenta=diccApellidos[apellido]
    balance=diccCtas[cuenta]

    print ("seleccione el tipo de transaccion a realizar")
    print("1.Retiro")
    print("2.Deposito")
    print("3.Consulta")
    print("4.Salir")

    opcion=int(input("ingrese una opcion: "))

    if opcion ==1:
        cantidadretiro = int(input("Favor indique el monto a retirar: "))
        total = balance - cantidadretiro
        diccCtas[cuenta] = total

        print("Se acaba de deducir ",cantidadretiro," de su cuenta, ahora su nuevo monto es: ", diccCtas[cuenta])
        
       
    if opcion ==2:
        cantidaddeposito=input("Favor indique el monto a depositar")
        print("Se acaba de recibir su deposito de ",cantidaddeposito," en su cuenta")

    if opcion ==3:
        print("El Cliente", apellido, "con la cuenta",
        cuenta," tiene un balance de",balance," en su cuenta")

        msvcrt.getch()#para esperar hasta presionar una tecla
        os.system('cls||clear')#para limpiar pantalla

        #para consultar diccionario
        print(diccApellidos)
        #diccApellidos.get(apellido)
        diccApellidos[apellido] = '11111'#para modificar el valor
        
        print(cuenta)

    if opcion ==4:
        print("adios")
        exit