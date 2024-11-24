"""módulo de exportación a JSON"""

import json


class JSONSerializableMixin:
    """Módulo que exporta el diccionario de un objeto como JSON"""

    def to_json(self):
        """Exporta el diccionario del objeto como JSON

        Returns:
            JSON: _description_
        """
        return json.dumps(self.__dict__)
