"""
Un granjero tiene cincuenta animales entre conejos y gallinas.
Si la cantidad de patas de los animales es 140,
¿Cuántos conejos y cuántas gallinas tiene el granjero?
"""

animales = 50
patas = 140

conejos = patas / 2 - animales
gallinas = animales - conejos

print("El número de conejos es", conejos)
print("El número de gallinas es", gallinas)
