
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
            
        
        id_logopeda = st.session_state.get("id_logopeda")
        
        
        
        if id_logopeda:
            col1, col2 = st.columns([1,1])
            with col1:
                st.image(imagen, use_container_width=True)
            
            col3, col4, col5= st.columns([2,2,4])
            with col5:

                lista_pacientes = paciente_service.obtener_pacientes_por_logopeda(id_logopeda)
            
                if lista_pacientes:
                    
                    for paciente in lista_pacientes:
                        st.write(f"- {paciente.nombre}")
                else:
                    st.write("No tienes pacientes asignados.")

        boton_registrar_paciente = st.button("Crear nuevo paciente")

        if boton_registrar_paciente:
            st.session_state.pantalla = 2
            st.rerun()


    
    
    
    