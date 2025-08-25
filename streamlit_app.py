import streamlit as st
from bd import inicializar_BD, inicializar_logopedas
from pantallas import pantalla_login, pantalla_registro, pantalla_resultados


if 'pantalla' not in st.session_state:

    #Inicializo las BD
    inicializar_BD()
    inicializar_logopedas

    st.session_state.pantalla = 0

if st.session_state.pantalla == 0:
    pantalla_login()
elif st.session_state.pantalla == 1:
    pantalla_registro()
elif st.session_state.pantalla == 2:
    pantalla_resultados()
