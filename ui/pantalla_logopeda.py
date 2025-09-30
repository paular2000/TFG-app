
import streamlit as st
from services import paciente_service

def pantalla_logopeda():
    
    usuario = st.session_state.get("usuario", "Usuario desconocido")
    st.title(f"Bienvenido, " +  usuario)
    
    id_logopeda = st.session_state.get("id_logopeda")
    if not id_logopeda:
        st.error("❌ Error: ID de logopeda no encontrado en la sesión.")
        return
    
    

    col1, col2 = st.columns([1,1])
    with col1:
        pacientes = paciente_service.obtener_pacientes_por_logopeda(id_logopeda)
        if not pacientes:
            st.info("No tienes pacientes registrados aún.")
            
    with col2:
        if st.button("Registrar nuevo paciente"):
            st.session_state.pantalla = "registro_paciente"
            st.experimental_rerun()
    
    
    