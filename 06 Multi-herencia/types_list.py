"""define clases según tipo, en este caso, volaor y nadador

Returns:
    string: cada tipo tiene una acción que devuelve un texto inicativo
    """


class Flyer:
    """tipo volador, tiene la habilidad de volar"""

    def fly(self):
        """Acción de tipo volador"""
        return "the animal is now flying"


class Swimmer:
    """tipo nadador, tiene la habilidad de nadar"""

    def swim(self):
        """Acción de tipo nadador"""
        return "the animal is now swimming"


class Duck(Flyer, Swimmer):
    """objeto de tipo pato, con cualidades de volador y nadador

    Args:
        Flyer (class): otorga habilidad de volar
        Swimmer (class): otorga habilidad de nadar"""
