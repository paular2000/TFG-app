


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
    diagnostico: str

@dataclass
class EstimuloSFA:
    id: str
    solucion: str # la respuesta correcta (columna estimulo)
    url: str
    categoria: str
    uso: str
    accion: str
    propiedades: str
    localizacion: str
    mostrar: str


    