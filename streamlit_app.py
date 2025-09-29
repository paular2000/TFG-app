
import streamlit as st

from ui import pantalla_logopeda







def main():

    if "pantalla" not in st.session_state:
        st.session_state.pantalla = 1
    

    if st.session_state.pantalla == 1:
        pantalla_logopeda.pantalla_logopeda()


if __name__ == "__main__":
    main()