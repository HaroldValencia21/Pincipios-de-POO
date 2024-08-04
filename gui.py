# gui.py

import tkinter as tk
from tkinter import ttk, messagebox
from gestor_vehiculos import GestorVehiculos, Coche, Microbus, FurgonetaCarga, Camion

class GUI:
    def __init__(self, root, gestor):
        self.root = root
        self.root.title("Alquiler de Vehículos")
        self.root.config(background="#cfcec9")
        self.gestor = gestor

        self.frameMain = tk.Frame(root, width=780, height=300, padx=10, bg="#17181d")
        self.frameMain.grid(row=1, column=0, pady=10)
        self.frameMain.grid_propagate(False)

        self.frameRegistro = self.crear_frame_registro(self.frameMain)
        self.frameAlquilar = self.crear_frame_alquilar(self.frameMain)
        self.frameLista = self.crear_frame_lista(self.frameMain)

        self.frameOpciones = self.crear_frame_opciones(root)
        
        self.mostrar_frame(self.frameRegistro)  # Mostrar el frame de registro por defecto

    def crear_frame_registro(self, parent):
        frame = tk.Frame(parent, width=780, height=300, padx=10, bg="#17181d")
        frame.grid_propagate(False)

        # Labels de Registro
        tk.Label(frame, text="Marca", font=("Arial", 12), bg="#CFD8D1", width=15, height=2).grid(row=0, column=0, padx=15, pady=20)
        tk.Label(frame, text="Modelo", font=("Arial", 12), bg="#CFD8D1", width=15, height=2).grid(row=1, column=0, padx=15, pady=20)
        tk.Label(frame, text="Placa", font=("Arial", 12), bg="#CFD8D1", width=15, height=2).grid(row=2, column=0, padx=15, pady=20)

        self.miMarca = tk.StringVar()
        tk.Entry(frame, textvariable=self.miMarca, width=30, font=("Arial", 14)).grid(row=0, column=1, padx=30, pady=10, columnspan=2)
        
        self.miModelo = tk.StringVar()
        tk.Entry(frame, textvariable=self.miModelo, width=30, font=("Arial", 14)).grid(row=1, column=1, padx=30, pady=10, columnspan=2)

        self.miPlaca = tk.StringVar()
        tk.Entry(frame, textvariable=self.miPlaca, width=30, font=("Arial", 14)).grid(row=2, column=1, padx=30, pady=10, columnspan=2)

        self.tipoVehiculo = ttk.Combobox(frame, state="readonly", values=["Coche", "Microbus", "Furgoneta de carga", "Camion"])
        self.tipoVehiculo.grid(row=0, column=3, padx=15, pady=20, sticky="nsew")
        self.tipoVehiculo.set("Tipo de Vehiculo")
        self.tipoVehiculo.config(width=19, font=("Arial", 10))

        # Boton Guardar
        tk.Button(frame, text="GUARDAR", command=self.agregar_vehiculo, width=30, height=2, border=0, bg="#61876B", font=("Arial", 10, "bold")).grid(row=5, column=2)

        return frame

    def crear_frame_alquilar(self, parent):
        frame = tk.Frame(parent, width=780, height=300, padx=10, bg="#17181d")
        frame.grid_propagate(False)

        tk.Label(frame, text="Digite la placa", font=("Arial", 12), bg="#CFD8D1", width=15, height=2).grid(row=0, column=0, padx=15, pady=20)
        tk.Label(frame, text="Días de alquiler", font=("Arial", 12), bg="#CFD8D1", width=15, height=2).grid(row=1, column=0, padx=15, pady=20)
        
        self.miPlacaAlquilar = tk.StringVar()
        tk.Entry(frame, textvariable=self.miPlacaAlquilar, width=30, font=("Arial", 14)).grid(row=0, column=1, padx=15, pady=10, columnspan=2)

        self.miDiasAlquilar = tk.StringVar()
        tk.Entry(frame, textvariable=self.miDiasAlquilar, width=30, font=("Arial", 14)).grid(row=1, column=1, padx=15, pady=10, columnspan=2)

        # Boton Alquilar
        tk.Button(frame, text="ALQUILAR", command=self.alquilar_vehiculo, width=30, height=2, border=0, bg="#61876B", font=("Arial", 10, "bold")).grid(row=3, column=2)

        self.labelEstadoVehiculo = tk.Label(frame, text="", font=("Arial", 12), bg="#CFD8D1", width=40, height=2)
        self.labelEstadoVehiculo.grid(row=2, column=0, columnspan=3, padx=15, pady=10)

        return frame

    def crear_frame_lista(self, parent):
        frame = tk.Frame(parent, width=780, height=300, padx=10, bg="#17181d")
        frame.grid_propagate(False)

        self.lista_vehiculos = tk.Listbox(frame, width=95, height=13)
        self.lista_vehiculos.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        scrollbar = tk.Scrollbar(frame, command=self.lista_vehiculos.yview)
        scrollbar.grid(row=0, column=4, sticky="nsew")
        self.lista_vehiculos.config(yscrollcommand=scrollbar.set)

        # Botones para actualizar y eliminar
        tk.Button(frame, text="Actualizar Lista", command=self.listar_vehiculos, width=20, height=2, border=0, bg="#61876B", font=("Arial", 10, "bold")).grid(row=1, column=3, padx=10, pady=10)
        tk.Button(frame, text="Eliminar Vehículo", command=self.eliminar_vehiculo, width=20, height=2, border=0, bg="#61876B", font=("Arial", 10, "bold")).grid(row=1, column=2, padx=10, pady=10)

        return frame

    def crear_frame_opciones(self, parent):
        frame = tk.Frame(parent, bg="#1d1f27", width=800, height=60)
        frame.grid_propagate(False)
        frame.grid(row=0, column=0)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_columnconfigure(2, weight=1)
        frame.grid_columnconfigure(3, weight=1)
        frame.grid_rowconfigure(0, weight=1)

        tk.Button(frame, text="Registrar Vehiculo", bd=0, bg="#777d97", pady=5, padx=10, command=lambda: self.mostrar_frame(self.frameRegistro), font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        tk.Button(frame, text="Alquilar Vehiculo", bd=0, bg="#777d97", pady=5, padx=20, command=lambda: self.mostrar_frame(self.frameAlquilar), font=("Arial", 12, "bold")).grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        tk.Button(frame, text="Lista Vehiculos", bd=0, bg="#777d97", pady=5, padx=10, command=lambda: self.mostrar_frame(self.frameLista), font=("Arial", 12, "bold")).grid(row=0, column=2, sticky="nsew", padx=10, pady=10)

        return frame

    def mostrar_frame(self, frame):
        self.frameRegistro.grid_forget()
        self.frameAlquilar.grid_forget()
        self.frameLista.grid_forget()
        frame.grid(row=0, column=0, padx=10, pady=10)

    def listar_vehiculos(self):
        self.lista_vehiculos.delete(0, tk.END)
        for i, vehiculo in enumerate(self.gestor.vehiculos):
            self.lista_vehiculos.insert(tk.END, f"{i+1}. {vehiculo.marca} - {vehiculo.modelo} - {vehiculo.placa} - {vehiculo.tipo} - {vehiculo.estado}")

    def agregar_vehiculo(self):
        try:
            marca = self.miMarca.get()
            modelo = self.miModelo.get()
            placa = self.miPlaca.get()
            tipo = self.tipoVehiculo.get()

            if not marca or not modelo or not placa or not tipo:
                raise ValueError("Todos los campos son obligatorios")

            if tipo == "Coche":
                vehiculo = Coche(marca, modelo, placa, tipo)
            elif tipo == "Microbus":
                vehiculo = Microbus(marca, modelo, placa, tipo)
            elif tipo == "Furgoneta de carga":
                vehiculo = FurgonetaCarga(marca, modelo, placa, tipo)
            elif tipo == "Camion":
                vehiculo = Camion(marca, modelo, placa, tipo)
            else:
                raise ValueError("Tipo de vehículo no válido")

            self.gestor.agregar_vehiculo(vehiculo)
            self.miMarca.set("")
            self.miModelo.set("")
            self.miPlaca.set("")
            self.tipoVehiculo.set("Tipo de Vehiculo")
            messagebox.showinfo("Éxito", "Vehículo agregado correctamente")

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def alquilar_vehiculo(self):
        placa = self.miPlacaAlquilar.get()
        dias = self.miDiasAlquilar.get()

        if not placa or not dias:
            messagebox.showerror("Error", "La placa y los días de alquiler son obligatorios")
            return

        try:
            dias = int(dias)
            costo = self.gestor.alquilar_vehiculo(placa, dias)

            if costo is None:
                messagebox.showerror("Error", "Vehículo no disponible o no encontrado")
            else:
                self.labelEstadoVehiculo.config(text=f"Vehículo {placa} alquilado por {dias} días. Costo: {costo}")
                messagebox.showinfo("Éxito", f"Vehículo alquilado correctamente. Costo: {costo}")
                self.gestor.guardar_datos()  # Asegura que los cambios se guarden
        except ValueError:
            messagebox.showerror("Error", "El número de días debe ser un número entero")


    def eliminar_vehiculo(self):
        seleccion = self.lista_vehiculos.curselection()

        if not seleccion:
            messagebox.showerror("Error", "Selecciona un vehículo para eliminar")
            return

        index = seleccion[0]

        if messagebox.askyesno("Confirmación", f"¿Estás seguro de que deseas eliminar el vehículo seleccionado?"):
            self.gestor.eliminar_vehiculo(index)
            self.listar_vehiculos()  # Actualiza la lista después de eliminar
            messagebox.showinfo("Éxito", "Vehículo eliminado correctamente")


if __name__ == "__main__":
    root = tk.Tk()
    gestor = GestorVehiculos("vehiculos.json")  # Cambia el nombre del archivo JSON si es necesario
    app = GUI(root, gestor)
    root.mainloop()
