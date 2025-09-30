
import streamlit as st

from ui import login, pantalla_logopeda, pantalla_registro_paciente







def main():

    if "pantalla" not in st.session_state:
        st.session_state.pantalla = 0
    
    if st.session_state.pantalla == 0:
        login.pantalla_login()
    elif st.session_state.pantalla == 1:
        pantalla_logopeda.pantalla_logopeda()
    elif st.session_state.pantalla == 3:
        pantalla_registro_paciente.pantalla_registro_paciente()
    

if __name__ == "__main__":
    main()