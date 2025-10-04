
import streamlit as st
from services import paciente_service

def pantalla_logopeda():
    
    usuario = st.session_state.get("usuario", "Usuario desconocido")
    st.title(f"Bienvenido, " +  usuario)
    
    
    id_logopeda = st.session_state.get("id_logopeda")
    
    st.write("Id Logopeda: " + id_logopeda)

    if st.button("Registrar nuevo paciente"):
        st.session_state.pantalla = 3
        
    

    