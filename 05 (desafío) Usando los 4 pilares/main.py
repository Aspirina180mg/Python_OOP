"""
Desafío: Sistema de Gestión de Vehículos

Contexto:
Vas a crear un sistema para gestionar diferentes tipos de vehículos en una 
flota. 
Cada tipo de vehículo tiene características y comportamientos únicos, pero 
también comparten algunas funcionalidades básicas.
"""

from vehiculos import Auto, Moto, AutoElectrico

print("iniciando auto\n")
camioneta = Auto(marca="Chevrolet", modelo="Captiva", anio=2007, combustible=50)
camioneta.informar_estado()
camioneta.cargar_combustible(100)
camioneta.obtener_nivel_combustible()
camioneta.arrancar()

print("\niniciando moto\n")
moto = Moto("Harley Davidson", "akashika", 2020, 10, "encendido")
moto.informar_estado()
moto.wheelie()
moto.detener()
moto.wheelie()

print("\niniciando auto electrico\n")
Auto = AutoElectrico("Tesla", "Model 3", 2023, bateria=50)
Auto.informar_estado()
Auto.cargar_combustible(100)
Auto.obtener_nivel_combustible()
Auto.cargar_bateria(25)
Auto.obtener_nivel_bateria()
Auto.arrancar()
