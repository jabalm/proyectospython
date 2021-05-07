#Programa: Hallar el volumen de una esfera
#formula: V = 4/3.π.r³

#SOLUCIÓN
import math
#var de entrada
radio = float(input("Ingrese radio: "))
#var de operación
ve = 4/3 * math.pi * math.pow(radio, 3)
#var de salida
print("Volumen de la esfera:",ve)
