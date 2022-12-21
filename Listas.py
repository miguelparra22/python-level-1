numbers = [1,2,3,4]
print(numbers)
print(type(numbers))


task = ["barrer", "lavar platos"]
print(task)


types = [1, True, 'hola']

task[0] = 'ver capacitacion'

print(task)

"""
metodos con listas

"""

numbers = [1,2,3,4,5]
print(numbers)
numbers.append(7)  #Agrega un nuevo elemento al final
print(numbers)

numbers.insert(0, 'Miguel')  #Agrega y toma como parametro la posicion y valor.
print(numbers)
numbers.insert(-1, "Angel")
print(numbers)



tasks = ["todo1", "todo2"]

new_list = numbers + tasks


print(new_list) #imprime la lista fucionada

#Busqueda


print(new_list.index('todo1'))
index = new_list.index('todo1')
new_list[index] = 'tarea cambiada'
print(new_list)
      
      
#Remover valors


new_list.remove('todo2')
print(new_list)


#pop elimina el ultimo elemento por defecto o parametrizo la posicion

new_list.pop()
print(new_list)


new_list.pop(0)
print(new_list)


new_list.reverse()
print(new_list)



numeros = [1,7,5,6]

numeros.sort()
print(numeros)


cadenas = ['re', 'a' ,'bs']

cadenas.sort()
print(cadenas)



#si hay tipos mezclados no puede ordenar el metodo sort



letters = ['A', 'B', 'C', 'D', 'E', 'F']

# Escribe tu solución 👇


letters.append('G')
letters.insert(0, 'Z')
letters.pop(3)

print(letters)