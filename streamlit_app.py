from ui import pantalla_login
from core.services.logopeda_service import LogopedaService
from core.services.paciente_service import PacienteService
import streamlit as st

from logopeda_repository_sheets import LogopedaRepositorySheets
from paciente_repository_sheets import PacienteRepositorySheets




# Inicializar servicios con repositorios concretos
logopeda_service = LogopedaService(LogopedaRepositorySheets("1gaOH07n1PE--QEBBkyahqnAlH5D9r5_uA7pd1UhXJdU"))
paciente_service = PacienteService(PacienteRepositorySheets("1gaOH07n1PE--QEBBkyahqnAlH5D9r5_uA7pd1UhXJdU"))


if 'pantalla' not in st.session_state:
    st.session_state.pantalla = 0
if st.session_state.pantalla == 0:
    pantalla_login(logopeda_service)

