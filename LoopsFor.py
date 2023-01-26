for element in range(1,20):
    print(element)
    
    

    
my_list = [23,45,67,89,43]
for element in my_list:
    print(element)
    
    
my_tuple = ('nico','juli', 'santi')
for element in my_tuple:
    print(element)
    
    
product = {
    'name': 'camisa',
    'price': 100,
    'stock': 89
}


for key, value in product.items():
    print(key, '=>', value)
    
    
'''
lista de diccionarios
'''

people = [
    {
        'name': 'miguel',
        'age': '22'
    },
    {
        'name': 'nata',
        'age': 21   
    }
]

for person in people:
 print('name =>', person['name'])
 
 
 matriz = [
     [1,2,3],
     [4,5,6],
     [7,8,9]
 ]
 
 #selecciona el valor de una lista de las matriz
 print(matriz[0][1])
 
 for row in matriz:
     print(row)
     for column in row:
         print(column)
         
         