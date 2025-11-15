

import random
from typing import List
from models.models import Paciente, EstimuloSFA
from data_base import sfa_repo


def iniciar_sesion_sfa(paciente: Paciente) -> List[EstimuloSFA]:
    """Inicia una sesión SFA para un paciente y devuelve una lista de estímulos SFA aleatorios."""
    
    # 1. Obtener todos los estímulos SFA desde el repositorio
    try:
        lista_completa_estimulos = sfa_repo.get_all_sfa_estimulos()
    except Exception as e:
        print (f"Error al obtener los estímulos SFA: {e}")
        return []
    
    # 2. Preparar las aficiones del paciente 
    aficiones_paciente = set(af.strip().lower() for af in paciente.aficiones)

    lista_filtrada_estimulos = []

    # 3. Filtrar los estímulos según las aficiones del paciente
    for estimulo in lista_completa_estimulos:
        criterio_mostrar = estimulo.mostrar.strip().lower()

        if criterio_mostrar == "Siempre":
            lista_filtrada_estimulos.append(estimulo)
        else:
            criterios_requeridos = set(c.strip().lower() for c in criterio_mostrar.split(","))

            if not aficiones_paciente.isdisjoint(criterios_requeridos):
                lista_filtrada_estimulos.append(estimulo)
    
    # 4. Barajar aleatoriamente la lista filtrada
    random.shuffle(lista_filtrada_estimulos)

    return lista_filtrada_estimulos



    
