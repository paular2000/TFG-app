
import streamlit as st

from ui import login, pantalla_logopeda, pantalla_formulario_paciente, pantalla_tareas




def main():

    if "pantalla" not in st.session_state:
        st.session_state.pantalla = 0

    if st.session_state.pantalla == 0:
        login.pantalla_login()
    if st.session_state.pantalla == 1:
        pantalla_logopeda.pantalla_logopeda()
    if st.session_state.pantalla == 2:
        pantalla_formulario_paciente.pantalla_formulario_paciente()
    if st.session_state.pantalla == 3:
        pantalla_tareas.pantalla_resultados()
        
if __name__ == "__main__":
    main()