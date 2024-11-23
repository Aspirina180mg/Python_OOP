"""implementación de la clase Animal, además de sus subclases Dog y Cat
que heredan atributos y métodos desde la clase padre."""


class Animal:
    """Clase padre"""

    def __init__(self, name):
        """inicialización

        Args:
            name (string): nombre del A
        nimal"""
        self.name = name

    def speak(self):
        """Acción de habla del A
        nimal, cambia según tipo

            Raises:
                NotImplementedError: cada hijo debe implementar speak()
        """
        raise NotImplementedError("subclase debe implementar este método")


# subclases, se pueden separar en archivos distintos, si se importa "Dog" por
# ejemplo, el archivo de Dog debe importar a# nimal, quedando de la manera:
# from animal import animal
# ---código de clase Dog---
# para importar Dog, se usa:
# from Dog import Dog
# implícitamente se importaría animal, porque Dog ya lo hace.


class Dog(Animal):
    """clase hijo de animal"""

    def speak(self):
        """Los perros ladran

        Returns:
            string: devuelve el nombre y la acción
        """
        return f"{self.name} dice Guau!"


class Cat(Animal):
    """clase hijo de animal"""

    def speak(self):
        """Los gatos Maullan

        Returns:
            string: devuelve el nombre y la acción
        """
        return f"{self.name} dice Miau!"
