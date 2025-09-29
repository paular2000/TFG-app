
import streamlit as st

from ui import login







def main():

    if "pantalla" not in st.session_state:
        st.session_state["pantalla"] = "login"
    
    if st.session_state["pantalla"] == "login":
        login.pantalla_login()


if __name__ == "__main__":
    main()