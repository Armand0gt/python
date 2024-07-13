####Datos enteros, flotantes, boleanos#####

x = 10
y = 5.678
#z = 1.2E6
#a = 1.2E-10
print(type(x))
print(type(y))
#print(type(z))
#print(type(a))
print(x+y)
print(x+x)
print(y+y)

#Boleanos
is_true = True
is_falase = False
print(is_true)
print(type(is_falase))

#Use de sep, separa parametros antes de imprimir
print("Nunca", "pares", "de", "aprender", sep=", ")

#El parámetro end cambia lo que se imprime al final de la llamada a print. En lugar de imprimir cada
#  mensaje en una nueva línea, end="" asegura que “Nunca” y “pares” se impriman en la misma línea, 
# resultando en “Nunca pares”. Por defecto, end es un salto de línea ("\n"), 
# lo que hace que cada llamada a print comience en una nueva línea.
print("Nunca", end=" ")
print("pares de aprender")


frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase:", frase, "Autor:", author)

