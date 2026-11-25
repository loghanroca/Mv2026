# Hosts entre dos enlaces troncales — app interactiva

**URL pública:** https://app-loghan.onrender.com/
**Repositorio:** https://github.com/loghanroca/Mv2026

> La app corre en un plan gratuito: si nadie la ha abierto en 15 minutos, la primera carga tarda cerca de 1 minuto.

## Pregunta y usuario

La app responde: ¿qué regla de reasignación reparte mejor los equipos (hosts) de un laboratorio entre los dos enlaces troncales de un switch? Es para estudiantes de Ingeniería Informática y Ciberseguridad que quieren ver cómo se desbalancea la carga de una red y qué regla la corrige, sin tocar la red física del campus ni arriesgar equipos. El modelo es una versión simple de mi proyecto de rack de comunicaciones en 3D.

## Cómo usar la app

Hay tres controles: **Semilla** (un número entero que se escribe; fija todo el azar, así que la misma semilla da siempre lo mismo), **Hosts** (cuántos equipos hay, de 6 a 60) y **Regla** (Mi regla, Seguir a la multitud o Decisión aprendida). El gráfico muestra el desbalance paso a paso en una corrida, con la línea base punteada (nadie se reasigna). Debajo, **Promedio en 10 semillas** es cuántos hosts de diferencia quedan entre los dos enlaces al final, promediado sobre 10 semillas seguidas desde la elegida: 0 es el reparto perfecto, y siempre se lee junto a la línea base. La última línea muestra la exactitud en prueba de la decisión aprendida contra su línea base.

## Resultados

Con la semilla de inicio **25092004** y **24 hosts** (promedio del desbalance final en las semillas 25092004 a 25092013):

| Regla | Promedio en 10 semillas |
|---|---|
| Línea base (nadie se reasigna) | 7.4 |
| Mi regla | 0.0 |
| Seguir a la multitud | 24.0 |
| Decisión aprendida | 0.0 |

Decisión aprendida: exactitud en prueba **0.902** contra **0.519** de su línea base (`DummyClassifier`, que responde siempre lo más frecuente).

**Conclusión:** con estas semillas, Mi regla y la decisión aprendida dejan los dos enlaces perfectamente repartidos (0.0), mejor que la línea base (7.4). Seguir a la multitud empeora la situación: 24.0 significa que los 24 hosts terminan en un solo enlace, el peor desbalance posible, porque cada host se va al enlace más cargado. Que la decisión aprendida iguale a Mi regla no es sorpresa: el árbol se entrenó para imitarla, así que no la supera.

## Limitaciones

1. El modelo es una simplificación del mundo real: todos los hosts generan la misma carga, cada uno conoce al instante cuántos hosts hay en cada enlace, y no existen VLANs, tabla MAC ni tráfico real. Solo se reparten equipos entre dos enlaces, así que no sirve para predecir el comportamiento de una red de verdad.
2. La decisión aprendida se entrena con datos sintéticos que yo mismo generé siguiendo mi regla con un 10 % de errores. Su exactitud de 0.902 solo mide qué tan bien imita esa regla (no si reparte mejor la carga) y el árbol solo es válido para entre 6 y 60 hosts, el mundo donde se entrenó.
3. Cada corrida dura 30 pasos y la métrica usa solo 10 semillas, por lo que el promedio cambia un poco si se elige otra semilla de inicio.

## Cómo funciona por dentro

- **La regla** (`mi_regla.py`): Cada host mira cuántos hosts hay en su enlace (`mi`, contándose a sí mismo) y cuántos en el otro (`otra`). Si su enlace tiene más hosts que el otro, se reasigna al otro; si no, se queda. Cada reasignación le cuesta un intento y empieza con 10. Es una regla local: el host no ve el desbalance total, solo compara su enlace con el otro.
- **La métrica** (`metrica` en `app.py`): Mide el desbalance final, que es la diferencia absoluta de hosts entre los dos enlaces después de 30 pasos. Una sola corrida puede engañar por el azar de la distribución inicial, así que `metrica` promedia el desbalance final en 10 semillas seguidas, empezando por la elegida. Siempre se compara con la línea base, la misma simulación donde nadie se reasigna. El mejor valor posible es 0.
- **El entrenamiento** (`decision_aprendida.py`): Genero 10 000 situaciones (hosts en mi enlace, en el otro e intentos) con la decisión que tomaría un host que sigue mi regla pero se equivoca el 10 % de las veces. Separo 70 % para entrenar un árbol de decisión de profundidad 6 y 30 % para probarlo, con la semilla 7 fija. La exactitud se mide solo en el 30 % de prueba y se compara con un `DummyClassifier` que responde siempre la clase más frecuente. El árbol entrenado se usa en la app como una regla más.

## Uso de IA

Usé Claude (Anthropic) para corregir errores en el código y, en esta entrega final, para adaptar los archivos del modelo al tema de redes (hosts y enlaces troncales en lugar de visitantes y salas) y redactar un borrador del README. Respondo por el código y por lo que explica este documento.

## Cómo correrla localmente

En Anaconda Prompt, dentro de la carpeta del proyecto:

```
conda activate mv2026
solara run app.py
```

Se abre `http://localhost:8765`. **Ctrl+C** la detiene. Las versiones exactas están en `requirements.txt`.

## Licencia

Código abierto bajo licencia MIT (archivo `LICENSE`).
