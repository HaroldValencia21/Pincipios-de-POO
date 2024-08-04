# gestor_vehiculos.py

import json
import os
from vehiculo import Coche, Microbus, FurgonetaCarga, Camion

class GestorVehiculos:
    def __init__(self, archivo):
        self.archivo = archivo
        self.vehiculos = self.cargar_datos()

    def cargar_datos(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, 'r') as file:
                data = json.load(file)
                vehiculos = []
                for item in data:
                    vehiculo = self.crear_vehiculo(item)
                    if vehiculo:
                        vehiculos.append(vehiculo)
                return vehiculos
        return []

    def guardar_datos(self):
        data = [self.serializar_vehiculo(v) for v in self.vehiculos]
        with open(self.archivo, 'w') as file:
            json.dump(data, file, indent=4)

    def crear_vehiculo(self, item):
        tipo = item["tipo"]
        if tipo == "Coche":
            return Coche(item["marca"], item["modelo"], item["placa"], item["tipo"])
        elif tipo == "Microbus":
            return Microbus(item["marca"], item["modelo"], item["placa"], item["tipo"])
        elif tipo == "Furgoneta de carga":
            return FurgonetaCarga(item["marca"], item["modelo"], item["placa"], item["tipo"])
        elif tipo == "Camion":
            return Camion(item["marca"], item["modelo"], item["placa"], item["tipo"])
        return None

    def serializar_vehiculo(self, vehiculo):
        return {
            "marca": vehiculo.marca,
            "modelo": vehiculo.modelo,
            "placa": vehiculo.placa,
            "tipo": vehiculo.tipo,
            "estado": vehiculo.estado
        }

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        self.guardar_datos()

    def eliminar_vehiculo(self, index):
        if 0 <= index < len(self.vehiculos):
            del self.vehiculos[index]
            self.guardar_datos()

    def alquilar_vehiculo(self, placa, dias):
        vehiculo = next((v for v in self.vehiculos if v.placa == placa), None)
        if vehiculo:
            if vehiculo.estado == "Disponible":
                vehiculo.estado = "Alquilado"
                return vehiculo.calcular_precio(dias)
        return None
