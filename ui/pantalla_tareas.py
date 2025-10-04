
import streamlit as st

from services import paciente_service



def pantalla_resultados():

    
    

    
    
    with st.form(key="resultados_form"):

        st.title("Resultados del test BETA")

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
        

        boton_enviar = st.form_submit_button("Guardar resultados")

        if boton_enviar:
            
            resultados = {
                "T1": resultado_T1,
                "T2": resultado_T2,
                "T3": resultado_T3,
                "T4": resultado_T4,
                "T5": resultado_T5,
                "T6": resultado_T6,
                "T7": resultado_T7,
                "T8": resultado_T8,
                "T9": resultado_T9,
                "T10": resultado_T10,
                "T11": resultado_T11,
                "T12": resultado_T12,
                "T13": resultado_T13,
                "T14": resultado_T14,
                "T15": resultado_T15,
                "T16": resultado_T16,
                "T17": resultado_T17,
                "T18": resultado_T18,
                "T19": resultado_T19,
                "T20": resultado_T20,
                "T21": resultado_T21,
                "T22": resultado_T22,
                "T23": resultado_T23,
                "T24": resultado_T24,
                "T25": resultado_T25,
                "T26": resultado_T26,
                "T27": resultado_T27,
                "T28": resultado_T28,
                "T29": resultado_T29,
                "T30": resultado_T30
            }

            exito, mensaje = paciente_service.actualizar_resultados_tareas(
                st.session_state.get("id_paciente"),
                resultados
            )

            if exito:
                st.success(mensaje)
                st.session_state.pantalla = 1
                st.rerun()
            else:
                st.error(mensaje)