""" clase de tipo de ave, puede ser Bird o Penguin"""


class Bird:
    """clase de tipo Ave, puede volar"""

    def fly(self):
        """Método de acción de ave

        Returns:
            string: indica que puede volar
        """
        return "Bird is flying"


class Penguin:
    """clase de tipo Pinguino, puede nadar"""

    def fly(self):
        """Método de acción de pinguino

        Returns:
            string: indica que puede nadar
        """
        return "Penguins can't fly, they swim"


def let_fly(bird):
    """método de dejar volar, indiferente de la clase, ejecuta el método fly()

    Args:
        bird (class): cambiará la acción según la clase del objeto
    """
    print(bird.fly())
