import random

class Osos:
    def __init__(self):
        self.nombre = "osos"

class Peces:
    def __init__(self):
        self.nombre = "peces"

class NoneObjecto:
    def __init__(self):
        self.nombre = "none"

def mover_rio(rio):
    for i in reversed(range(len(rio))):
        if isinstance(rio[i], (Osos, Peces)):
            mover = random.choice([True, False])
            if mover:
                if i < len(rio) - 1 and isinstance(rio[i+1], NoneObjecto):
                    rio[i], rio[i+1] = rio[i+1], rio[i]

rio = []

for _ in range(10):
    ecosistema = random.choice([Osos,Peces, NoneObjecto()])
    rio.append(ecosistema)

print("Primera lista:")
for elemento in rio:
    print(elemento.nombre, end=' ')
print()

mover_rio(rio)

print("Segunda lista:")
for elemento in rio:
    print(elemento.nombre, end=' ')
print()
