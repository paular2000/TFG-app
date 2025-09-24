

from typing import Optional, Tuple
from core.models import Logopeda
from core.repositories import ILogopedaRepository
from db import get_sheets_client, open_spreadsheet
from datetime import datetime


class LogopedaRepositorySheets(ILogopedaRepository):

    def __init__(self):
        client = get_sheets_client()
        self.spreadsheet = open_spreadsheet(client, "1gaOH07n1PE--QEBBkyahqnAlH5D9r5_uA7pd1UhXJdU")
        self.sheet = self.spreadsheet.get_worksheet(1)  # segunda pestaña

        if not self.sheet.get_all_values():
            encabezados = ["ID", "Usuario", "Contraseña", "Fecha_registro"]
            self.sheet.append_row(encabezados)


    def registrar_logopeda(self, logopeda: Logopeda) -> str:
        filas = self.sheet.get_all_values()
        nuevo_id = f"L0{len(filas)}"
        fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.sheet.append_row([nuevo_id, logopeda.usuario, logopeda.contrasena, fecha_registro])
        return nuevo_id

    def validar_logopeda(self, usuario: str, contrasenia: str) -> Tuple[bool, Optional[str]]:
        filas = self.sheet.get_all_records()
        for fila in filas:
            if fila["Usuario"] == usuario and fila["Contraseña"] == contrasenia:
                return True, fila["ID"]
        return False, None