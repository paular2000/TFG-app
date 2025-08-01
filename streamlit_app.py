import streamlit as st
from datetime import datetime

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

#--------------------------------------------
#Conexion con la BD
service_account_info = st.secrets["service_account"]


credentials = ServiceAccountCredentials.from_json_keyfile_dict(
    service_account_info,
    scopes=["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
)

client = gspread.authorize(credentials)
sheet = client.open("Base de datos 1.0").sheet1
#----------------------------------------------


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
        
        nombre = st.text_input("Nombre")
        apellidos = st.text_input("Apellidos")


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
        
        #------------
        # Selectboxes
        profesiones = ["Escoger opción","Jardinero", "Profesor"]
        estudios = ["Escoger opción","Primaria", "Secundaria", "Bachillerato", "Grado", "Master", "Doctorado"]
        aficiones = ["Escoger opción","Música", "Deportes", "Lectura"]
        
        st.markdown("#### Otros datos")
        profesionSB = st.selectbox("Elija su profesión:", profesiones)

        estudiosSB = st.selectbox("Elija su nivel de estudios:", estudios)

        aficionesSB = st.selectbox("Elija sus aficiones:", aficiones)

        submit = st.form_submit_button("Siguiente")

        if submit:
            campos_obligatorios = [nombre, apellidos, profesionSB, estudiosSB, aficionesSB]

            if all(campos_obligatorios) and \
            profesionSB != "Escoger opción" and \
            estudiosSB != "Escoger opción" and \
            aficionesSB != "Escoger opción":
                try:
                    fecha_nacimiento = datetime(anio, meses.index(mes_nombre) + 1, dia)
                    st.session_state.datos_paciente = {
                        "nombre": nombre,
                        "apellidos": apellidos,
                        "fecha_nacimiento": fecha_nacimiento.strftime("%d/%m/%Y"),
                        "profesion": profesionSB,
                        "estudios": estudiosSB,
                        "aficiones": aficionesSB
                    }

                    #-----
                    #Ingresar paciente



                    siguiente_pantalla()
                except ValueError:
                    st.error("⚠️ Fecha inválida.")
            else:
                st.warning("⚠️ Se deben completar todos los campos obligatorios.")

    


# ------------------------
# PANTALLA 2: Resultados del test BETA
# ------------------------
elif st.session_state.pantalla == 2:
    st.title("Resultados del test BETA")

    with st.form(key="resultados_form"):
      st.markdown("#### Bloque I: Comprensión oral")
      resultado_T1= st.number_input("Discriminación de fonemas: ", min_value=0, max_value=32, 
                              value=0) 
      resultado_T2= st.number_input("Decisión léxica auditiva: ", min_value=0, max_value=32, 
                              value=0) 
      resultado_T3= st.number_input("Emparejamiento palabra hablada- dibujo: ", min_value=0, max_value=30, 
                              value=0) 
      resultado_T4= st.number_input("Repetición de palabras: ", min_value=0, max_value=32, 
                              value=0) 
      resultado_T5= st.number_input("Repetición de pseudopalabras: ", min_value=0, max_value=30, 
                              value=0) 

      st.markdown("#### Bloque II: Producción oral") 
      resultado_T6= st.number_input("Denominación de objetos: ", min_value=0, max_value=30, 
                              value=0) 
      resultado_T7= st.number_input("Denominación de acciones: ", min_value=0, max_value=30, 
                              value=0) 
      resultado_T8= st.number_input("Nombrar a definiciones: ", min_value=0, max_value=30, 
                              value=0) 
      resultado_T9= st.number_input("Fluidez verbal: ", min_value=0, max_value=40, 
                              value=0) 
      resultado_T10= st.number_input("Fluidez verbal de personajes: ", min_value=0, max_value=20, 
                              value=0) 
      
      st.markdown("#### Bloque III: Lectura") 
      resultado_T11= st.number_input("Nombrado de letras: ", min_value=0, max_value=20, 
                              value=0) 
      resultado_T12= st.number_input("Decisión léxica visual: ", min_value=0, max_value=32, 
                              value=0) 
      resultado_T13= st.number_input("Lectura de palabras: ", min_value=0, max_value=32, 
                              value=0) 
      resultado_T14= st.number_input("Lectura de pseudopalabras: ", min_value=0, max_value=30, 
                              value=0) 
      resultado_T15= st.number_input("Emparejamiento palabra escrita- dibujo: ", min_value=0, max_value=30, 
                              value=0) 
      
      st.markdown("#### Bloque IV: Escritura") 
      resultado_T16= st.number_input("Señalar la letra: ", min_value=0, max_value=20, 
                              value=0) 
      resultado_T17= st.number_input("Copia de mayúscula a minúscula: ", min_value=0, max_value=8, 
                              value=0) 
      resultado_T18= st.number_input("Denominación escrita de dibujos: ", min_value=0, max_value=10, 
                              value=0) 
      resultado_T19= st.number_input("Dictado de palabras de ortografía arbitraria: ", min_value=0, max_value=10, 
                              value=0) 
      resultado_T20= st.number_input("Dictado de pseudopalabras: ", min_value=0, max_value=10, 
                              value=0) 
      
      st.markdown("#### Bloque V: Semántica") 
      resultado_T21= st.number_input("Asociación semántica: ", min_value=0, max_value=30, 
                              value=0) 
      resultado_T22= st.number_input("Emparejamiento objeto- acción: ", min_value=0, max_value=30, 
                              value=0) 
      resultado_T23= st.number_input("Emparejamiento definición- palabra: ", min_value=0, max_value=30, 
                              value=0) 
      resultado_T24= st.number_input("Emparejamiento de sinónimos: ", min_value=0, max_value=30, 
                              value=0) 
      resultado_T25= st.number_input("Señalar el diferente: ", min_value=0, max_value=30, 
                              value=0) 
      
      st.markdown("#### Bloque VI: Oraciones") 
      resultado_T26= st.number_input("Emparejamiento oración hablada- dibujo: ", min_value=0, max_value=20, 
                              value=0) 
      resultado_T27= st.number_input("Emparejamiento oración escrita- dibujo: ", min_value=0, max_value=20, 
                              value=0) 
      resultado_T28= st.number_input("Juicios de gramaticalidad: ", min_value=0, max_value=40, 
                              value=0) 
      resultado_T29= st.number_input("Prueba de dígitos: ", min_value=0, max_value=7, 
                              value=0) 
      resultado_T30= st.number_input("Descripción de una lámina: ", min_value=0, max_value=10, 
                              value=0) 

