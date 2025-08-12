from datetime import datetime
from google.oauth2.service_account import Credentials
import gspread
import streamlit as st

scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

credentials = Credentials.from_service_account_info(
    st.secrets["google_service_account"],
    scopes=scopes
)

client = gspread.authorize(credentials)
spreadsheet = client.open_by_key("1gaOH07n1PE--QEBBkyahqnAlH5D9r5_uA7pd1UhXJdU")
sheet = spreadsheet.get_worksheet("Base de datos 1.0")


def inicializar_BD():
    contenido = sheet.get_all_values()
    if not contenido or all(cell == "" for cell in contenido[0]):
        tareas = [f"T{i+1}" for i in range(30)]
        encabezados = ["ID","Nombre", "Apellidos", "Edad", "Profesión", "Estudios", "Aficiones"] + tareas
        sheet.append_row(encabezados)

def ingresar_paciente(datos):
    try:
        inicializar_BD()
        filas = sheet.get_all_values()
        id = len(filas)
        id_00 = f"{id:03}"
        sheet.append_row([
            id_00,
            datos["nombre"],
            datos["apellidos"],
            datos["edad"],
            datos["profesion"],
            datos["estudios"],
            ", ".join(datos["aficiones"])
        ])
        return id_00
    except Exception as e:
        st.error(f"❌ Error al guardar los datos: {e}")
        return None

def guardar_resultados_tareas(id_paciente, resultados):
    try:
        inicializar_BD()
        fila_resultados = [id_paciente] + [resultados[f"T{i+1}"] for i in range(30)]
        tarea_sheet.append_row(fila_resultados)
        st.success("✅ Resultados del test guardados con éxito.")
    except Exception as e:
        st.error(f"❌ Error al guardar los resultados: {e}")
