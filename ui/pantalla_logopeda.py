
import streamlit as st
from services import paciente_service

from PIL import Image

def pantalla_logopeda():

    imagen_logo = Image.open("images/logo_nombre.jpg")
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


        col3, col4 = st.columns([1,2])
        with col4:
            busqueda = st.text_input("", placeholder="🔍 Buscar paciente", help="Buscar un paciente por su nombre")


            
        col5, col6, col7= st.columns([1,1,3])
        with col7:

            lista_pacientes = paciente_service.obtener_pacientes_por_logopeda(id_logopeda)

            if lista_pacientes:

                if busqueda:
                    lista_pacientes = paciente_service.obtener_pacientes_por_nombre(id_logopeda, busqueda)

                lista_pacientes = sorted(lista_pacientes, key=lambda p: p.nombre.lower())

                if lista_pacientes:
                    
                    for i in range(0, len(lista_pacientes), 4):
                        cols = st.columns(4)  # 4 columnas por fila
                        
                        for j, col in enumerate(cols):
                            if i + j < len(lista_pacientes):
                                paciente = lista_pacientes[i + j]
                                with col:                                    
                                    st.markdown(
                                        f'''
                                            <a href="#" onclick="window.parent.location.href='?paciente_id={paciente.id}'" style="text-decoration:none;">
                                                <img src="{imagen_paciente}" width="150" style="border-radius:10px;"/>
                                                <p style="text-align:center; color:black;">{paciente.nombre} {paciente.apellidos}</p>
                                            </a>
                                            ''',
                                            unsafe_allow_html=True
                                            
                                        )
                                    query_params = st.experimental_get_query_params()

                                    if "paciente_id" in query_params:
                                        paciente_id = query_params["paciente_id"][0]
                                        st.session_state["paciente_actual_id"] = paciente_id
                                        st.session_state.pantalla = 4
                                        
                st.info("No tienes pacientes asignados. Crea uno nuevo.")

        boton_registrar_paciente = st.button("Crear nuevo paciente")

        if boton_registrar_paciente:
            st.session_state.pantalla = 2
            st.rerun()


    
    
    
    