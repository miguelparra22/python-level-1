

'''
Las variables son contenedores para almacenar valores de datos.
Para entender que son las variables podemos usar una analogía con las cajas, cada caja tiene un nombre 
dependiendo de su contenido, el contenido puede variar.
'''


x=1  #como podemos ver no debemos declarar una palabra clave para definir una variable ni tampoco el tipo de dato.
y=2

print(x+y)

#Declaracion de String
my_name = "Miguel"


"""
Hay maneras en las que una variable no se puede definir como las siguientes.

=> 2myvar = "John"
=> my-var = "John"
=> my var = "John"

"""




#El metodo input permite obtener el texto que el usuario a escrito por medio del teclado.

print("Escribe tu nombre")
nombre = input()
print( f"Bienvenido. {nombre}")


#multiples variable y asiganaciones

x,y,z = "Orange", "Banana" , "Manzana"

print(x)
print(y)
print(z)

x = y = z = "Naranja"

print(x)
print(y)
print(z)


"""
Asignacion de variables a una coleccion
"""
frutas = ["Manzana1", "Banano1", "Fresas1"]

x,y,z = frutas

print(x)
print(y)
print(z)

p = ['Mx']
p.append('h')
print(p)