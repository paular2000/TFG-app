
import datetime
from models.models import Paciente

from git import List, Optional
from .db import get_sheets_client, open_spreadsheet


SPREADSHEET_KEY = "1gaOH07n1PE--QEBBkyahqnAlH5D9r5_uA7pd1UhXJdU"
SHEET_INDEX = 0



def get_pacientes_sheet():
    """Devuelve la hoja de los pacientes"""
    client = get_sheets_client()
    spreadsheet = open_spreadsheet(client, SPREADSHEET_KEY)
    return spreadsheet.get_worksheet(SHEET_INDEX)



def inicializar_pacientes():
    """Inicializa los encabezados de la bd"""
    sheet = get_pacientes_sheet()
    filas = sheet.get_all_values()

    if not filas or all(cell == "" for cell in filas[0]):
        tareas = [f"T{i+1}" for i in range(30)]
        encabezados = ["ID","ID_Logopeda","Fecha_de_Registro","Nombre", "Apellidos", "Email_contacto", "Edad", "Profesión",
        "Estudios", "Habito_lector", "Aficion"] + tareas

        sheet.append_row(encabezados)



def get_all_pacientes() -> List[Paciente]:
    """Devuelve todos los pacientes registrados como objetos Paciente."""
    sheet = get_pacientes_sheet()
    filas = sheet.get_all_records()
    return [
        Paciente(
            id=fila["ID"],
            id_logopeda=fila["ID_Logopeda"],
            fecha_registro=fila["Fecha de Registro"],
            nombre=fila["Nombre"],
            apellidos=fila["Apellidos"],
            edad=fila["Edad"],
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


def insert_paciente(id_logopeda: str, nombre: str, apellidos: str, email: str, edad: str, profesion: str,
                    estudios: str, habito_lector: str, aficiones: List[str]):
    sheet = get_pacientes_sheet()
    filas = sheet.get_all_values()

    

    new_id = f"P0{len(filas)}"  # cuenta también la fila de encabezado

    nuevo_paciente = Paciente(
        id=new_id,
        id_logopeda=id_logopeda,
        fecha_registro=datetime.datetime.now().strftime("%d/%m/%Y"),
        nombre=nombre,
        apellidos=apellidos,   
        email=email,
        edad=edad,
        profesion=profesion,
        estudios=estudios,
        habito_lector=habito_lector,
        aficiones=", ".join(aficiones) if aficiones else ""
    )

    sheet.append_row([
        nuevo_paciente.id,
        nuevo_paciente.id_logopeda,
        nuevo_paciente.fecha_registro,
        nuevo_paciente.nombre,
        nuevo_paciente.apellidos,
        nuevo_paciente.email,
        nuevo_paciente.edad,
        nuevo_paciente.profesion,
        nuevo_paciente.estudios,
        nuevo_paciente.habito_lector,
        nuevo_paciente.aficiones
    ])
    return nuevo_paciente
   

