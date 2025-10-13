

import gspread
from typing import Optional
from models.models import Paciente
from data_base import paciente_repo



def registrar_paciente(id_logopeda: str, nombre: str, apellidos: str, email: str, edad: str,
                       profesion: str, estudios: str, habito_lector: str, aficiones: list, diagnostico: str):
    try:

        
        nuevo_paciente = Paciente(
            id="",
            id_logopeda=id_logopeda,
            fecha_registro="",
            nombre=nombre,
            apellidos=apellidos,   
            email=email,
            edad=edad,
            profesion=profesion,
            estudios=estudios,
            habito_lector=habito_lector,
            aficiones=aficiones,
            diagnostico=diagnostico
        )

        nuevo_paciente = paciente_repo.insert_paciente(nuevo_paciente) # Me lo devuelve ya con su id asignado
        
        return True, f"✅ Usuario {nuevo_paciente.nombre} registrado con éxito.", nuevo_paciente
        
    except Exception as e:
        return False, f"❌ Error al registrar paciente: {e}", None
    

def obtener_pacientes_por_logopeda(id_logopeda: str):
    """Devuelve la lista de pacientes asignados a un logopeda específico."""

    try:
        pacientes = paciente_repo.get_all_pacientes()
        pacientes_logopeda = [p for p in pacientes if p.id_logopeda == id_logopeda]
        return pacientes_logopeda
    except Exception as e:
        return []
    
    
    
    
def obtener_paciente_por_id(id_paciente: str):
    """Devuelve un paciente por su ID."""
    
    paciente = paciente_repo.find_paciente_by_id(id_paciente)
    
    return paciente
    
    

    
def obtener_pacientes_por_nombre(id_logopeda: str, nombre_busqueda: str):
    """Devuelve la lista de pacientes cuyo nombre contiene el texto de búsqueda (case insensitive)."""
    try:
        pacientes = obtener_pacientes_por_logopeda(id_logopeda)
        nombre_busqueda = nombre_busqueda.lower()
        pacientes_filtrados = [p for p in pacientes if nombre_busqueda in p.nombre.lower()]
        return pacientes_filtrados
    except Exception as e:
        return []


def actualizar_resultados_tareas(id_paciente: str, resultados: dict):
    """Actualiza los resultados de las tareas para un paciente específico."""
    try:
        sheet = paciente_repo.get_pacientes_sheet()
        
        columna_de_ids = sheet.col_values(1)

        if id_paciente not in columna_de_ids:
            raise ValueError(f"Paciente con ID '{id_paciente}' no encontrado.")

        fila_index = columna_de_ids.index(id_paciente) + 1  

       
        columna_inicio = 13  # Columna M
        valores = [resultados[f"T{i+1}"] for i in range(len(resultados))]
        columna_fin = columna_inicio + len(valores) - 1

        rango = f"{gspread.utils.rowcol_to_a1(fila_index, columna_inicio)}:{gspread.utils.rowcol_to_a1(fila_index, columna_fin)}"
        sheet.update(rango, [valores])
        
        return True, "✅ Resultados actualizados con éxito."
    except Exception as e:
        return False, f"❌ Error al actualizar resultados: {e}"