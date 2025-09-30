


from dataclasses import dataclass
from typing import List

@dataclass
class Logopeda:
    id: str
    usuario: str
    contrasenia: str
    fecha_registro: str

class Paciente:
    def __init__(self, id, id_logopeda, nombre, apellidos, fecha_nacimiento,
                 profesion, estudios, aficiones, fecha_registro=None, edad=None):
        self.id = id
        self.id_logopeda = id_logopeda
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.profesion = profesion
        self.estudios = estudios
        self.aficiones = aficiones
        self.fecha_registro = fecha_registro
        self.edad = edad
