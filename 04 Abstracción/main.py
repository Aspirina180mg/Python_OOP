"""crea un auto y una moto, desde una clase abstracta Vehicle
    """
from vehicle import Car, Motorcicle

auto = Car()
moto = Motorcicle()
print(auto.start_engine())
print(moto.start_engine())
print(moto.stop_engine())