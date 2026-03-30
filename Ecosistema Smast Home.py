"""
EJERCICIO 2: ECOSISTEMA SMART HOME 🏠🔌
Enunciado: Diseñen la arquitectura de una app para domótica. Lleven el conteo global de dispositivos,
restrinjan acciones si no hay internet y aseguren métodos únicos de activación.
"""

from abc import ABC, abstractmethod

def verificar_conexion(func):

    def envoltura(self, *args, **kwargs):

        if not self.conectado:

            print(f"Error el dispositivo {self.nombre} esta offline")

            return None
        
        return func(self, *args, **kwargs)
    
    return envoltura

class DispositivoInteligente(ABC):

    _total_dispositivos = 0

    def __init__(self, nombre):

        self.nombre = nombre
        self.conectado = True
        DispositivoInteligente._sumar_dispositivo()

    @classmethod

    def _sumar_dispositivo(cls):

        cls._total_dispositivos += 1

    @classmethod

    def obtener_conteo_global(cls):

        return f"dispositivos totales en la casa: {cls._total_dispositivos}"

    @abstractmethod
    def activar_funcion_principal(self):
        pass

class Termostato(DispositivoInteligente):

    def __init__(self, nombre):

        super().__init__(nombre)
        self._temperatura_objetivo = 22

    @property

    def temperatura_objetivo(self):

        return self._temperatura_objetivo

    @temperatura_objetivo.setter

    def temperatura_objetivo(self, valor):

        if 10 <= valor <= 30:

            self._temperatura_objetivo = valor
            print(f"🌡️ {self.nombre}: Temperatura ajustada a {valor}°C.")

        else:

            print(f"Error la temperatura {valor}C° está fuera de rango (10-30 C°).")

    @verificar_conexion

    def activar_funcion_principal(self):
        print(f"POLIMORFISMO Regulando clima a {self._temperatura_objetivo}C°")

class CamaraSeguridad(DispositivoInteligente):

    @verificar_conexion
    def activar_funcion_principal(self):
        print(f"POLIMORFISMO Iniciando streaming de video HD en {self.nombre}.")