import streamlit as st
from typing import List
from .db import get_sheets_client, open_spreadsheet
from models.models import EstimuloSFA


SFA_SHEET_NAME = "adctividad01_sfa"



def get_sfa_sheet():
    """Devuelve la hoja específica de SFA"""
    client = get_sheets_client()
    spreadsheet_key = st.secrets["database"]["spreadsheet_key"]
    spreadsheet = open_spreadsheet(client, spreadsheet_key)

    # Abrir la hoja específica de SFA por su nombre
    return spreadsheet.worksheet(SFA_SHEET_NAME)

def get_all_sfa_estimulos() -> List[EstimuloSFA]:
    """Devuelve todos los estímulos SFA desde la hoja de cálculo"""
    try:
        sheet = get_sfa_sheet()
        filas = sheet.get_all_records()

        lista_estimulos = []
        for fila in filas:
            estimulo = EstimuloSFA(
                id=str(fila["id"]),
                solucion=str(fila["estimulo"]),
                url=str(fila["URL"]),
                categoria=str(fila["categoria"]),
                uso=str(fila["uso"]),
                accion=str(fila["accion"]),
                propiedades=str(fila["propiedades"]),
                localizacion=str(fila["localizacion"]),
                mostrar=str(fila["mostrar"])
            )
            lista_estimulos.append(estimulo)
            
        return lista_estimulos
    except Exception as e:
        st.error(f"Error al obtener los estímulos SFA: {e}")
        return [] # Lista vacía en caso de error
    
    