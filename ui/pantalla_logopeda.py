
import streamlit as st
from services import paciente_service

def pantalla_logopeda():
    
    usuario = st.session_state.get("usuario", "Usuario desconocido")
    st.title(f"Bienvenido, " +  usuario)
    
    
    id_logopeda = st.session_state.get("id_logopeda")
    
    st.write("Id Logopeda: " + id_logopeda)
    
    if id_logopeda:

        ok, lista_pacientes = paciente_service.obtener_pacientes_por_logopeda(id_logopeda)
        
        if ok and lista_pacientes:
            st.write("Pacientes asignados:")
            for paciente in lista_pacientes[1]:
                st.write(f"- {paciente.nombre} {paciente.apellidos}, Edad: {paciente.edad}")
        else:
            st.write("No tienes pacientes asignados.")

    

    col1 = st.columns([1,1])
    with col1:
        ok, pacientes = paciente_service.obtener_pacientes_por_logopeda(id_logopeda)
        if ok and pacientes:
            st.subheader("📋 Lista de pacientes")
            for paciente in pacientes:
                st.write(f"{paciente.nombre} {paciente.apellidos}")
        else:
            st.info("No tienes pacientes asignados.")
    

    if st.button("Registrar nuevo paciente"):
        st.session_state.pantalla = 3
        
    

    