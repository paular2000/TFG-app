from core.models import Paciente

from repositories import IPacienteRepository
from typing import List, Optional

class PacienteService:
    

    def __init__(self, repo: IPacienteRepository):
        self.repo = repo


    def registrar_paciente(self, paciente: Paciente) -> Optional[str]:
        
        try:
            return self.repo.registrar_paciente(paciente)
        except Exception as e:
            print(f"❌ Error al registrar paciente: {e}")
            return None

    def listar_pacientes(self, id_logopeda: str) -> List[Paciente]:
        
        try:
            return self.repo.obtener_pacientes_por_logopeda(id_logopeda)
        except Exception as e:
            print(f"❌ Error al listar pacientes: {e}")
            return []



    def obtener_paciente_por_id(self, id_paciente: str) -> Optional[Paciente]:
        
        try:
            return self.repo.obtener_paciente_por_id(id_paciente)
        except Exception as e:
            print(f"❌ Error al obtener paciente por ID: {e}")
            return None
