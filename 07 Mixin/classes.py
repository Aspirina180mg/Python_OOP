"""implementción de clases Employee y Manager"""

from mixin import JSONSerializableMixin


class Employee:
    """clase de empleado, tiene nombre y posición"""

    def __init__(self, name, position):
        self.name = name
        self.position = position


class Manager(Employee, JSONSerializableMixin):
    """Manager hereda desde EMployee y el Mixin

    Args:
        Employee (class): atributos de nombre y posición
        JSONSerializableMixin (class): mixin para exportar a JSON
    """
