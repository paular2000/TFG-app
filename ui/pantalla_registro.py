import streamlit as st
from datetime import datetime
from core.services.paciente_service import PacienteService
from core.models import Paciente

def pantalla_registro(paciente_service: PacienteService):
    st.title("Registro de Pacientes")
    st.write("Por favor, introduzca los datos del paciente.")

    with st.form(key="registro_form"):
        nombre = st.text_input("Nombre")
        apellidos = st.text_input("Apellidos")
        dias = list(range(1, 32))
        meses = [ "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
                  "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        anios = list(range(datetime.now().year, 1900, -1))
        col1, col2, col3 = st.columns(3)
        with col1: dia = st.selectbox("Día", dias)
        with col2: mes_nombre = st.selectbox("Mes", meses)
        with col3: anio = st.selectbox("Año", anios)

        profesiones_opciones = ["Escoger una opción","Jardinero", "Profesor"]
        estudios_opciones = ["Escoger una opción","Primaria", "Secundaria", "Bachillerato", "Grado", "Master", "Doctorado"]
        aficiones_opciones = ["Música", "Deportes", "Lectura","Forjar espadas", "Fumar pipas","Canto en lenguas antiguas"]

        profesion = st.selectbox("Elija su profesión:", profesiones_opciones)
        estudios = st.selectbox("Elija su nivel de estudios:", estudios_opciones)
        aficiones = st.multiselect("Elija sus aficiones:", aficiones_opciones,placeholder="Escoger opciones")

        submit = st.form_submit_button("Siguiente")

        if submit:
            campos_obligatorios = [nombre, apellidos, profesion, estudios, aficiones]
            if all(campos_obligatorios) and profesion != "Escoger una opción" and estudios != "Escoger una opción" and aficiones:
                try:
                    fecha_nacimiento = datetime(anio, meses.index(mes_nombre) + 1, dia)
                    edad = int(datetime.now().year - fecha_nacimiento.year)

                    paciente = Paciente(
                        id="",
                        id_logopeda=st.session_state.get("id_logopeda"),
                        nombre=nombre,
                        apellidos=apellidos,
                        edad=edad,
                        profesion=profesion,
                        estudios=estudios,
                        aficion=aficiones,
                        resultados={}
                    )

                    id_paciente = paciente_service.registrar_paciente(paciente)
                    if id_paciente:
                        st.session_state.id_paciente = id_paciente
                        st.session_state.pantalla = 4
                        st.rerun()
                except ValueError:
                    st.error("⚠️ Fecha inválida.")
            else:
                st.warning("⚠️ Se deben completar todos los campos obligatorios.")
