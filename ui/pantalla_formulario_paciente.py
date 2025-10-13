
from datetime import datetime
import logging
import streamlit as st

from services import paciente_service

def pantalla_formulario_paciente():


    with st.sidebar:
            
            if st.button("Volver"):
                st.session_state.pantalla = 1
                st.rerun()
            if st.button("Cerrar sesión"):
                st.session_state.pantalla = 0
                st.session_state["usuario"] = ""
                st.session_state["id_logopeda"] = ""
                st.rerun()
    
    with st.form("formulario_paciente"):
        
        nombre = st.text_input("", placeholder="Nombre", help="Introduce el nombre del paciente")
        apellidos = st.text_input("", placeholder="Apellidos", help="Introduce los apellidos del paciente")
        email = st.text_input("", placeholder="Email de contacto", help="Introduce el email del contacto del paciente")



        dias = list(range(1, 32))
        meses = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]
        anios = list(range(datetime.now().year, 1900, -1))

        with st.container():
            st.write("Fecha de nacimiento")
            col1, col2, col3 = st.columns(3)
            with col1:
                dia = st.selectbox("Día", dias)
            with col2:
                mes_nombre = st.selectbox("Mes", meses)
            with col3:
                anio = st.selectbox("Año", anios)

        profesiones_opciones = ["Escoger una opción","Jardinero", "Profesor"]
        estudios_opciones = ["Escoger una opción","Primaria", "Secundaria", "Bachillerato", "Grado", "Master", "Doctorado"]
        aficiones_opciones = ["Música", "Deportes", "Lectura","Senderismo", "Cine","Teatro","Videojuegos","Arte","Cocina","Viajes","Tecnología","Jardinería","Fotografía","Baile","Animales","Manualidades","Meditación","Yoga"]
        habito_lector_opciones = ["Escoger una opción", "Lee todos/Casi todos los días", "Una/Dos veces por semana", "Alguna vez al mes", "Alguna vez al trimestre", "Casi nunca", "Nunca"]

        profesion = st.selectbox("Profesion", profesiones_opciones,  help="Selecciona la profesión del paciente")
        estudios = st.selectbox("Estudios", estudios_opciones, help="Selecciona el nivel de estudios del paciente")

        select_habito_lector = st.selectbox("¿Tiene hábito lector?", habito_lector_opciones, help="Indica si el paciente tiene hábito lector")

        

        aficiones = st.multiselect("Aficiones", aficiones_opciones, placeholder="Elegir aficiones", help="Selecciona las aficiones del paciente")

        boton_siguiente = st.form_submit_button("Siguiente")

        if boton_siguiente:
            
            campos_obligatorios = [nombre, apellidos, email, profesion, estudios, select_habito_lector, aficiones]

            if all(campos_obligatorios) and \
               profesion != "Escoger una opción" and \
               estudios != "Escoger una opción" and \
               select_habito_lector != "Escoger una opción" and \
               aficiones:
                
                try:
                    fecha_nacimiento = datetime(anio, meses.index(mes_nombre) + 1, dia)
                    edad = int(datetime.now().year - fecha_nacimiento.year)

                    if (select_habito_lector=="Lee todos/Casi todos los días" or select_habito_lector=="Una/Dos veces por semana"):
                        habito_lector = "Lector frecuente" 
                    elif (select_habito_lector=="Alguna vez al mes" or select_habito_lector=="Alguna vez al trimestre"):
                        habito_lector = "Lector ocasional"
                    else:
                        habito_lector = "No lector"

                    """
                    exito, mensaje, nuevo_paciente = paciente_service.registrar_paciente(
                        id_logopeda=st.session_state.get("id_logopeda"),
                        nombre=nombre,
                        apellidos=apellidos,
                        email=email,
                        edad=edad,
                        profesion=profesion,
                        estudios=estudios,
                        habito_lector=habito_lector,
                        aficiones=aficiones
                    )
                    """
                    

                    st.session_state["nombre"] = nombre
                    st.session_state["apellidos"] = apellidos
                    st.session_state["email"] = email
                    st.session_state["edad"] = edad
                    st.session_state["profesion"] = profesion
                    st.session_state["habito_lector"] = habito_lector
                    st.session_state["aficiones"] = aficiones
                    
                    
                    
                    
                    
                    """
                    if exito and nuevo_paciente:
                        st.success(mensaje)
                        st.session_state["id_paciente"] = nuevo_paciente.id
                        st.session_state.pantalla = 3
                        st.rerun()
                    else:
                        st.error(mensaje)
                    """
                    
                except ValueError:
                    st.error("❌ Fecha no válida. Por favor, seleccionar una fecha correcta.")
                    return
                
            else:
                st.error("❌ Por favor, complete todos los campos.")
                return