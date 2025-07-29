import streamlit as st

st.title("Formulario de registro de pacientes")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
with st.form(key="registro_form"):
    nombre = st.text_input("Nombre")
    edad = st.number_input("Edad",
                            min_value= 0,
                            max_value= 100)
    profesion = st.text_input("Profesión")