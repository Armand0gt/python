numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers[2])
information = {"nombre": "Ronaldo",
                "Apellido": "Rodriguez", 
                "Altura": 1.70,
                "Edad":31}
print(information)
del information ["Edad"]
print(information)
claves = information.keys()
print(type(claves))
values = information.values()
print(values)
