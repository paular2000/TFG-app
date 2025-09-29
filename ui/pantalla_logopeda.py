
import streamlit as st
from services import paciente_service

def pantalla_logopeda():
    usuario = st.session_state.get("usuario", "Logopeda")
    st.title(f"Bienvenido, {st.session_state[usuario]}")

    id_logopeda = st.session_state["id_logopeda"]

    # Botón para mostrar/ocultar pacientes
    if "show_pacientes" not in st.session_state:
        st.session_state.show_pacientes = False

    col1, col2 = st.columns([1,1])
    with col1:
        if st.button("Ver pacientes"):
            st.session_state.show_pacientes = not st.session_state.show_pacientes
    with col2:
        if st.button("Registrar nuevo paciente"):
            st.session_state.pantalla = "registro_paciente"
            st.experimental_rerun()
    
    if st.session_state.show_pacientes:
        ok, pacientes = paciente_service.obtener_pacientes_por_logopeda(id_logopeda)
        if ok and pacientes:
            st.subheader("📋 Lista de pacientes")
            cols = st.columns(3)  # 3 columnas por fila

            for i, paciente in enumerate(pacientes):
                with cols[i % 3]:
                    key = f"paciente_{paciente.id}"
                    if st.button(f"{paciente.nombre} {paciente.apellidos}", key=key):
                        st.session_state["paciente_actual_id"] = paciente.id
                        st.session_state.pantalla = "ficha_paciente"
                        st.experimental_rerun()
        else:
            st.info("No tienes pacientes registrados aún.")