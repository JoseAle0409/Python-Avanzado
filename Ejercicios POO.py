"""
ejercio 1: Gestión de Inventario Tecnológico
Enunciado: Crear un sistema básico para llevar el registro de dispositivos en un almacén tecnológico.
 El sistema debe distinguir entre un dispositivo genérico y un teléfono inteligente.
"""

class Dispositivo:

    cantidad_total_registra = 0

    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo
        self.encendido = False

        Dispositivo.cantidad_total_registrada += 1

    def cambiar_estado(self):

        if self.encendido:
            self.encendido = False
        else:
            self.encendido = True

class Telefono(Dispositivo):

    def __init__(self, marca, modelo):

        super().__init__(marca, modelo)
        self.aplicaciones = []

    def instalar_app(self, nombre_app):
        self.aplicaciones.append(nombre_app)

        print(f"instalada: {nombre_app} en {self.modelo}")

def mostrar_telefonos_ensendidos(lista_telefonos):

    print("\ntelefono ensendido.\n")

    for t in lista_telefonos:

        if t.encendido:

            print(f"Marca: {t.marca}/ Modelo: {t.modelo}")

telefono1 = Telefono("Samsung", "S23")
telefono2 = Telefono("Apple", "iPhone 15")
laptop = Dispositivo("Lenobo", "XPS 13")

telefono1.cambiar_estado()
telefono1.instalar_app("Discord")


telefonos = [telefono1, telefono2]

mostrar_telefonos_ensendidos(telefonos)

print(f"\ntotal de dispositivos en inventario: {Dispositivo.cantidad_total_registrada}")


""" 
ejercicio 2: sistema de Puntuación de Videojuego
Enunciado: Desarrollar la lógica base para personajes de un videojuego, con jugadores normales y VIP.
"""

class Jugador:

    puntuacion_base = 100

    def __init__(self, nombre_usuario, puntos_actuales):

        self.nombre_usuario = nombre_usuario
        self.puntos_actuales = puntos_actuales
    
    def ganar_puntos(self, cantidad):

        self.puntos_actuales += cantidad

class JugadorVIP(Jugador):

    def __init__(self, nombre_usuario, multiplicador):

        super().__init__(nombre_usuario)
        self.multiplicador = multiplicador

    def ganar_puntos_vip(self, cantidad):
        
        puntos_bono = cantidad * self.multiplicador
        self.puntos_actuales += puntos_bono

def filtrar_mejores_jugadores(lista_jugadores, puntaje_minimo):

    mejores = []
    for j in lista_jugadores:

        if j.puntos_actuales >= puntaje_minimo:

            mejores.append(j.nombre_usuario)
    return mejores

j1 = Jugador("Vandal")
j2 = JugadorVIP("adersgamer09", multiplicador=3)
j3 = Jugador("OverLord67")

j1.ganar_puntos(50)
j2.ganar_puntos_vip(50)
j3.ganar_puntos(10)

ranking = [j1, j2, j3]

top = filtrar_mejores_jugadores(ranking, 150)

print(f"\nJugadores que superan el puntaje minimo: {top}")

"""
ejercicio 3: simulador de Flota de Vehículos
Enunciado: Simular el consumo de combustible de una flota de reparto (vehículos estándar y camiones).
"""

class Vehiculo:

    costo_por_litro = 1.5

    def __init__(self, matricula, combustible_litros):

        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.en_ruta = True

    def viajar(self, kilometros):

        if not self.en_ruta:

            print(f"El vehiculo {self.matricula} no puede viajar, esta fuera de ruta.\n")
            return

        consumo = kilometros / 10
        if self.combustible_litros >= consumo:
            
            self.combustible_litros -= consumo
            print(f"{self.matricula} condujo {kilometros}km. Quedan {self.combustible_litros}L.\n")

        else:

            self.combustible_litros = 0
            self.en_ruta = False

            print(f"{self.matricula} se quedo sin gasolina a mitad del camino.\n")

class Camion(Vehiculo):

    def __init__(self, matricula, combustible_litros, cargas):

        super().__init__(matricula, combustible_litros)
        self.cargas_entregadas = cargas

    def entregar_carga(self):

        if self.cargas_entregadas:

            carga = self.cargas_entregadas.pop()

            print(f"Carga entregada: {carga} por el camion {self.matricula}.\n")

        else:
            print(f"El camion {self.matricula} ya no tiene cargas pendientes.\n")

def simular_jornada(lista_vehiculos, distancias_a_recorrer):

    for vehiculo, distancia in zip(lista_vehiculos, distancias_a_recorrer):

        vehiculo.viajar(distancia)
        if isinstance(vehiculo, Camion) and vehiculo.en_ruta:

            vehiculo.entregar_carga()

vehiculo1 = Vehiculo("VGT-777", 20)
camion1 = Camion("Truck-67", 50, ["alimentos", "electronicos", "muebles"])

flota = [vehiculo1, camion1]
rutas = [150, 100]

simular_jornada(flota, rutas)

print(f"Estado {vehiculo1.matricula}: {vehiculo1.combustible_litros}L/ En ruta: {vehiculo1.en_ruta}.\n")
print(f"Estado {camion1.matricula}: {camion1.combustible_litros}L/ Cargas restantes: {len(camion1.cargas_entregadas)}")