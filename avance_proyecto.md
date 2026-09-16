# Avance del proyecto — idea y necesidad

**Nombre(s):** Loghan Rojas Castro

**Dominio elegido (libre, cotidiano, NO relacionado con salud pública, epidemiología ni ningún
dominio profesional del docente):** Redes de comunicación y servicios TI

---

## 1. La experiencia

En 2–3 frases, describa **qué es** el entorno inmersivo que quiere construir durante el semestre.
No hace falta tenerlo resuelto técnicamente — hoy es una idea, no una escena terminada.

> Ejemplos para pensar, **no para copiar**: un recorrido virtual de un taller de mecánica para
> mostrarle a un cliente un repuesto antes de pedirlo; una sala de ensayo virtual para una banda
> que no siempre puede reunirse; un mapa 3D de una feria de emprendedores. El dominio es suyo.

Un rack de comunicaciones interactivo en 3D que contiene routers, switches administrables y patch panels. Permite visualizar no solo la distribución física del cableado, sino también la lógica de la red: asignación de VLANs codificada por colores, estado de las interfaces (LEDs en verde, amarillo o rojo) y el flujo de paquetes recorriendo los puertos.

## 2. La necesidad

¿Qué **problema real** resuelve, o qué decisión ayuda a tomar? Un entorno inmersivo "porque se ve
bien" no basta — tiene que existir **para algo**. Complete la frase:

> "Esta experiencia existe para que [quién] pueda [qué], sin tener que [qué evita]."

Esta experiencia existe para que estudiantes de Ingeniería Informática para que puedan comprender la correlación directa entre la topología física (puertos/cables) y la configuración lógica (VLANs, enrutamiento y la tabla MAC), sin tener que desconectar la red física de los laboratorios del campus ni arriesgar equipos costosos por malas conexiones.

## 3. Quién la usa

¿Quién entra a esta experiencia? Una persona, un tipo de usuario concreto — no "todo el mundo".

Estudiantes de Ingenieria Informatica y Ciberseguridad

## 4. Primer boceto de la escena

En una lista corta (3–6 líneas), los objetos que tendría la primera versión de esta escena y,
si ya lo tiene claro, una posición aproximada `(x, y, z)` para cada uno — no hace falta que sea
exacta, es un boceto, no las coordenadas finales.

| Objeto | Posición aproximada `(x, y, z)` | Para qué está ahí |
|---|---|---|
|Bastidor |0.0 1.2 -2.5 |Estructura principal de montaje del equipamiento. |
|Router Principal |0.0 1.8 -2.4 | Administrar el enrutamiento inter-VLAN y salida a red exterior|
|Switch Administrable| 0.0 1.4 -2.4| Conmutación de paquetes y segmentación por VLANs|
|Patch Panel de Distribución |0.0 1.0 -2.4| Conectar y organizar las líneas provenientes de los clientes |
|LEDs de estado de puertos |-0.6 1.4 -2.3| Indicar estado del enlace (Verde = Activo, Rojo = Caído/Falla).|
|Paquete de tráfico IP |0.0 1.2 -2.0| Simular el recorrido visible de una trama desde el puerto origen al destino|

## 5. Qué le falta todavía

Sea honesto: ¿qué parte de esta idea **no sabe todavía** cómo construir con lo que ha visto en el
curso? (Está bien no saberlo — apenas es la semana 4. Esto ayuda a planear las semanas siguientes.)

Aprender a cambiar dinámicamente los colores de los objetos (a-sphere y materiales) mediante código al simular un cambio de estado en la red (por ejemplo, cuando se cae un puerto o se reasigna una VLAN), y trazar la animación del paquete a lo largo de las trayectorias de los cables.

---

> Este avance **no** se evalúa por qué tan ambicioso sea el mundo, sino por qué tan clara es la
> **necesidad** que justifica construirlo. La escena base real (ya con numpy y glTF) se consolida
> la **semana 5**; hoy solo se pide la idea, por escrito, y que se sostenga ante la pregunta "¿para
> qué sirve esto?".
