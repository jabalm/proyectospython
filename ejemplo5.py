#problema: leer un numero entero de 2 digitos y muestrelo al reves
#ejemplo: 21 --> 12

#SOLUCIÓN
#variable de entrada
num = int(input("Ingrese Numero de 2 digitos: "))
#variables de operaciones
uni = int(num / 10)
dec = num % 10
ni = dec * 10 + uni
#variables de salida
print("Numero invertido:", ni)

