
import streamlit as st
from services import paciente_service

from PIL import Image

def pantalla_logopeda():

    imagen = Image.open("images/logo_y_nombre.png")

    with st.sidebar:
            st.title("Menú")
            if st.button("Cerrar sesión"):
                st.session_state.pantalla = 0
                st.session_state["usuario"] = ""
                st.session_state["id_logopeda"] = ""
                st.rerun()


    with st.container():
            
        usuario = st.session_state.get("usuario", "Usuario desconocido")
            
        
        
        id_logopeda = st.session_state.get("id_logopeda")
        st.write("Id Logopeda: " + id_logopeda)
        
        if id_logopeda:
            
            #col1, col2, col3, col4 = st.columns([1,1,1,1])

            st.image(imagen, use_container_width=True)
            
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


    
    
    
    