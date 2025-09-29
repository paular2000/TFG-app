import streamlit as st
from services import logopeda_service


def pantalla_login():
    st.title("Inicio de sesión")

    opciones = st.radio("Elegir", ("Iniciar sesión", "Registrarse"))

    if opciones == "Iniciar sesión":
        st.subheader("Iniciar sesión")
        
        usuario = st.text_input("Usuario")
        contrasenia = st.text_input("Contraseña", type="password")
        if st.button("Entrar"):
            if not usuario or not contrasenia:
                st.error("❌ Por favor, complete todos los campos.")
            else:
                valido, resultado = logopeda_service.validar_logopeda(usuario, contrasenia)
                if valido:
                    st.success("✅ Bienvenido/a., {usuario}!")
                    
                else:
                    st.error(resultado)
    else:
        st.subheader("Registrarse")
        
        nuevo_usuario = st.text_input("Nuevo usuario")
        nueva_contrasenia = st.text_input("Nueva contraseña", type="password")
        confirmar_contrasenia = st.text_input("Confirmar contraseña", type="password")
        if st.button("Registrar"):
            if not nuevo_usuario or not nueva_contrasenia:
                st.error("❌ Por favor, complete todos los campos.")
            elif nueva_contrasenia != confirmar_contrasenia:
                st.error("❌ Las contraseñas no coinciden.")
            else:
                registrado, mensaje = logopeda_service.registrar_logopeda(nuevo_usuario, nueva_contrasenia)
                if registrado:
                    st.success(mensaje)
                else:
                    st.error(mensaje)