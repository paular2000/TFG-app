
import datetime
from models.models import Paciente

from git import List, Optional
from .db import get_sheets_client, open_spreadsheet


SPREADSHEET_KEY = "1gaOH07n1PE--QEBBkyahqnAlH5D9r5_uA7pd1UhXJdU"
SHEET_INDEX = 0



def get_pacientes_sheet():
    client = get_sheets_client()
    spreadsheet = open_spreadsheet(client, SPREADSHEET_KEY)
    return spreadsheet.get_worksheet(SHEET_INDEX)


def inicializar_pacientes():
    
    tareas = [f"T{i+1}" for i in range(30)]
    encabezados = ["ID","ID_Logopeda","Fecha de Registro","Nombre", "Apellidos", "Edad", "Profesión",
    "Estudios", "Aficion"] + tareas

    get_pacientes_sheet().append_row(encabezados)


def get_all_pacientes() -> List[Paciente]:
    """Devuelve todos los pacientes registrados como objetos Paciente."""
    sheet = get_pacientes_sheet()
    filas = sheet.get_all_records()
    return [
        Paciente(
            id=fila["ID"],
            id_logopeda=fila["ID_Logopeda"],
            fecha_registtro=fila["Fecha de Registro"],
            nombre=fila["Nombre"],
            apellidos=fila["Apellidos"],
            edad=fila["edad"],
            profesion=fila["Profesión"],
            estudios=fila["Estudios"],  
            aficiones=fila["Aficion"].split(", ") if fila["Aficion"] else []
        )
        for fila in filas
    ]



def find_paciente_by_id(paciente_id: str) -> Optional[Paciente]:
    """Busca un paciente por ID del logopeda asignado."""
    pacientes = get_all_pacientes()
    for p in pacientes:
        if p.id == paciente_id:
            return p
    return None


def insert_paciente(paciente: Paciente):
    sheet = get_pacientes_sheet()
    filas = sheet.get_all_values()

    if not filas or all(cell == "" for cell in filas[0]):
        inicializar_pacientes()
        filas = sheet.get_all_values()
    
    
    new_id = f"P0{len(filas)}"  # cuenta también la fila de encabezado

    

    nuevo_paciente = Paciente(
        id=new_id,
        id_logopeda=paciente.id_logopeda,
        fecha_registro=datetime.now().strftime("%d/%m/%Y"),
        nombre=paciente.nombre,
        apellidos=paciente.apellidos,
        edad=paciente.edad,
        profesion=paciente.profesion,
        estudios=paciente.estudios,
        aficiones=paciente.aficiones
    )

    sheet.append_row([
        nuevo_paciente.id,
        nuevo_paciente.id_logopeda,
        nuevo_paciente.fecha_registro,
        nuevo_paciente.nombre,
        nuevo_paciente.apellidos,
        nuevo_paciente.edad if nuevo_paciente.edad else "",
        nuevo_paciente.profesion,
        nuevo_paciente.estudios,
        nuevo_paciente.aficiones
    ])
    return nuevo_paciente

