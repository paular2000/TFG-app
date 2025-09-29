import streamlit as st
from core.services.logopeda_service import LogopedaService

def pantalla_login(logopeda_service: LogopedaService):
    st.title("DURAGUI")
    st.write("Por favor, inicie sesión o regístrese.")

    if "modo_login" not in st.session_state:
        st.session_state.modo_login = None


    # Botones principales
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Iniciar Sesión"):
            st.session_state.modo_login = "login"
    with col2:
        if st.button("Registrarse"):
            st.session_state.modo_login = "registro"

    # Formulario de login:
    if st.session_state.modo_login == "login":
        st.subheader("Iniciar Sesión")

        with st.form(key="login_form"):
            usuario = st.text_input("Usuario")
            contrasenia = st.text_input("Contraseña", type="password")
            submit = st.form_submit_button("Ingresar")

            if submit:
                if not usuario or not contrasenia:
                    st.error("❌ Por favor, complete todos los campos.")
                else:
                    ok, id_logopeda = logopeda_service.validar_logopeda(usuario, contrasenia)
                    if ok and id_logopeda:
                        st.success("✅ Inicio de sesión exitoso.")
                        st.session_state.id_logopeda = id_logopeda
                        st.session_state.modo_login = None
                        st.experimental_rerun()
                    else:
                        st.error("❌ Usuario o contraseña incorrectos.")

        
    # Formulario de registro:
    elif st.session_state.modo_login == "registro":
        st.subheader("Registrarse")

        with st.form(key="registro_form"):
            usuario = st.text_input("Usuario")
            contrasenia = st.text_input("Contraseña", type="password")
            confirmar_contrasenia = st.text_input("Confirmar Contraseña", type="password")
            submit = st.form_submit_button("Registrar")

            if submit:
                if not usuario.strip():
                    st.error("⚠️ El nombre de usuario no puede estar vacío.")
                elif not contrasenia.strip():
                    st.error("⚠️ La contraseña no puede estar vacía.")
                elif contrasenia != confirmar_contrasenia:
                    st.error("⚠️ Las contraseñas no coinciden.")
                else:
                    ok, mensaje = logopeda_service.registrar_logopeda(usuario, contrasenia)
                    if ok:
                        st.success(f"✅ Bienvenido, {usuario}. Su cuenta ha sido creada.")
                        st.session_state.modo_login = None
                        st.experimental_rerun()
                    else:
                        st.error(mensaje)



                       