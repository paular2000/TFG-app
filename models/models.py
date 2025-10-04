


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
    fecha_registro: str
    nombre: str
    apellidos: str
    email: str
    edad: int
    profesion: str
    estudios: str
    habito_lector: str
    aficiones: List[str]
    