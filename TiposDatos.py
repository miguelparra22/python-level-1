"""
En este archivo veremos los tipos de datos.
para ver un tipo de dato podemos usar el método type.
"""



"""
Tipos de datos
"""

#Int
age = 22
print(type(age))

#Bolean
is_single = True
print(type(is_single))

#String
name = "Miguel"
print(type(name))


"""
STRINGS

"""
last_name= "Orjuela"
full_name = name +" "+last_name

print(full_name)


#formatos

template = "Hola, mi nombre es  " + full_name 

print('v1',template)

template = "Hola mi nombre es {} y mi apellido es {}".format(name, last_name)

print('v2', template)


template = f"Hola mi nombre es {name}"

print('v3', template)



"""
Numbers

"""

vidas =  1


#float
temperatura = 34.5
print(type(temperatura))



"""
Boleeans
"""

is_single = True


#not invierte el valor del boleean
print(not is_single)
