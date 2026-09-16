# Funciones reutilizables para construir la galería — Semana 3, El Metaverso 2026-II
#
# Por que en un archivo .py y no en una celda del cuaderno: una funcion que se usa en mas
# de un lugar (o que se reutilizaria con otra escena) se mantiene mejor en un archivo
# editado fuera del navegador.


def crear_obra(nombre, artista, posicion, sala, año, visible=True):
    assert isinstance(nombre, str) and nombre, "el nombre debe ser un texto no vacio"
    assert isinstance(artista, str) and artista, "el artista debe ser un texto no vacio"
    assert len(posicion) == 3, "la posicion debe tener exactamente 3 coordenadas (x, y, z)"
    assert isinstance(año, int), "el año debe ser un numero entero"
    return {
        "nombre": nombre,
        "artista": artista,
        "posicion": posicion,
        "sala": sala,
        "año": año,
        "visible": visible,
    }


def crear_sala_segura(nombre, obras=None):
    if obras is None:
        obras = []
    return {"nombre": nombre, "obras": obras}



# Escriba aqui, usted mismo, la funcion agregar_obra_a_sala(sala, obra) que pide la
# seccion "Agrupar la galeria en salas" del cuaderno escena_con_funciones.ipynb.
def agregar_obra_a_sala(sala, obra):
    sala["obras"].append(obra["nombre"])
    return sala