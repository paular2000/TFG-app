
import streamlit as st

from datetime import datetime
from services import paciente_service

def pantalla_registro_paciente():

    st.title("Registro de nuevo paciente")

    with st.form(key="registro_form"):
        nombre = st.text_input("Nombre")
        apellidos = st.text_input("Apellidos")

        dias = list(range(1, 32))
        meses = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]
        anios = list(range(datetime.now().year, 1900, -1))

        col1, col2, col3 = st.columns(3)
        with col1:
            dia = st.selectbox("Día", dias)
        with col2:
            mes_nombre = st.selectbox("Mes", meses)
        with col3:
            anio = st.selectbox("Año", anios)
        
        fecha_nacimiento = datetime(anio, meses.index(mes_nombre) + 1, dia)

        profesiones_opciones = ["Escoger una opción","Jardinero", "Profesor"]
        estudios_opciones = ["Escoger una opción","Primaria", "Secundaria", "Bachillerato", "Grado", "Master", "Doctorado"]
        aficiones_opciones = ["Música", "Deportes", "Lectura","Forjar espadas", "Fumar pipas","Canto en lenguas antiguas"]

        profesion = st.selectbox("Elija su profesión:", profesiones_opciones)
        estudios = st.selectbox("Elija su nivel de estudios:", estudios_opciones)
        aficiones = st.multiselect("Elija sus aficiones:", aficiones_opciones,placeholder="Escoger opciones")



        if st.form_submit_button("Siguiente"): 

            campos_obligatorios = [nombre, apellidos, fecha_nacimiento, profesion, estudios, aficiones]

            if all(campos_obligatorios) and \
                profesion != "Escoger una opción" and \
                estudios != "Escoger una opción" and \
                aficiones:
                
                try:
    
                    registrado = paciente_service.registrar_paciente(
                        id_logopeda=st.session_state.id_logopeda,
                        nombre=nombre,
                        apellidos=apellidos,
                        fecha_nacimiento=fecha_nacimiento.strftime("%d/%m/%Y"),
                        profesion=profesion,
                        estudios=estudios,
                        aficiones=aficiones
                    )

                    if registrado:
                        st.success(f"✅ Paciente {nombre} {apellidos} registrado con éxito.")
                        st.session_state.pantalla = 4
                except ValueError:
                    st.error("⚠️ Fecha inválida.")
            else:
                st.warning("⚠️ Se deben completar todos los campos obligatorios.")