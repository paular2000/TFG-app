import streamlit as st
from datetime import datetime

st.title("Formulario de registro de pacientes")
st.write(
    "Por favor, introduzca los datos del paciente.")
with st.form(key="registro_form"):
    st.markdown("####Nombre")
    nombre = st.text_input("")

    
    fecha_de_nacimiento = st.markdown("#### Fecha de nacimiento")
    
    dias = list(range(1, 32))
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    anios = list(range(datetime.now().year, 1900, -1))

    col1, col2, col3 = st.columns(3)

    with col1:
        dia = st.selectbox("Día", dias)

    with col2:
        mes_nombre = st.selectbox("Mes", meses)

    with col3:
        anio = st.selectbox("Año", anios)

    profesion = st.selectbox("Elija su profesión:", options=["Jardinero", "Profesor"])

    submit = st.form_submit_button("Enviar")