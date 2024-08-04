# main.py

import tkinter as tk
from gui import GUI
from gestor_vehiculos import GestorVehiculos

if __name__ == "__main__":
    root = tk.Tk()
    gestor = GestorVehiculos("vehiculos.json")
    app = GUI(root, gestor)
    root.mainloop()
