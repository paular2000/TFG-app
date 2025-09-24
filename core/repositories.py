
from core.models import Logopeda, Paciente
from typing import Optional, Tuple



#public interface LogopedaRepository {
#    Tuple<Boolean, String> registrarLogopeda(String usuario, String contrasenia);
#}


#actuara como interface
class ILogopedaRepository:

    def registrarLogopeda(self, logopeda:Logopeda) ->str:
        raise NotImplementedError
    
    def validarLogopeda(self, usuario:str, contrasenia:str) -> Tuple[bool,Optional[str]]:
        raise NotImplementedError


 
class IPacienteRepository:

    def registrarPaciente(self, paciente: Paciente) -> str:
        raise NotImplementedError
    
    def obtenerPacientePorLogopeda(self, id_logopeda:str) -> str:
        raise NotImplementedError
    
    def ObtenerPacientePorID(self, id_padiente:str) -> str:
        raise NotImplementedError


