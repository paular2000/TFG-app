
import streamlit as st
import pandas as pd

from PIL import Image

from services import paciente_service

def pantalla_paciente():

    imagen_paciente = Image.open("images/icon_paciente.jpg")

    with st.sidebar:
            
            if st.button("Volver"):
                st.session_state.pantalla = 1
                st.rerun()
            if st.button("Cerrar sesión"):
                st.session_state.pantalla = 0
                st.session_state["usuario"] = ""
                st.session_state["id_logopeda"] = ""
                st.rerun()


    id_paciente = st.session_state.get("paciente_actual_id")
    
    paciente = paciente_service.obtener_paciente_por_id(id_paciente)
    
    if paciente:

        col1, col2, col3, col4, col5 = st.columns([4,2,6,3,5])

        with col1:
            st.image(imagen_paciente, use_container_width=True)
        with col3:
            st.markdown(f'<span style="font-size: 24px; font-weight: bold">{paciente.nombre} {paciente.apellidos}</span>', unsafe_allow_html=True)
            st.write("Diagnóstico: ")
            st.write(f"Nivel educativo: {paciente.estudios}")
            st.write(f"Proefsión: {paciente.profesion}")
        with col5:
            st.write(f"📌Última sesión: -------")
            st.write("🗒️Notas rápidas: ")

        st.write("")
        st.write("")


        col1, col2 = st.columns([4,16])

        with col2:
            st.markdown(f'<span style="font-size: 24px; font-weight: bold">Biblioteca de actividades sugeridas</span>', unsafe_allow_html=True)

        col1, col2, col3, col4, col5 = st.columns([4,2,2,2,5])
        with col2:
             st.write("-")
        with col3:
             st.write("-")
        with col4:
             st.write("-")
        
        st.write("")
        st.write("")
        
        col1, col2 = st.columns([4,16])
        with col2:
            st.markdown(f'<span style="font-size: 24px; font-weight: bold">Favoritas</span>', unsafe_allow_html=True)

        st.write("")
        st.write("")
        
        col1, col2 = st.columns([4,16])
        with col2:
            st.markdown(f'<span style="font-size: 24px; font-weight: bold">Evolución</span>', unsafe_allow_html=True)
             
            chart_data = pd.DataFrame({
                "Aciertos": [120, 250, 175, 300],
                "Errores": [80, 150, 100, 180],
            }, index=["A", "B", "C", "D"])
        
            st.bar_chart(chart_data)