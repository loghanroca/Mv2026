# galeria_modelo.py — hosts repartidos entre dos enlaces troncales de un switch, como modelo de Mesa
from mesa import Agent, Model


class Host(Agent):
    # Un host (computador del laboratorio): usa un enlace troncal (0 = Troncal A, 1 = Troncal B)
    # y tiene un número limitado de reasignaciones de puerto.
    def __init__(self, model, enlace):
        super().__init__(model)
        self.enlace = enlace
        self.intentos = 10                       # reasignaciones de puerto que le quedan

    def step(self):
        mi = self.model.hosts_en(self.enlace)    # hosts en mi enlace (me incluye)
        otra = self.model.n - mi                 # hosts en el otro enlace
        if self.intentos > 0 and self.model.regla(mi, otra, self.intentos):
            self.enlace = 1 - self.enlace        # me reasigno al otro enlace
            self.intentos -= 1                   # reasignar cuesta 1 intento


class RackRed(Model):
    # El mundo: n hosts, una regla de decisión y una semilla.
    def __init__(self, regla, n=24, semilla=1):
        super().__init__(rng=semilla)            # la semilla fija todo el azar
        self.n = n
        self.regla = regla
        en_troncal_a = int(self.rng.integers(n // 4, 3 * n // 4 + 1))
        for i in range(n):
            Host(self, 0 if i < en_troncal_a else 1)
        self.historia = [self.desbalance()]      # desbalance en cada paso

    def hosts_en(self, enlace):
        return sum(1 for a in self.agents if a.enlace == enlace)

    def desbalance(self):
        return abs(self.hosts_en(0) - self.hosts_en(1))   # 0 = reparto perfecto

    def step(self):
        self.agents.shuffle_do("step")           # orden al azar, fijado por la semilla
        self.historia.append(self.desbalance())


def no_mover(mi, otra, intentos):
    return False                                 # línea base: nadie se reasigna


def seguir_multitud(mi, otra, intentos):
    return otra > mi                             # irse al enlace que ya tiene más hosts (la regla de la semana 8)


def correr(regla, semilla, n=24, pasos=30):
    # Corre una simulación completa y devuelve la historia del desbalance.
    modelo = RackRed(regla, n=n, semilla=semilla)
    for _ in range(pasos):
        modelo.step()
    return modelo.historia


def promedio_final(regla, semillas, n=24):
    # Desbalance final promedio sobre varias semillas: la métrica honesta.
    finales = [correr(regla, s, n)[-1] for s in semillas]
    return round(sum(finales) / len(finales), 2)
