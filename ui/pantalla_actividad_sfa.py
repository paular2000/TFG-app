
import streamlit as st

def pantalla_sfa(): 
    """
    Esta es la pantalla principal de la actividad SFA.
    Se redibuja en cada interacción.
    """

    lista_juego = st.session_state.get("sfa_lista_estimulos", [])
    index_actual = st.session_state.get("sfa_item_actual", 0)

    # Se comprueba si la partida ha terminado
    if not lista_juego or index_actual >= len(lista_juego):
        st.success("¡Has completado la actividad SFA!")
        st.write("Se han finalizado todos los ítems de la actividad.")

        # Se muestran los resultados
        resultados = st.session_state.get("sfa_resultados", [])
        if resultados:
            st.write("Resultados de la sesión:")
            st.dataframe(resultados)

        if st.button("Volver a la pantalla del paciente"):
            st.session_state['sfa_lista_estimulos'] = []
            st.session_state['sfa_item_actual'] = 0
            st.session_state['sfa_resultados'] = []
            st.session_state['sfa_pistas_vistas'] = []
            st.session_state.pantalla = 4  # Pantalla del paciente
            st.rerun()

        return 
    
    item_actual = lista_juego[index_actual]

    st.title("Actividad SFA")
    st.progress((index_actual + 1) / len(lista_juego),
                text=f"Estímulo {index_actual + 1} de {len(lista_juego)}")
    
    st.divider()

    col_img, col_info = st.columns([1,1])
    with col_img:
        st.subheader("Primer intento de denominación:")
        st.info("Deje que el paciente intente nombrar el objeto. Si no puede, active las pistas.")
        
        # Pista para el logopeda
        st.markdown(f"**Solución:** `{item_actual.solucion}`")
    
    st.divider()

    st.subheader("Pistas Semánticas")
    pistas_cols = st.columns(5)
    with pistas_cols[0]:
        st.button(f"Grupo", use_container_width=True, key="btn_grupo")
    with pistas_cols[1]:
        st.button(f"Uso", use_container_width=True, key="btn_uso")
    with pistas_cols[2]:
        st.button(f"Acción", use_container_width=True, key="btn_accion")
    with pistas_cols[3]:
        st.button(f"Propiedades", use_container_width=True, key="btn_propiedades")
    with pistas_cols[4]:
        st.button(f"Localización", use_container_width=True, key="btn_localizacion")

    st.divider()

    st.subheader("Registro del Logopeda")
    registro_cols = st.columns(2)
    with registro_cols[0]:
        st.button("✅ Acierto", use_container_width=True, key="btn_acierto")
    with registro_cols[1]:
        st.button("❌ Error", use_container_width=True, key="btn_error")