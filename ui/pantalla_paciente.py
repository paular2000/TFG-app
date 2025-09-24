import streamlit as st
from core.services.paciente_service import PacienteService

def pantalla_paciente(paciente_service: PacienteService):
    pid = st.session_state.get("paciente_actual_id")
    if not pid:
        st.error("No se encontró el paciente seleccionado.")
        return

    paciente = paciente_service.obtener_paciente_por_id(pid)
    if not paciente:
        st.error("No se ha podido cargar la ficha del paciente.")
        return

    st.title(f"🧑 Paciente: {paciente.nombre} {paciente.apellidos}")
    st.write(f"**Edad:** {paciente.edad}")
    st.write(f"**Profesión:** {paciente.profesion}")
    st.write(f"**Estudios:** {paciente.estudios}")
    st.write(f"**Aficiones:** {', '.join(paciente.aficion)}")

    if st.button("⬅️ Volver"):
        st.session_state.pantalla = 1
        st.rerun()
