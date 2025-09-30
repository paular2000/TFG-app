

from typing import Optional
from models.models import Paciente
from data_base import paciente_repo



def registrar_paciente(id_logopeda: str, nombre: str, apellidos: str, fecha_nacimiento: str,
                       profesion: str, estudios: str, aficiones: list):
    try:
        paciente_repo.inicializar_pacientes()

        paciente = Paciente(
            id_logopeda=id_logopeda,
            nombre=nombre,
            apellidos=apellidos,
            fecha_nacimiento=fecha_nacimiento,
            profesion=profesion,
            estudios=estudios,
            aficiones=", ".join(aficiones)
        )  

        nuevo_paciente = paciente_repo.insert_paciente(paciente)
        return True, f"✅ Paciente {nuevo_paciente.nombre} registrado con éxito."
    except Exception as e:
        return False, f"❌ Error al registrar paciente: {e}"
    

def obtener_pacientes_por_logopeda(id_logopeda: str):
    """Devuelve la lista de pacientes asignados a un logopeda específico."""

    try:
        pacientes = paciente_repo.get_all_pacientes()
        pacientes_logopeda = [p for p in pacientes if p.id_logopeda == id_logopeda]
        return True, pacientes_logopeda
    except Exception as e:
        return False, f"❌ Error al obtener pacientes: {e}"
    
    
def obtener_paciente_por_id(id_paciente: str) -> Optional[Paciente]:
    """Devuelve un paciente por su ID."""
    try:
        paciente = paciente_repo.find_paciente_by_id(id_paciente)
        if paciente:
            return True, paciente
        else:
            return False, "❌ Paciente no encontrado."
    except Exception as e:
        return False, f"❌ Error al obtener paciente: {e}"
    
    
def actualizar_resultados_tareas(id_paciente: str, resultados: dict):
    """Actualiza los resultados de las tareas para un paciente específico."""
    try:
        sheet = paciente_repo.get_pacientes_sheet()
        filas = sheet.col_values(1)  # columna A tiene los IDs
        if id_paciente not in filas:
            raise ValueError("Paciente no encontrado.") # ID no existe
        
        fila_index = filas.index(id_paciente) + 1  # +1 porque A1-indexed
        columna_inicio = 10  # columna J
        valores = [resultados[f"T{i+1}"] for i in range(len(resultados))]
        columna_fin = columna_inicio + len(valores) - 1

        rango = f"{gspread.utils.rowcol_to_a1(fila_index, columna_inicio)}:{gspread.utils.rowcol_to_a1(fila_index, columna_fin)}"
        sheet.update(rango, [valores])
        return True, "✅ Resultados actualizados con éxito."
    except Exception as e:
        return False, f"❌ Error al actualizar resultados: {e}"