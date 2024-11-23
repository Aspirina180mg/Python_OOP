"""Clase Dog, hijo de Animal
este es un ejemplo de cómo debería quedar el archivo si se separara Animal.py 
en distintos archivos por clase.
"""

from animal import Animal


class Dog(Animal):
    """clase hijo de Animal"""

    def speak(self):
        """Los perros ladran

        Returns:
            string: devuelve el nombre y la acción
        """
        return f"{self.name} dice Guau!"
