
from git import List, Optional
from .db import get_sheets_client, open_spreadsheet
import streamlit as st

from models.models import Logopeda
from datetime import datetime

SPREADSHEET_KEY = "1gaOH07n1PE--QEBBkyahqnAlH5D9r5_uA7pd1UhXJdU"
SHEET_INDEX = 1


def get_logopedas_sheet():
    client = get_sheets_client()
    spreadsheet = open_spreadsheet(client, SPREADSHEET_KEY)
    return spreadsheet.get_worksheet(SHEET_INDEX)


def inicializar_logopedas():
    filas = get_logopedas_sheet().get_all_values()

    if not filas or all(cell == "" for cell in filas[0]):
        encabezados = ["ID", "Usuario", "Contraseña", "Fecha_registro"]
        get_logopedas_sheet().append_row(encabezados)


def get_all_logopedas() -> List[Logopeda]:
    """Devuelve todos los logopedas registrados como objetos Logopeda."""
    sheet = get_logopedas_sheet()
    filas = sheet.get_all_records()
    return [
        Logopeda(
            id=fila["ID"],
            usuario=fila["Usuario"],
            contrasenia=fila["Contraseña"],
            fecha_registro=fila["Fecha_registro"],
        )
        for fila in filas
    ]


def find_logopeda_by_user(usuario: str) -> Optional[Logopeda]:
    """Busca un logopeda por nombre de usuario."""
    logopedas = get_all_logopedas()
    for l in logopedas:
        if l.usuario == usuario:
            return l
    return None


def insert_logopeda(usuario: str, contrasenia: str):
    sheet = get_logopedas_sheet()
    filas = sheet.get_all_values()
    new_id = f"L0{len(filas)}"  # cuenta también la fila de encabezado

    nuevo_logopeda = Logopeda(
        id=new_id,
        usuario=usuario,
        contrasenia=contrasenia,
        fecha_registro=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

    sheet.append_row([nuevo_logopeda.id, nuevo_logopeda.usuario, nuevo_logopeda.contrasenia, nuevo_logopeda.fecha_registro])
    return nuevo_logopeda