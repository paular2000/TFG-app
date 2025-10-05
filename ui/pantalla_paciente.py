
import streamlit as st
from services import paciente_service

def pantalla_paciente():

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
    

    

    st.title("ID Paciente: " + id_paciente)