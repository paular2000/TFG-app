import streamlit as st
from services import logopeda_service


def pantalla_login():
    st.title("DuraGUI")

    opciones = st.radio("Elegir", ("Iniciar sesión", "Registrarse"))

    if opciones == "Iniciar sesión":
        st.subheader("Iniciar sesión")
        
        usuario = st.text_input("Usuario", key="login_usuario")
        contrasenia = st.text_input("Contraseña", type="password", key="login_contrasenia")
        if st.button("Entrar", key="btn_login"):
            if not usuario or not contrasenia:
                st.error("❌ Por favor, complete todos los campos.")
            else:
                valido, resultado = logopeda_service.validar_logopeda(usuario, contrasenia)
                if valido:
                    st.success(f"✅ Bienvenido/a, {usuario}!")
                    st.session_state["pantalla"] = "logopeda"   # ir a pantalla principal       
                    st.session_state["id_logopeda"] = resultado 
                    st.rerun()                    # forzar recarga de main()
                    
                else:
                    st.error(resultado)
    else:
        st.subheader("Registrarse")
        
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
                    # Obtener el objeto logopeda para guardar su ID
                    logopeda = logopeda_service.find_logopeda_by_user(nuevo_usuario)
                    if logopeda:
                        st.session_state["id_logopeda"] = logopeda.id

                    else:
                        st.error("❌ Error al recuperar el ID del logopeda registrado.")
                        return
                    st.session_state.pantalla = "logopeda"
                    st.rerun()
                else:
                    st.error(mensaje)