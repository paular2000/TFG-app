from typing import List, Optional
from core.models import Paciente
from core.repositories import IPacienteRepository
from db import get_sheets_client, open_spreadsheet



class PacienteRepositorySheets(IPacienteRepository):

    def __init__(self, spreadsheet_key: str):
        self.client = get_sheets_client()
        self.spreadsheet = open_spreadsheet(self.client, spreadsheet_key)
        self.sheet = self.spreadsheet.get_worksheet(0)  # pestaña de pacientes

        # Inicializar encabezados si no existen
        if not self.sheet.get_all_values():
            tareas = [f"T{i+1}" for i in range(30)]
            encabezados = ["ID", "ID_Logopeda", "Nombre", "Apellidos", "Edad", "Profesión", "Estudios", "Aficion"] + tareas
            self.sheet.append_row(encabezados)


    def registrar_paciente(self, paciente: Paciente) -> str:
        filas = self.sheet.get_all_values()
        nuevo_id = f"{len(filas):03}"  # ID secuencial
        aficiones_str = ", ".join(paciente.aficion) if paciente.aficion else ""
        fila = [
            nuevo_id,
            paciente.id_logopeda,
            paciente.nombre,
            paciente.apellidos,
            paciente.edad,
            paciente.profesion,
            paciente.estudios,
            aficiones_str
        ]
        # rellenar tareas vacías
        fila += [""] * 30
        self.sheet.append_row(fila)
        return nuevo_id

    def obtener_pacientes_por_logopeda(self, id_logopeda: str) -> List[Paciente]:
        filas = self.sheet.get_all_records()
        pacientes = []
        for fila in filas:
            if str(fila.get("ID_Logopeda", "")) == str(id_logopeda):
                paciente = Paciente(
                    id=fila["ID"],
                    id_logopeda=fila["ID_Logopeda"],
                    nombre=fila["Nombre"],
                    apellidos=fila["Apellidos"],
                    edad=fila["Edad"],
                    profesion=fila["Profesión"],
                    estudios=fila["Estudios"],
                    aficion=fila["Aficion"].split(", ") if fila["Aficion"] else [],
                    resultados={}  # inicializamos vacío, resultados se guardan aparte
                )
                pacientes.append(paciente)
        return pacientes

    def obtener_paciente_por_id(self, id_paciente: str) -> Optional[Paciente]:
        filas = self.sheet.get_all_records()
        for fila in filas:
            if str(fila.get("ID", "")) == str(id_paciente):
                return Paciente(
                    id=fila["ID"],
                    id_logopeda=fila["ID_Logopeda"],
                    nombre=fila["Nombre"],
                    apellidos=fila["Apellidos"],
                    edad=fila["Edad"],
                    profesion=fila["Profesión"],
                    estudios=fila["Estudios"],
                    aficion=fila["Aficion"].split(", ") if fila["Aficion"] else [],
                    resultados={}
                )
        return None
