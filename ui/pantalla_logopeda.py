
import streamlit as st
from services import paciente_service

def pantalla_logopeda():

    with st.sidebar:
            st.title("Menú")
            if st.button("Cerrar sesión"):
                st.session_state.pantalla = 0
                st.session_state["usuario"] = ""
                st.session_state["id_logopeda"] = ""
                st.rerun()

    
    usuario = st.session_state.get("usuario", "Usuario desconocido")
    st.title(f"Bienvenido, " +  usuario)
    
        
    st.markdown(
        f"""
        <style>
        .titulo {{
            border: 2px solid #4CAF50;
            padding: 12px;
            border-radius: 10px;
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            color: #222;
            background: #f9f9f9;
            transition: all 0.3s ease;
        }}
        .titulo:hover {{
            background: #4CAF50;
            color: white;
            cursor: pointer;
            transform: scale(1.02);
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }}
        </style>
        <div class="titulo">Bienvenido, {usuario}</div>
        """,
        unsafe_allow_html=True
    )
    
    id_logopeda = st.session_state.get("id_logopeda")
    
    st.write("Id Logopeda: " + id_logopeda)
    
    if id_logopeda:

        ok, lista_pacientes = paciente_service.obtener_pacientes_por_logopeda(id_logopeda)
        
        if ok and lista_pacientes:
            st.write("Pacientes asignados:")
            for paciente in lista_pacientes[1]:
                st.write(f"- {paciente.nombre} {paciente.apellidos}, Edad: {paciente.edad}")
        else:
            st.write("No tienes pacientes asignados.")


    
    
    
    