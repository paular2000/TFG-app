from ..models import Logopeda
from repositories import ILogopedaRepository
from typing import Tuple, Optional

class LogopedaService:
    

    def __init__(self, repo: ILogopedaRepository):
        self.repo = repo


    def registrar_logopeda(self, usuario: str, contrasena: str) -> Tuple[bool, str]:
        
        logopeda = Logopeda(usuario=usuario, contrasena=contrasena)
        try:
            # Aquí el repositorio devuelve el ID generado
            id_logopeda = self.repo.registrar_logopeda(logopeda)
            return True, id_logopeda
        except Exception as e:
            return False, f"❌ Error al registrar logopeda: {e}"
        


    def validar_logopeda(self, usuario: str, contrasena: str) -> Tuple[bool, Optional[str]]:
        
        try:
            ok, id_logopeda = self.repo.validar_logopeda(usuario, contrasena)
            return ok, id_logopeda
        except Exception as e:
            return False, None
