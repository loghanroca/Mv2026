# app.py — hosts entre dos enlaces troncales de un rack: la app del proyecto final (Solara)
import solara
from matplotlib.figure import Figure
from galeria_modelo import correr, promedio_final, no_mover, seguir_multitud
from mi_regla import regla_mia
from decision_aprendida import regla_aprendida, ACC_PRUEBA, ACC_BASE

semilla = solara.reactive(25092004)     # valores que el usuario cambia con los controles;
hosts = solara.reactive(24)             # cuando uno cambia, Solara vuelve a dibujar la página
nombre_regla = solara.reactive('Mi regla')


def grafico(historia, base, n):
    # Desbalance paso a paso: la regla elegida contra la línea base.
    fig = Figure(figsize=(6, 3))
    ax = fig.subplots()
    ax.plot(base, '--', label='línea base: nadie se reasigna')
    ax.plot(historia, label=nombre_regla.value)
    ax.set_ylim(0, n)                   # eje desde 0: no exagera diferencias
    ax.set_xlabel('paso')
    ax.set_ylabel('desbalance (hosts)')
    ax.legend()
    return fig


@solara.component
def Corrida():
    # Controles + gráfico de UNA corrida (la semilla elegida).
    solara.InputInt('Semilla (escriba un entero)', value=semilla)
    solara.SliderInt('Hosts', value=hosts, min=6, max=60, step=2)
    solara.Select('Regla', value=nombre_regla, values=list(REGLAS))
    sem = int(semilla.value or 1)       # si el campo queda vacío, se usa 1
    historia = correr(REGLAS[nombre_regla.value], sem, hosts.value)
    base = correr(no_mover, sem, hosts.value)
    solara.FigureMatplotlib(grafico(historia, base, hosts.value))
    solara.Markdown(f'**Esta corrida:** desbalance final {historia[-1]} · línea base {base[-1]}')


def metrica(regla, semilla, n):
    # Desbalance final promedio en las 10 semillas que empiezan en `semilla` (Taller 15).
    return promedio_final(regla, range(semilla, semilla + 10), n)


@solara.component
def Page():
    solara.Markdown(f'## Hosts entre dos enlaces troncales\n{PREGUNTA}')   # 1. la pregunta, arriba
    Corrida()                                                      # 2. controles, gráfico, una corrida
    sem = int(semilla.value or 1)
    regla = REGLAS[nombre_regla.value]
    promedio = metrica(regla, sem, hosts.value)
    base = metrica(no_mover, sem, hosts.value)
    solara.Markdown(f'**Promedio en 10 semillas:** {promedio} · línea base {base}  \n{COMO_LEER}')
    solara.Markdown(f'*Decisión aprendida:* exactitud en prueba {ACC_PRUEBA} · línea base {ACC_BASE}')


# --- Su parte (Taller 16): el menú de reglas y los textos que guían al usuario ---
REGLAS = {'Mi regla': regla_mia, 'Seguir a la multitud': seguir_multitud,
          'Decisión aprendida': regla_aprendida}
PREGUNTA = '¿Qué regla de reasignación reparte mejor los equipos de un laboratorio entre los dos enlaces troncales de un switch? Para estudiantes de Ingeniería Informática y Ciberseguridad que quieren entender cómo se desbalancea la carga de una red sin tocar la red física del campus.'
COMO_LEER = 'El promedio es cuántos hosts de diferencia quedan entre los dos enlaces al final: 0 es el reparto perfecto. Compárelo siempre con la línea base (nadie se reasigna).'
