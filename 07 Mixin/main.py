"""genera un objeto y lo exporta como JSON"""

from classes import Manager

manager = Manager("Alice", "CTO")
print(manager.to_json())
