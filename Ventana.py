# Clase llamada "ventana" contiene la programación de la interfaz gráfica

import tkinter as tk
from tkinter import messagebox

class Ventana:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ventana de Registro")
        self.ventana.geometry("300x300")

        self.label_nombre = tk.Label(self.ventana, text="Nombre:")
        self.label_nombre.pack()
        self.entry_nombre = tk.Entry(self.ventana)
        self.entry_nombre.pack()
        self.entry_nombre.bind('<Return>', lambda event: self.mostrar_bienvenida())

        self.label_apellido1 = tk.Label(self.ventana, text="Primer Apellido:")
        self.label_apellido1.pack()
        self.entry_apellido1 = tk.Entry(self.ventana)
        self.entry_apellido1.pack()
        self.entry_apellido1.bind('<Return>', lambda event: self.mostrar_bienvenida())

        self.label_apellido2 = tk.Label(self.ventana, text="Segundo Apellido:")
        self.label_apellido2.pack()
        self.entry_apellido2 = tk.Entry(self.ventana)
        self.entry_apellido2.pack()
        self.entry_apellido2.bind('<Return>', lambda event: self.mostrar_bienvenida())

        self.label_bienvenida = tk.Label(self.ventana, text="")

        self.boton_enviar = tk.Button(self.ventana, text="Enviar", command=self.mostrar_bienvenida)
        self.boton_enviar.pack()

    def mostrar_bienvenida(self):
        nombre = self.entry_nombre.get()
        apellido1 = self.entry_apellido1.get()
        apellido2 = self.entry_apellido2.get()

        self.label_nombre.pack_forget()
        self.label_apellido1.pack_forget()
        self.label_apellido2.pack_forget()
        self.entry_nombre.pack_forget()
        self.entry_apellido1.pack_forget()
        self.entry_apellido2.pack_forget()
        self.boton_enviar.pack_forget()

        mensaje_bienvenida = f"Bienvenido {nombre} {apellido1} {apellido2}"
        self.label_bienvenida.config(text=mensaje_bienvenida)
        self.label_bienvenida.pack()

        # Iniciar la cuenta regresiva antes de mostrar los botones
        self.cuenta_regresiva(5, nombre, apellido1, apellido2)

    def cuenta_regresiva(self, segundos_restantes, nombre, apellido1, apellido2):
        if segundos_restantes >= 0:
            mensaje = f"Bienvenido {nombre} {apellido1} {apellido2}, tiempo restante: {segundos_restantes} segundos"
            self.label_bienvenida.config(text=mensaje, fg="purple")
            self.ventana.after(1000, self.cuenta_regresiva, segundos_restantes - 1, nombre, apellido1, apellido2)
        else:
            # Cuando la cuenta regresiva llega a cero, mostrar los botones
            self.mostrar_botones()

    def mostrar_botones(self):
        # Ocultar el mensaje de bienvenida
        self.label_bienvenida.pack_forget()

        # Botón "Saltar"
        self.boton_salir = tk.Button(self.ventana, text="Omitir", fg="red", command=self.salir)
        self.boton_salir.pack(side=tk.LEFT, padx=10)

        # Botón "Info"
        self.boton_info = tk.Button(self.ventana, text="Info", fg="blue", command=self.mostrar_info_programa)
        self.boton_info.pack(side=tk.LEFT, padx=10)

        # Centrar los botones
        self.boton_salir.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.boton_info.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    def salir(self):
        self.ventana.destroy()

    def mostrar_info_programa(self):
        info = "Este programa es un registro de persona que solicita el nombre y los apellidos del usuario. Luego de ingresar los datos, muestra un mensaje de bienvenida con la información ingresada. Después de 6 segundos, se muestran dos botones adicionales: 'Saltar' para salir del programa y 'Info' para obtener una breve descripción del programa."
        messagebox.showinfo("Información del Programa", info)

    def visualizar_ventana(self):
        self.ventana.mainloop()