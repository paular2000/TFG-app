import streamlit as st
import base64
from services import logopeda_service


def pantalla_login():


    logo_base64 = load_image_as_base64("images/Logo.png")
       
    st.markdown(
        f"""
        <style>
        .titulo {{
            display: flex;
            flex-direction: center;
            align-items: center;
            width: 500px;       
            height: 500px; 
            border: 2px solid black;
            padding: 12px;
            border-radius: 10px;
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            color: #222;
            background: #f9f9f9;
            transition: all 0.3s ease;

        }}
        .titulo:hover {{
            background: #FFD700;
            color: white;
            cursor: pointer;
            transform: scale(1.02);
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }}


        </style>
        <body>
            <div class="titulo">
                <img src="data:image/png;base64,{logo_base64}"> 
                <p></p>
                <p></p>
            </div>

        </body>""",       
        unsafe_allow_html=True
    )


    st.write("")
    
    if "modo_registro" not in st.session_state:
        st.session_state.modo_registro = False

    # Mostrar login o registro según el modo
    if not st.session_state.modo_registro:
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            
            with st.form("login_form"):
                
                usuario = st.text_input("Usuario", key="login_usuario")
                contrasenia = st.text_input("Contraseña", type="password", key="login_contrasenia")
                boton_entrar = st.form_submit_button("Entrar")
                col4 = st.columns([1])
                with col4[0]:
                    boton_eres_nuevo = st.form_submit_button("¿Eres nuevo?")

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

                if boton_eres_nuevo:
                    st.session_state.modo_registro = True
                    st.rerun()  # Volvemos a renderizar con el modo registro

    else:  # Modo registro
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.subheader("Registrarse") 
            nuevo_usuario = st.text_input("Nuevo usuario", key="registro_usuario")
            nueva_contrasenia = st.text_input("Nueva contraseña", type="password", key="registro_contrasenia")
            confirmar_contrasenia = st.text_input("Confirmar contraseña", type="password",  key="registro_confirmar_contrasenia")

            boton_registrar = st.button("Registrar")
            boton_volver_login = st.button("Volver al login")

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

            if boton_volver_login:
                st.session_state.modo_registro = False
                st.rerun()




    




    """
    # Botones principales
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Iniciar Sesión"):
            st.subheader("Iniciar sesión")
        
        usuario = st.text_input("Usuario", key="login_usuario")
        contrasenia = st.text_input("Contraseña", type="password", key="login_contrasenia")
        if st.button("Entrar", key="btn_login"):
            if not usuario or not contrasenia:
                st.error("❌ Por favor, complete todos los campos.")
            else:
                valido, resultado = logopeda_service.validar_logopeda(usuario, contrasenia)
                if valido:
                    st.success("Bienvenido, "+ usuario)

                    
                    st.session_state["usuario"] = usuario

                    logopeda = logopeda_service.find_logopeda_by_user(usuario)
                    if logopeda:
                        st.session_state["id_logopeda"] = logopeda.id # Guardo el id del logopeda en "memoria"
                    else:
                        st.error("❌ Error al recuperar el ID del logopeda registrado.")
                        return   
                                     
                    st.session_state.pantalla = 1 
                    st.rerun()                 
                    
                else:
                    st.error(resultado)
            
    with col2:
        if st.button("Registrarse"):
            st.subheader("Registrarse") # Caso de primera vez en la app
        
        nuevo_usuario = st.text_input("Nuevo usuario", key="registro_usuario")
        nueva_contrasenia = st.text_input("Nueva contraseña", type="password", key="registro_contrasenia")
        confirmar_contrasenia = st.text_input("Confirmar contraseña", type="password",  key="registro_confirmar_contrasenia")
        if st.button("Registrar", key="btn_registro"):
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
                    
                    # Obtener el objeto logopeda para guardar su ID
                    logopeda = logopeda_service.find_logopeda_by_user(nuevo_usuario)
                    
                    if logopeda:
                        st.session_state["id_logopeda"] = logopeda.id # Guardo el id del logopeda en "memoria"
                    else:
                        st.error("❌ Error al recuperar el ID del logopeda registrado.")
                        return
                    
                    st.session_state.pantalla = 1
                    st.rerun()

                else:
                    st.error(mensaje)
        

        """


def load_image_as_base64(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()