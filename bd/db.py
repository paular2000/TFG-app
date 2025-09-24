import gspread # type: ignore
import unicodedata
from google.oauth2.service_account import Credentials # type: ignore
import streamlit as st




SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]



def get_sheets_client():
    """Devuelve el cliente autorizado de Google Sheets"""
    credentials = Credentials.from_service_account_info(
        st.secrets["google_service_account"],
        scopes=SCOPES
    )
    return gspread.authorize(credentials)

def open_spreadsheet(client, key: str):
    """Abre una hoja de cálculo por su clave"""
    return client.open_by_key(key)

def normalize_key(s: str) -> str:
    """Normaliza un string quitando tildes y pasándolo a minúsculas"""
    return ''.join(
        c for c in unicodedata.normalize('NFD', str(s))
        if unicodedata.category(c) != 'Mn'
    ).lower()


