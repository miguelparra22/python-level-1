my_dict = {}
print(type(my_dict))


my_dict = {
    'name': 'Miguel',
    'last_name': 'Orjuela',
    'age': 22
}

print(my_dict)
print(len(my_dict))

print(my_dict['age'])
print(my_dict.get('name'))
print(my_dict.get('valorquenoexiste'))


print('last_name' in my_dict)


person = {
    'name': 'nico'
}