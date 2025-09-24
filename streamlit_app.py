from ui import pantalla_login, pantalla_logopeda, pantalla_paciente, pantalla_registro, pantalla_resultados
from core.services.logopeda_service import LogopedaService
from core.services.paciente_service import PacienteService
import streamlit as st


import sys
import os

# Agregar la carpeta raíz del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(__file__))


from bd.logopeda_repository_sheets import LogopedaRepositorySheets
from bd.paciente_repository_sheets import PacienteRepositorySheets




# Inicializar servicios con repositorios concretos
logopeda_service = LogopedaService(LogopedaRepositorySheets("1gaOH07n1PE--QEBBkyahqnAlH5D9r5_uA7pd1UhXJdU"))
paciente_service = PacienteService(PacienteRepositorySheets("1gaOH07n1PE--QEBBkyahqnAlH5D9r5_uA7pd1UhXJdU"))


if 'pantalla' not in st.session_state:
    st.session_state.pantalla = 0
if st.session_state.pantalla == 0:
    pantalla_login(logopeda_service)
elif st.session_state.pantalla == 1:
    pantalla_logopeda(paciente_service)
elif st.session_state.pantalla == 2:
    pantalla_registro(paciente_service)
elif st.session_state.pantalla == 3:
    pantalla_paciente(paciente_service)
elif st.session_state.pantalla == 4:
    pantalla_resultados(paciente_service)