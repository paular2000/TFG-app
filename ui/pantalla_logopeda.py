
import streamlit as st
from services import paciente_service

from PIL import Image

def pantalla_logopeda():

    imagen_logo = Image.open("images/logo_y_nombre.png")
    imagen_paciente = Image.open("images/icon_paciente.jpg")


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
                st.image(imagen_logo, use_container_width=True)

            with col2:
                busqueda = st.text_input("", placeholder="🔍 Buscar paciente", help="Buscar un paciente por su nombre")


            
            col4, col5, col6= st.columns([1,1,3])
            with col6:

                lista_pacientes = paciente_service.obtener_pacientes_por_logopeda(id_logopeda)
            
                if lista_pacientes:
                    
                    # Recorremos la lista en bloques de 4
                    for i in range(0, len(lista_pacientes), 4):
                        cols = st.columns(4)  # 4 columnas por fila
                        
                        for j, col in enumerate(cols):
                            if i + j < len(lista_pacientes):
                                paciente = lista_pacientes[i + j]
                                with col:
                                    st.image(imagen_paciente, use_container_width=True)
                                    st.write(f"**{paciente.nombre} {paciente.apellidos}**")
                else:
                    st.info("No tienes pacientes asignados. Crea uno nuevo.")

        boton_registrar_paciente = st.button("Crear nuevo paciente")

        if boton_registrar_paciente:
            st.session_state.pantalla = 2
            st.rerun()


    
    
    
    