
from PIL import Image
import streamlit as st
from services import paciente_service

def pantalla_paciente():

    imagen_logo = Image.open("images/logo_nombre.jpg")

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

        col1, col2, col3 = st.columns([1,4,4])

        with col1:
            st.image(imagen_logo, use_container_width=True)
        with col2:
            st.markdown(f"**{paciente.nombre} {paciente.apellidos}**")
             
             
         
         

    