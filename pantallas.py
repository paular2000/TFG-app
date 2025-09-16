import streamlit as st
from datetime import datetime
from bd import get_pacientes, ingresar_paciente, guardar_resultados_tareas, registrar_logopeda, validar_logopeda


# ---------------
# Logeo Logopedas
# ---------------

def pantalla_login():

    st.set_page_config(page_title="Inicio sesión", page_icon="✅")

    st.title("DURAGUI")
    st.write("Por favor, inicie sesión o regístrese.")

    if "modo_login" not in st.session_state:
        st.session_state.modo_login = None
    
    # Botones principales
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Iniciar Sesión"):
            st.session_state.modo_login = "login"
    with col2:
        if st.button("Registrarse"):
            st.session_state.modo_login = "registro"


    # FORMULARIO DE LOGIN
    if st.session_state.modo_login == "login":
        st.subheader("Iniciar Sesión")
        with st.form("form_login"):
            usuario = st.text_input("Usuario")
            contrasena = st.text_input("Contraseña", type="password")
            submit_login = st.form_submit_button("Entrar")

            if submit_login:
                ok, result = validar_logopeda(usuario, contrasena)
                if ok:
                    st.success("Bienvenido, "+ usuario)
                    st.session_state["id_logopeda"] = result
                    st.session_state["usuario"] = usuario
                    st.session_state["autenticado"] = True
                    st.session_state.pantalla = 1
                else:
                    st.error(result)                

    # FORMULARIO DE REGISTRO
    elif st.session_state.modo_login == "registro":
        st.subheader("Registro de nuevo logopeda")
        with st.form("form_registro"):
            nuevo_usuario = st.text_input("Nombre de usuario")
            nueva_contrasena = st.text_input("Contraseña", type="password")
            confirmar_contrasena = st.text_input("Confirmar contraseña", type="password")
            submit_registro = st.form_submit_button("Registrarse")

            if submit_registro:
                if not nuevo_usuario.strip():
                    st.error("⚠️ El nombre de usuario no puede estar vacío.")
                elif not nueva_contrasena.strip():
                    st.error("⚠️ La contraseña no puede estar vacía.")
                elif nueva_contrasena != confirmar_contrasena:
                    st.error("⚠️ Las contraseñas no coinciden.")
                else:
                    ok, msg = registrar_logopeda(nuevo_usuario, nueva_contrasena)
                    if ok:
                        st.success(msg)
                        st.session_state.modo_login = None
                        st.session_state.pantalla = 1
                    else:
                        st.error(msg)
#-----------------------------------------------------------

#-------------------------
#PAGINA PRINCIPAL DEL LOGOPEDA
#-------------------------

def pantalla_logopeda():
    st.title("Logopea (nombre logopeda)")

    


    if st.button("Ver pacientes"):
        pacientes = get_pacientes(st.session_state["id_logopeda"])

        if pacientes:
            st.subheader("Lista de pacientes")
            for paciente in pacientes:
                with st.container():
                    cols = st.columns([1,4])
                    with cols[0]:
                        if st.button("🧑", key=paciente["ID"]):
                            st.session_state.paciente_actual = paciente
                            st.session_state.pantalla = 3  # Nueva pantalla del paciente
                            st.rerun()
                    with cols[1]:
                        st.write(f"**{paciente['nombre']} {paciente['apellidos']}**")
        else:
            st.info("📭 No tienes pacientes registrados.")

    if st.button("Registrar nuevo paciente"):
        st.session_state.pantalla = 2


def pantalla_paciente():
    st.title("FUTURA PANTALLA DEL PACIENTE")

def pantalla_registro():
    st.set_page_config(page_title="Formulario Paciente", page_icon="📝")

    st.title("Formulario de registro de pacientes")
    st.write("Por favor, introduzca los datos del paciente.")
    
    with st.form(key="registro_form"):
        nombre = st.text_input("Nombre")
        apellidos = st.text_input("Apellidos")

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

        profesiones_opciones = ["Escoger una opción","Jardinero", "Profesor"]
        estudios_opciones = ["Escoger una opción","Primaria", "Secundaria", "Bachillerato", "Grado", "Master", "Doctorado"]
        aficiones_opciones = ["Música", "Deportes", "Lectura","Forjar espadas", "Fumar pipas","Canto en lenguas antiguas"]

        profesion = st.selectbox("Elija su profesión:", profesiones_opciones)
        estudios = st.selectbox("Elija su nivel de estudios:", estudios_opciones)
        aficiones = st.multiselect("Elija sus aficiones:", aficiones_opciones,placeholder="Escoger opciones")

        submit = st.form_submit_button("Siguiente")
        
        #------------------

        if submit: #si pulsar siguiente
            campos_obligatorios = [nombre, apellidos, profesion, estudios, aficiones]

            if all(campos_obligatorios) and \
               profesion != "Escoger una opción" and \
               estudios != "Escoger una opción" and \
               aficiones:
                try:
                    #calculo de la edad
                    fecha_nacimiento = datetime(anio, meses.index(mes_nombre) + 1, dia)
                    edad = int(datetime.now().year - fecha_nacimiento.year)

                    st.session_state.datos_paciente = {
                        "nombre": nombre,
                        "apellidos": apellidos,
                        "edad": edad,
                        "profesion": profesion,
                        "estudios": estudios,
                        "aficion": aficiones,
                    }
                    id_paciente = ingresar_paciente(st.session_state.datos_paciente)
                    if id_paciente:
                        st.session_state.id_paciente = id_paciente
                        st.session_state.pantalla = 4
                except ValueError:
                    st.error("⚠️ Fecha inválida.")
            else:
                st.warning("⚠️ Se deben completar todos los campos obligatorios.")

def pantalla_resultados():

    st.set_page_config(page_title="Formulario tareas", page_icon="📝")

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
        submit = st.form_submit_button("Guardar resultados")
        
        if submit:
            if 'id_paciente' in st.session_state:
                resultados_lista = [
                                    resultado_T1, resultado_T2, resultado_T3, resultado_T4, resultado_T5,
                                    resultado_T6, resultado_T7, resultado_T8, resultado_T9, resultado_T10,
                                    resultado_T11, resultado_T12, resultado_T13, resultado_T14, resultado_T15,
                                    resultado_T16, resultado_T17, resultado_T18, resultado_T19, resultado_T20,
                                    resultado_T21, resultado_T22, resultado_T23, resultado_T24, resultado_T25,
                                    resultado_T26, resultado_T27, resultado_T28, resultado_T29, resultado_T30
                                ]

                resultados = {f"T{i+1}": val for i, val in enumerate(resultados_lista)}
                guardar_resultados_tareas(st.session_state.id_paciente, resultados) 
            else:
                st.error("❌ No se ha registrado el paciente.")

