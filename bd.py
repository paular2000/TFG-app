from datetime import datetime
from google.oauth2.service_account import Credentials
import gspread
import streamlit as st

scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

credentials = Credentials.from_service_account_info(
    st.secrets["google_service_account"],
    scopes=scopes
)
global sheet
client = gspread.authorize(credentials)
spreadsheet = client.open_by_key("1gaOH07n1PE--QEBBkyahqnAlH5D9r5_uA7pd1UhXJdU")
sheet = spreadsheet.get_worksheet(0)

#sheet logopedas
sheet_logopedas = client.open_by_key("1gaOH07n1PE--QEBBkyahqnAlH5D9r5_uA7pd1UhXJdU").get_worksheet(1)

#prueba
sheet_prueba = spreadsheet.get_worksheet(2)


# ==============================
#  Registro de logopedas
# ==============================

def inicializar_logopedas():
    contenido = sheet_logopedas.get_all_values()

    if not contenido or all(cell == "" for cell in contenido[0]):
        encabezados = ["ID", "Usuario", "Contraseña", "Fecha_registro","Prueba"]
        sheet_logopedas.append_row(encabezados)


def inicializar_prueba():
    contenido = sheet_prueba.get_all_values()

    if not contenido or all(cell == "" for cell in contenido[0]):
        encabezados = ["Prueba"]
        sheet_prueba.append_row(encabezados)


def registrar_logopeda(usuario, contrasena):
    try:
        inicializar_logopedas()

        inicializar_prueba()

        # comprobar si usuario ya existe
        usuarios = sheet_logopedas.col_values(2)  # columna B
        if usuario in usuarios:
            return False, "❌ El usuario ya existe."

        filas = sheet_logopedas.get_all_values()
        id = len(filas)  # cuenta también la fila de encabezado
        id_00 = f"L0{id}"


        sheet_logopedas.append_row([
            id_00,
            usuario,
            contrasena,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "prueba"
            
        ])

        return True, f"✅ Usuario {usuario} registrado con éxito."
    except Exception as e:
        return False, f"❌ Error al registrar: {e}"

def validar_logopeda(usuario, contrasena):
    try:
        inicializar_logopedas()
        filas = sheet_logopedas.get_all_records()  # devuelve lista de dicts
        for fila in filas:
            if fila["Usuario"] == usuario and fila["Contraseña"] == contrasena:
                return True, fila["ID"]
        return False, "❌ Usuario o contraseña incorrectos."
    except Exception as e:
        return False, f"❌ Error al validar: {e}"




# ==============================
#  Registro de pacientes
# ==============================


def inicializar_BD():
    contenido = sheet.get_all_values()

    tareas = [f"T{i+1}" for i in range(30)]
    encabezados = [
        "ID", "ID_Logopeda", "Nombre", "Apellidos", "Edad", "Profesión",
        "Estudios", "Aficion"
        ] + tareas
    
    if not contenido or all(cell == "" for cell in contenido[0]):
        sheet.append_row(encabezados)
 

def ingresar_paciente(datos):
    try:
        inicializar_BD()
        filas = sheet.get_all_values()
        id = len(filas)
        id_00 = f"{id:03}"
        
        #recupero el id del logopeda
        id_logopeda = st.session_state.get("id_logopeda",None)
        if not id_logopeda:
            st.error("No se encuentra al logopeda")
            return None

        sheet.append_row([
            id_00,
            datos["nombre"],
            datos["apellidos"],
            datos["edad"],
            datos["profesion"],
            datos["estudios"],
            ", ".join(datos["aficion"]),
            id_logopeda
        ])
        st.success("✅ Datos del paciente guardados con éxito.")
        return id_00
    except Exception as e:
        st.error(f"❌ Error al guardar los datos: {e}")
        return None

def guardar_resultados_tareas(id_paciente, resultados):
    try:
        inicializar_BD()

        lista_ids = sheet.col_values(1)  # columna A

        if id_paciente not in lista_ids:
            st.error("❌ Paciente no encontrado en la hoja.")
            return
        
        fila = lista_ids.index(id_paciente) + 1  

        columna_inicio = 9  # columna J
        valores = [resultados[f"T{i+1}"] for i in range(len(resultados))]
        columna_fin = columna_inicio + len(valores) - 1

        
        rango = f"{gspread.utils.rowcol_to_a1(fila, columna_inicio)}:{gspread.utils.rowcol_to_a1(fila, columna_fin)}"

        sheet.update(rango, [valores])

        st.success("✅ Resultados del test guardados con éxito.")
    except Exception as e:
        st.error(f"❌ Error al guardar los resultados: {e}")

