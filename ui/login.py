import streamlit as st

from services import logopeda_service

from PIL import Image

from utils import password

def pantalla_login():

    imagen = Image.open("images/logo_y_nombre.png")
    
    if "modo_registro" not in st.session_state:
        st.session_state.modo_registro = False

    # Mostrar login o registro según el modo
    if not st.session_state.modo_registro:
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            
            with st.form("login_form"):

                st.image(imagen, use_container_width=True)
                
                usuario = st.text_input("", key="login_usuario", placeholder="Usuario")
                contrasenia = st.text_input("Contraseña", type="password", key="login_contrasenia")
                
                col4, col5, col6 = st.columns([1,1,1])
                with col5:
                    boton_entrar = st.form_submit_button("Entrar")
                

                if boton_entrar:
                    if not usuario or not contrasenia:
                        st.error("❌ Por favor, complete todos los campos.")
                    else:
                        valido, resultado = logopeda_service.validar_logopeda(usuario, contrasenia)
                        if valido:
                            st.success("Bienvenido, "+ usuario)
                            st.session_state["usuario"] = usuario
                            logopeda = logopeda_service.find_logopeda_by_user(usuario)
                            if logopeda:
                                st.session_state["id_logopeda"] = logopeda.id
                            else:
                                st.error("❌ Error al recuperar el ID del logopeda registrado.")
                                return
                            st.session_state.pantalla = 1 
                            st.rerun()                 
                        else:
                            st.error(resultado)
            boton_eres_nuevo = st.button("¿Eres nuevo?")
            if boton_eres_nuevo:
                st.session_state.modo_registro = True
                st.rerun()  # Volvemos a renderizar con el modo registro

    else:  # Modo registro

        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            with st.form("registro_form"):

                st.image(imagen, use_container_width=True)
                    
                nuevo_usuario = st.text_input("Nuevo usuario", key="registro_usuario")
                nueva_contrasenia = st.text_input("Nueva contraseña", type="password", key="registro_contrasenia")
                confirmar_contrasenia = st.text_input("Confirmar contraseña", type="password",  key="registro_confirmar_contrasenia")

                

                col4, col5, col6 = st.columns([1,1,1])
                with col5:
                    boton_registrar = st.form_submit_button("Registrar")
                

                if boton_registrar:
                    if not nuevo_usuario or not nueva_contrasenia:
                        st.error("❌ Por favor, complete todos los campos.")
                    elif nueva_contrasenia != confirmar_contrasenia:
                        st.error("❌ Las contraseñas no coinciden.")
                    else:
                        registrado, mensaje = logopeda_service.registrar_logopeda(nuevo_usuario, nueva_contrasenia)
                        if registrado:
                            st.success(mensaje)
                            st.session_state["usuario"] = nuevo_usuario
                            logopeda = logopeda_service.find_logopeda_by_user(nuevo_usuario)
                            if logopeda:
                                st.session_state["id_logopeda"] = logopeda.id
                            else:
                                st.error("❌ Error al recuperar el ID del logopeda registrado.")
                                return
                            st.session_state.pantalla = 1
                            st.session_state.modo_registro = False
                            st.rerun()
                        else:
                            st.error(mensaje)
            boton_volver_login = st.button("Volver al login")
            if boton_volver_login:
                st.session_state.modo_registro = False
                st.rerun()




    




