
import streamlit as st

from ui import login, pantalla_logopeda




def main():

    if "pantalla" not in st.session_state:
        st.session_state.pantalla = 0

    if st.session_state.pantalla == 0:
        login.pantalla_login()
    if st.session_state.pantalla == 1:
        pantalla_logopeda.pantalla_logopeda()
    

if __name__ == "__main__":
    main()