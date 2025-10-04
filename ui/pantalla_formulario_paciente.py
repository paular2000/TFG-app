
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

        profesiones_opciones = ["Escoger una opción","Jardinero", "Profesor"]
        estudios_opciones = ["Escoger una opción","Primaria", "Secundaria", "Bachillerato", "Grado", "Master", "Doctorado"]
        aficiones_opciones = ["Música", "Deportes", "Lectura","Senderismo", "Cine","Teatro","Videojuegos","Arte","Cocina","Viajes","Tecnología","Jardinería","Fotografía","Baile","Animales","Manualidades","Meditación","Yoga"]


        profesion = st.selectbox("", profesiones_opciones, placeholder="Profesión", help="Selecciona la profesión del paciente")
        estudios = st.selectbox("", estudios_opciones, placeholder="Estudios", help="Selecciona el nivel de estudios del paciente")
        aficiones = st.multiselect("", aficiones_opciones, placeholder="Aficiones", help="Selecciona las aficiones del paciente")

        submit = st.form_submit_button("Siguiente")