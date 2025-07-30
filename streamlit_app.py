import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Formulario Paciente", page_icon="📝")
if 'pantalla' not in st.session_state:
    st.session_state.pantalla = 1

def siguiente_pantalla():
    st.session_state.pantalla = 2


# ------------------------
# PANTALLA 1: Formulario del paciente
# ------------------------
if st.session_state.pantalla == 1:
    st.title("Formulario de registro de pacientes")
    st.write("Por favor, introduzca los datos del paciente.")

    with st.form(key="registro_form"):
        st.markdown("#### Nombre")
        #se queda un espacio. REVISAR
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

        submit = st.form_submit_button("Siguiente")

        if submit:
            if nombre and mes_nombre and profesion:
                try:
                    fecha_nacimiento = datetime(anio, meses.index(mes_nombre) + 1, dia)
                    st.session_state.datos_paciente = {
                        "nombre": nombre,
                        "fecha_nacimiento": fecha_nacimiento.strftime("%d/%m/%Y"),
                        "profesion": profesion
                    }
                    siguiente_pantalla()
                except ValueError:
                    st.error("La fecha introducida no es válida.")
            else:
                st.warning("Por favor, complete todos los campos.")

# ------------------------
# PANTALLA 2: Resultados del test BETA
# ------------------------
elif st.session_state.pantalla == 2:
    st.title("Resultados del test BETA")

    with st.form(key="resultados_form"):
      st.markdown("#### Bloque I: Comprensión oral")
      resultado_T1= st.slider("Discriminación de fonemas: ", min_value=0, max_value=32, 
                              value=0, step=1) 



      st.markdown("#### Bloque II: Producción oral") 

