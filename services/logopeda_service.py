
from models.models import Logopeda
from data_base import logopeda_repo

from passlib.context import CryptContext

#Contexto de hasheo de contraseñas
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def registrar_logopeda(usuario: str, contrasenia: str):
    try:
        logopeda_repo.inicializar_logopedas()
        

        existe = logopeda_repo.find_logopeda_by_user(usuario)
        if existe:
            return False, "❌ El usuario ya existe."
        
        # Hashear la contraseña antes de guardarla
        hashed_contrasenia = pwd_context.hash(contrasenia)

        nuevo_logopeda = logopeda_repo.insert_logopeda(usuario, hashed_contrasenia)
        return True, f"✅ Usuario {nuevo_logopeda.usuario} registrado con éxito."
    
    except Exception as e:
        return False, f"❌ Error al registrar: {e}"


def validar_logopeda(usuario: str, contrasenia: str):
    try:
        logopeda_repo.inicializar_logopedas()
        
        logopeda = logopeda_repo.find_logopeda_by_user(usuario)
        
        if not logopeda:
            return False, "❌ Usuario no existe."
        
        hash_guardado = str(logopeda.contrasenia).strip()
        contrasenia_plana = str(contrasenia).strip()

        if pwd_context.verify(contrasenia_plana, hash_guardado):
            return True, logopeda.id

        return False, "❌ Contraseña incorrecta."
    except Exception as e:
        return False, f"❌ Error al validar: {e}"
    

def find_logopeda_by_user(usuario: str):
    try:
        logopeda_repo.inicializar_logopedas()
        logopeda = logopeda_repo.find_logopeda_by_user(usuario)
        return logopeda
    except Exception as e:
        return None