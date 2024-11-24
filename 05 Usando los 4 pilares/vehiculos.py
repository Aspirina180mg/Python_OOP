"""módulo de clases, se utiliza Auto, Moto y Auto_Electrico"""

from abc import ABC, abstractmethod


class Vehiculo(ABC):
    """Clase abstracta, se definen algunas funciones básicas y la estructura"""

    def __init__(self, marca, modelo, anio, combustible, estado_motor):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self._combustible = combustible
        self._estado_motor = estado_motor

    def arrancar(self):
        """enciende el motor del vehículo"""
        self._estado_motor = "encendido"
        print("se ha encendido el motor")

    def detener(self):
        """detiene el motor del vehículo"""
        self._estado_motor = "apagado"
        print("se ha apagado el motor")

    @abstractmethod
    def informar_estado(self):
        """informa el estado general, como tambien muestra características"""

    def cargar_combustible(self, cantidad_cargada):
        """aumenta la cantidad de combustible en el estanque

        Args:
            cantidad_cargada (int): cantidad de combustible a cargar
        """
        self._combustible += cantidad_cargada
        print(f"se ha cargado {cantidad_cargada} litros de combustible")

    def obtener_nivel_combustible(self):
        """entrega el nivel de combustible restante en el vehículo"""
        print(f"al vehículo le quedan {self._combustible} litros de combustible")


class Auto(Vehiculo):
    """clase general para Autos, tiene un atributo de aire acondicionado"""

    def __init__(
        self,
        marca,
        modelo,
        anio,
        combustible=0,
        estado_motor="apagado",
        aire_acondicionado="apagado",
    ):
        super().__init__(marca, modelo, anio, combustible, estado_motor)
        self._aire_acondicionado = aire_acondicionado

    def informar_estado(self):
        print(
            f"el auto {self.marca} {self.modelo} del año {self.anio} tiene el "
            f"motor {self._estado_motor} y el aire acondicionado "
            f"{self._aire_acondicionado}"
        )


class Moto(Vehiculo):
    """clase general de motos, tiene un método de hacer wheelie (1 rueda)"""

    def __init__(
        self,
        marca,
        modelo,
        anio,
        combustible=0,
        estado_motor="apagado",
    ):
        super().__init__(marca, modelo, anio, combustible, estado_motor)

    def informar_estado(self):
        if self._estado_motor == "encendido":
            print(
                f"la moto {self.marca} {self.modelo} del año {self.anio} "
                f"tiene el motor {self._estado_motor} y está lista para hacer "
                f"un wheelie"
            )
        else:
            print(
                f"la moto {self.marca} {self.modelo} del año {self.anio} tiene"
                f" el motor {self._estado_motor} y no puede hacer un wheelie"
            )

    def wheelie(self):
        """método para hacer un wheelie, solo si el motor está encendido"""
        if self._estado_motor == "encendido":
            print("Haciendo un wheelie.")
        else:
            print("No se puede hacer wheelie, motor apagado.")


class AutoElectrico(Vehiculo):
    """clase especial, no usa combustible y tiene métodos para batería"""

    def __init__(
        self,
        marca,
        modelo,
        anio,
        bateria=0,
        estado_motor="apagado",
        aire_acondicionado="apagado",
    ):
        super().__init__(
            marca, modelo, anio, combustible=bateria, estado_motor=estado_motor
        )
        self._bateria = bateria
        self._aire_acondicionado = aire_acondicionado

    def informar_estado(self):
        print(
            f"el auto {self.marca} {self.modelo} del año {self.anio} tiene el "
            f"motor {self._estado_motor} y el aire acondicionado "
            f"{self._aire_acondicionado}"
        )

    def cargar_combustible(self, cantidad_cargada):
        print("este es un auto electrico, no se puede cargar combustible")

    def obtener_nivel_combustible(self):
        print("este es un auto electrico, no tiene estanque de combustible")

    def cargar_bateria(self, cantidad_cargada):
        """carga batería en lugar de combustible, llega hasta 100%"""
        self._bateria += cantidad_cargada
        print(f"se ha cargado {cantidad_cargada}% de bateria")

    def obtener_nivel_bateria(self):
        """muestra el porcentaje de batería restante"""
        print(f"al vehículo le quedan {self._bateria}% de batería")
