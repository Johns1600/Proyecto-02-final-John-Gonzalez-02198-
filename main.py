#Proyecto 02 programación III (02198) John Gonzalez Valdez

import os   # Librería para limpiar pantalla.
from Ventana import *
from Producto import Articulo
from Proveedor import *


if __name__ == '__main__':

    ventana1 = Ventana()
    ventana1.visualizar_ventana()
    while True:
        os.system('cls')
        print("Bienvenido al menu")
        print("OP1.Consulta de precio ventas al por mayor")
        print("OP2.Registro de proveedores")
        print("OP3.Información de contacto de proveedores")
        print("OP4.")
        print("OP5.")
        print("OP6.Salir")

        try:
            opcionMenu = int(input("Selecciona la opcion: "))
        except ValueError:
            print("Error, debe ingresar un número entero (1 a 6)")
            input("Presiona enter para volver... ")
            continue

        if opcionMenu == 1:
            os.system('cls')

            Articulo1 = Articulo(205, "Producto 1", 5)
            Articulo1.CalculadoraUnidades()

            input("Presiona enter...")

        elif opcionMenu == 2:
            os.system('cls')

            Proveedor1 = Proveedor()
            Proveedor1.ingresarProveedores()
            Proveedor1.mostrarProveedores()
            Proveedor1.ContinuarIngresandoProveedores()

            input("Presiona enter...")

        elif opcionMenu == 3:
            pass

        elif opcionMenu == 4:
            pass

        elif opcionMenu == 5:
            pass

        elif opcionMenu == 6:
            break   # Opción salir, rompe la ejecución del "While".

        else:
            print("Error al seleccionar opcion")
            input("Presiona enter para volver... ")