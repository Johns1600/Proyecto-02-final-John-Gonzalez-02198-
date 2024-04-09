class Producto:
    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        self.__codigo = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        self.__precio = valor

    def calcular_total(self, unidades):
        return self.precio * unidades

    def mostrar_resultado_individual(self, unidades):
        total_individual = self.calcular_total(unidades)
        print("Total a pagar por", self.nombre, ":", total_individual)

    def __str__(self):
        return 'Codigo: ' + str(self.__codigo) + ', nombre: ' + self.__nombre + ', precio: ' + str(self.__precio)


class Articulo(Producto):
    def __init__(self, codigo, nombre, precio):
        super().__init__(codigo, nombre, precio)

    def CalculadoraUnidades(self):
        # Crear objetos de la clase ProductoHeredado
        p1 = Articulo(205, "Producto 1", 5)
        p2 = Articulo(210, "Producto 2", 10)
        p3 = Articulo(220, "Producto 3", 20)

        while True:
            # Solicitar al usuario qué productos quiere comprar
            print("Productos disponibles:")
            print("Cod: 205. Producto 1")
            print("Cod: 210. Producto 2")
            print("Cod: 220. Producto 3")
            print("Salir: 4")
            productos_a_comprar = input(
                "Ingrese el codigo(s) de producto(s) que desea comprar (separados por coma): ").split(',')

            # Calcular y mostrar el resultado individual para cada producto seleccionado
            for producto in productos_a_comprar:
                if producto.strip() == '205':
                    unidades_p1 = int(input("Ingrese las unidades para el Producto 1: "))
                    p1.mostrar_resultado_individual(unidades_p1)
                elif producto.strip() == '210':
                    unidades_p2 = int(input("Ingrese las unidades para el Producto 2: "))
                    p2.mostrar_resultado_individual(unidades_p2)
                elif producto.strip() == '220':
                    unidades_p3 = int(input("Ingrese las unidades para el Producto 3: "))
                    p3.mostrar_resultado_individual(unidades_p3)
                elif producto.strip() == '4':
                    break
                else:
                    print("El número de producto ingresado no es válido.")

            if '4' in productos_a_comprar:
                break  # Salir del bucle while