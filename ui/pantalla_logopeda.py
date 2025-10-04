
import streamlit as st
from services import paciente_service

def pantalla_logopeda():
    
    usuario = st.session_state.get("usuario", "Usuario desconocido")
    st.title(f"Bienvenido, " +  usuario)
    
    

    
    if st.button("Registrar nuevo paciente"):
        st.session_state.pantalla = 3
        
    

    