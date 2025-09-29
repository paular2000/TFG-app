


from dataclasses import dataclass
from typing import List

@dataclass
class Logopeda:
    id: str
    usuario: str
    contrasenia: str
    fecha_registro: str

@dataclass
class Paciente:
    id: str
    id_logopeda: str
    nombre: str
    apellidos: str
    edad: int
    profesion: str
    estudios: str
    aficiones: List[str]