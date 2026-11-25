# mi_regla.py — mi regla de decisión para el host
def regla_mia(mi, otra, intentos):
    # mi = hosts en mi enlace, otra = hosts en el otro enlace, intentos = reasignaciones que me quedan
    # Me paso al otro enlace solo si el mío tiene más hosts (así se busca igualar la carga).
    return mi > otra
