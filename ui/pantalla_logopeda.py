
import streamlit as st
from services import paciente_service

def pantalla_logopeda():
    
    usuario = st.session_state.get("usuario", "Usuario desconocido")
    st.title(f"Bienvenido, " +  usuario)
    
    id_logopeda = st.session_state.get("id_logopeda")
    if not id_logopeda:
        st.error("❌ Error: ID de logopeda no encontrado en la sesión.")
        return
    
    

    

    
    if st.button("Registrar nuevo paciente"):
        st.session_state.pantalla = 3
        
    

    