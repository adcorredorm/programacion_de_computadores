### Diferentes formas de definir la función que calcula el área de un círculo en Python

radio = 1

def area_circulo(r: float) -> float:
    return 3.14159265 * r**2

print(area_circulo(radio))

#####
import math
def area_circulo(r):
    area = math.pi * r * r
    return area

print(area_circulo(radio))

#####
from math import pi as PI

def area_circulo(r):
    return PI * r**2

print(area_circulo(radio))

#####
area_circulo = lambda r: math.pi * r**2
print(area_circulo(radio))
