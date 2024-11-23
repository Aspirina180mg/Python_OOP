"""clase abstracta Vehicle, puede iniciar o apagar motor"""

from abc import ABC, abstractmethod


class Vehicle(ABC):
    """clase padre, abstracta"""

    @abstractmethod
    def start_engine(self):
        """método de iniciar motor"""
        # pass

    @abstractmethod
    def stop_engine(self):
        """método de apagar motor"""
        # pass


class Car(Vehicle):
    """objeto auto"""
    def start_engine(self):
        return "Car engine started"

    def stop_engine(self):
        return "Car engine stopped"


class Motorcicle(Vehicle):
    """objeto moto"""
    def start_engine(self):
        return "Motorcicle engine started"

    def stop_engine(self):
        return "Motorcicle engine stopped"
