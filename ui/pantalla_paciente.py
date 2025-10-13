
from PIL import Image
import streamlit as st
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

        col1, col2, col3 = st.columns([3,5,5])

        with col1:
            st.image(imagen_paciente, use_container_width=True)
        with col2:
            
            st.markdown(f'<span style="font-size: 24px; font-weight: bold">{paciente.nombre} {paciente.apellidos}</span>', unsafe_allow_html=True)

             
         
         

    