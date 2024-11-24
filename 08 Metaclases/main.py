"""ejemplo de creación de metaclase"""

class MyMeta(type):
    """metaclase, preefine clases para uso futuro"""

    def __new__(mcs, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(mcs, name, bases, dct)


class MyClass(metaclass=MyMeta):
    """se crea la clase MyClass con las propiedades de MyMeta"""


obj = MyClass()
