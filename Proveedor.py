class Proveedor:
    def __init__(self):
        self.listaProveedores = []

    def agregarProveedor(self, nombre, tipoProducto, sucursal):
        proveedor = [nombre, tipoProducto, sucursal]
        self.listaProveedores.append(proveedor)

    def ingresarProveedores(self):
        cantidad = int(input("Ingrese la cantidad de proveedores a registrar: "))
        for i in range(cantidad):
            nombre = input(f"Ingrese el nombre del proveedor {i+1}: ")
            tipo_producto = input(f"Ingrese el tipo de productos del proveedor {i+1}: ")
            sucursal = input(f"Ingrese el nombre de la sucursal del proveedor {i+1}: ")
            self.agregarProveedor(nombre, tipo_producto, sucursal)

    def mostrarProveedores(self):
        if self.listaProveedores:
            print("Proveedores: \n")
            for proveedor in self.listaProveedores:
                print("Nombre del proveedor:", proveedor[0])
                print("Tipo de productos:", proveedor[1])
                print("Sucursal:", proveedor[2])
                print("------------------------")
        else:
            print("No hay proveedores registrados.")

    def mostrarTodasLasListas(self):
        for i, proveedor in enumerate(self.listaProveedores, start=1):
            print(f"Lista de proveedor {i}: {proveedor}")

    def ContinuarIngresandoProveedores(self):
        while True:
            opcion = input("¿Desea ingresar más proveedores? (si/no): ").lower()
            if opcion == "si":
                self.ingresarProveedores()
                print("\nProveedores registrados hasta el momento:")
                self.mostrarProveedores()
            elif opcion == "no":
                print("\nListas de todos los proveedores ingresados:")
                self.mostrarTodasLasListas()
                input("Presiona enter para continuar...")
                break
            else:
                print("Opción no válida. Por favor, ingrese 'si' o 'no'.")