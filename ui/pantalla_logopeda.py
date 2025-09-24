import streamlit as st
from core.services.paciente_service import PacienteService

def pantalla_logopeda(paciente_service: PacienteService):
    st.title("Logopeda - Panel Principal")

    if 'show_pacientes' not in st.session_state:
        st.session_state.show_pacientes = False

    col1, col2 = st.columns([1,1])
    with col1:
        if st.button("Ver pacientes"):
            st.session_state.show_pacientes = not st.session_state.show_pacientes
    with col2:
        if st.button("Registrar nuevo paciente"):
            st.session_state.pantalla = 2
            st.rerun()

    if st.session_state.show_pacientes:
        pacientes = paciente_service.listar_pacientes(st.session_state.get("id_logopeda"))
        if pacientes:
            st.subheader("Lista de pacientes")
            cols = st.columns(3)
            for i, paciente in enumerate(pacientes):
                with cols[i % 3]:
                    key = f"pac_{paciente.id}"
                    if st.button(f"{paciente.nombre} {paciente.apellidos}", key=key):
                        st.session_state.paciente_actual_id = paciente.id
                        st.session_state.pantalla = 3
                        st.rerun()
        else:
            st.info("No tienes pacientes registrados aún.")
