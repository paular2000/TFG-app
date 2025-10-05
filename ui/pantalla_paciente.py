
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
    

    paciente = paciente_service.obtener_paciente_por_id(id_paciente)

    if not paciente:
        st.error("No se ha podido cargar la ficha del paciente.")
        return

    st.title("ID Paciente: " + paciente.id)