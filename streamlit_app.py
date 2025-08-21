import streamlit as st
from pantallas import pantalla_login, pantalla_registro, pantalla_resultados

st.set_page_config(page_title="Formulario Paciente", page_icon="📝")

if 'pantalla' not in st.session_state:
    st.session_state.pantalla = 0

if st.session_state.pantalla == 0:
    pantalla_login()
elif st.session_state.pantalla == 1:
    pantalla_registro()
elif st.session_state.pantalla == 2:
    pantalla_resultados()
