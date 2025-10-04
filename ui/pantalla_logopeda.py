
import streamlit as st
from services import paciente_service

def pantalla_logopeda():
    
    usuario = st.session_state.get("usuario", "Usuario desconocido")
    st.title(f"Bienvenido, " +  usuario)
    
    
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


    
    #menu hamburguesa
    st.markdown(
    """
    <style>
    .menu {
        position: fixed;
        top: 20px;
        left: 20px;
        z-index: 9999; /* Forzar a estar por encima */
    }
    .menu input { display: none; }
    .menu span {
        display: block;
        width: 30px;
        height: 4px;
        margin: 6px;
        background: #000;
        border-radius: 2px;
        transition: 0.4s;
    }
    .menu-content {
        display: none;
        background: #f5f5f5;
        padding: 12px;
        border-radius: 10px;
        margin-top: 10px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.3);
    }
    .menu input:checked ~ .menu-content {
        display: block;
    }
    .menu-content a {
        text-decoration: none;
        color: #333;
        display: block;
        margin: 8px 0;
        font-weight: 500;
    }
    .menu-content a:hover {
        color: #007bff;
    }
    </style>

    <div class="menu">
        <label>
            <input type="checkbox" id="menu-toggle"/>
            <span></span>
            <span></span>
            <span></span>
            <div class="menu-content">
                <a href="#">🏠 Inicio</a>
                <a href="#">👤 Perfil</a>
                <a href="#">📋 Pacientes</a>
            </div>
        </label>
    </div>
    """,
    unsafe_allow_html=True
)

    
        
    

    