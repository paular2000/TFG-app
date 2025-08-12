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
        st.success("✅ Resultados del test guardados con éxito.")
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

        columna_inicio = 8  # columna H 
        valores = [resultados[f"T{i+1}"] for i in range(len(resultados))]
        columna_fin = columna_inicio + len(valores) - 1

        
        rango = f"{gspread.utils.rowcol_to_a1(fila, columna_inicio)}:{gspread.utils.rowcol_to_a1(fila, columna_fin)}"

        sheet.update(rango, [valores])

        st.success("✅ Resultados del test guardados con éxito.")
    except Exception as e:
        st.error(f"❌ Error al guardar los resultados: {e}")

