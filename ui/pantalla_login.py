import streamlit as st
from core.services.logopeda_service import LogopedaService

def pantalla_login(logopeda_service: LogopedaService):
    st.title("DURAGUI")
    st.write("Por favor, inicie sesión o regístrese.")

    if "modo_login" not in st.session_state:
        st.session_state.modo_login = None



    col1, col2 = st.columns(2)
    with col1:
        if st.button("Iniciar Sesión"):
            st.session_state.modo_login = "login"
    with col2:
        if st.button("Registrarse"):
            st.session_state.modo_login = "registro"

    if st.session_state.modo_login == "login":
        st.subheader("Iniciar Sesión")
        with st.form("form_login"):
            usuario = st.text_input("Usuario")
            contrasena = st.text_input("Contraseña", type="password")
            submit_login = st.form_submit_button("Entrar")

            if submit_login:
                ok, result = logopeda_service.validar_logopeda(usuario, contrasena)
                if ok:
                    st.success(f"Bienvenido, {usuario}")
                    st.session_state["id_logopeda"] = result
                    st.session_state["usuario"] = usuario
                    st.session_state["autenticado"] = True
                    st.session_state.pantalla = 1
                else:
                    st.error("❌ Usuario o contraseña incorrectos.")

    elif st.session_state.modo_login == "registro":
        st.subheader("Registro de nuevo logopeda")
        with st.form("form_registro"):
            nuevo_usuario = st.text_input("Nombre de usuario")
            nueva_contrasena = st.text_input("Contraseña", type="password")
            confirmar_contrasena = st.text_input("Confirmar contraseña", type="password")
            submit_registro = st.form_submit_button("Registrarse")

            if submit_registro:
                if not nuevo_usuario.strip():
                    st.error("⚠️ El nombre de usuario no puede estar vacío.")
                elif not nueva_contrasena.strip():
                    st.error("⚠️ La contraseña no puede estar vacía.")
                elif nueva_contrasena != confirmar_contrasena:
                    st.error("⚠️ Las contraseñas no coinciden.")
                else:
                    ok, msg = logopeda_service.registrar_logopeda(nuevo_usuario, nueva_contrasena)
                    if ok:
                        st.success(f"Usuario {nuevo_usuario} registrado con éxito")
                        st.session_state.modo_login = None
                        st.session_state.pantalla = 1
                    else:
                        st.error(msg)
