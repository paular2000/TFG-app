
from datetime import datetime
import streamlit as st

def pantalla_formulario_paciente():
    
    with st.form("formulario_paciente"):
        
        nombre = st.text_input("", placeholder="Nombre", help="Introduce el nombre del paciente")
        apellidos = st.text_input("", placeholder="Apellidos", help="Introduce los apellidos del paciente")

        dias = list(range(1, 32))
        meses = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]
        anios = list(range(datetime.now().year, 1900, -1))

        col1, col2, col3 = st.columns(3)
        with col1:
            dia = st.selectbox("Día", dias)
        with col2:
            mes_nombre = st.selectbox("Mes", meses)
        with col3:
            anio = st.selectbox("Año", anios)
