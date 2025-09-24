import streamlit as st
from core.services.paciente_service import PacienteService

def pantalla_resultados(paciente_service: PacienteService):
    st.set_page_config(page_title="Formulario tareas", page_icon="📝")
    st.title("Resultados del test BETA")

    with st.form(key="resultados_form"):
        # Bloques
        bloques = {
            "Bloque I: Comprensión oral": [
                "Discriminación de fonemas", "Decisión léxica auditiva",
                "Emparejamiento palabra hablada- dibujo", "Repetición de palabras",
                "Repetición de pseudopalabras"
            ],
            "Bloque II: Producción oral": [
                "Denominación de objetos", "Denominación de acciones", "Nombrar a definiciones",
                "Fluidez verbal", "Fluidez verbal de personajes"
            ],
            "Bloque III: Lectura": [
                "Nombrado de letras", "Decisión léxica visual", "Lectura de palabras",
                "Lectura de pseudopalabras", "Emparejamiento palabra escrita- dibujo"
            ],
            "Bloque IV: Escritura": [
                "Señalar la letra", "Copia de mayúscula a minúscula", "Denominación escrita de dibujos",
                "Dictado de palabras de ortografía arbitraria", "Dictado de pseudopalabras"
            ],
            "Bloque V: Semántica": [
                "Asociación semántica", "Emparejamiento objeto- acción", "Emparejamiento definición- palabra",
                "Emparejamiento de sinónimos", "Señalar el diferente"
            ],
            "Bloque VI: Oraciones": [
                "Emparejamiento oración hablada- dibujo", "Emparejamiento oración escrita- dibujo",
                "Juicios de gramaticalidad", "Prueba de dígitos", "Descripción de una lámina"
            ]
        }

        resultados_inputs = []
        for bloque_nombre, tareas in bloques.items():
            st.markdown(f"#### {bloque_nombre}")
            for tarea in tareas:
                val = st.number_input(tarea, min_value=0, max_value=40, value=0)
                resultados_inputs.append(val)

        submit = st.form_submit_button("Guardar resultados")

        if submit:
            if 'id_paciente' in st.session_state:
                resultados = {f"T{i+1}": val for i, val in enumerate(resultados_inputs)}
                paciente_service.guardar_resultados(st.session_state.id_paciente, resultados)
                st.success("✅ Resultados guardados correctamente.")
            else:
                st.error("❌ No se ha registrado el paciente.")
