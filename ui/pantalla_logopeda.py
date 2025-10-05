
import streamlit as st
from services import paciente_service

from PIL import Image

def pantalla_logopeda():

    imagen = Image.open("images/logo_y_nombre.png")

    with st.sidebar:
            
            if st.button("Cerrar sesión"):
                st.session_state.pantalla = 0
                st.session_state["usuario"] = ""
                st.session_state["id_logopeda"] = ""
                st.rerun()


    with st.container():
            
        
        id_logopeda = st.session_state.get("id_logopeda", "")
        
        
        
        if id_logopeda:
            
            col1, col2 = st.columns([1,1])

            with col1:
                st.image(imagen, use_container_width=True)
            
            col3, col4 = st.columns([1,3])
            with col4:

                ok, lista_pacientes = paciente_service.obtener_pacientes_por_logopeda(id_logopeda)
            
                if ok and lista_pacientes:
                    st.write("Pacientes asignados:")
                    for paciente in lista_pacientes[1]:
                        st.write(f"- {paciente.nombre} {paciente.apellidos}, Edad: {paciente.edad}")
                else:
                    st.write("No tienes pacientes asignados.")

        boton_registrar_paciente = st.button("Crear nuevo paciente")

        if boton_registrar_paciente:
            st.session_state.pantalla = 2
            st.rerun()


    
    
    
    