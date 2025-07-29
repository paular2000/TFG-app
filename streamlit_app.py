import streamlit as st

st.title("Formulario de registro de pacientes")
st.write(
    "Por favor, introduzca los datos del paciente.")
with st.form(key="registro_form"):
    nombre = st.text_input("Nombre")
    edad = st.number_input("Edad",
                            min_value= 0,
                            max_value= 100)
    profesion = st.selectbox("Elija su profesion: ",options=["Jardinero","Profesor"])