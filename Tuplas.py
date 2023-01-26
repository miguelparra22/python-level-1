numbers = (1,2,3,5,2)
print(' inicio de tupla =' , numbers[0])
print(' final de la tupla  =', numbers[-1])


#Las tuplas son listas inmutables. son solo de lectura


print(numbers.index(2))
print(numbers.count(2))


#pasar de tupla a lista
my_list = list(numbers)
print(type(my_list))

#pasar de lista a tupla

my_tuple = tuple(my_list)
print(type(my_tuple))


print((8/2) + 4*8)