


from models.models import Logopeda
from data_base import logopeda_repo



def registrar_logopeda(usuario: str, contrasenia: str):
    try:
        logopeda_repo.inicializar_logopedas()
        

        existe = logopeda_repo.find_logopeda_by_user(usuario)
        if existe:
            return False, "❌ El usuario ya existe."
        
        nuevo_logopeda = logopeda_repo.insert_logopeda(usuario, contrasenia)
        return True, f"✅ Usuario {nuevo_logopeda.usuario} registrado con éxito."
    except Exception as e:
        return False, f"❌ Error al registrar: {e}"


def validar_logopeda(usuario: str, contrasenia: str):
    try:
        logopeda_repo.inicializar_logopedas()
        
        logopeda = logopeda_repo.find_logopeda_by_user(usuario)
        if logopeda and logopeda.contrasenia.strip() == contrasenia.strip():
            return True, logopeda.id
        return False, "❌ Usuario o contraseña incorrectos."
    except Exception as e:
        return False, f"❌ Error al validar: {e}"