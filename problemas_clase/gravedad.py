### Programa que calcula la fuerza de gravedad entre 2 cuerpos m1, m2 separados por una distancia r

G:float = 6.67384e-11

m1 = float(input("Ingrese la masa del objeto 1: "))
m2 = float(input("Ingrese la masa del objeto 2: "))
r = float(input("Ingrese la distancia entre los objetos: "))

F:float = G * (m1 * m2) / (r * r)

print("La fuerza de gravedad es:", F)
