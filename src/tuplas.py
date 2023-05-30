print('Este es el archivo de Tuplas!!!')

numbers = (1, 2, 3, 4)

strings = ('thiago', 'nico', 'guada', 'thiago')
print(numbers)
print('0 =>', numbers[0])
print('final =>', numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

# CRUD

print(strings)
print('En que posicion esta nico =>',strings.index('nico'))
print('Veces que se repite "thiago" =>',strings.count('thiago'))

my_list = list(strings)
print(my_list)
print(type(my_list))

my_list[1] = 'joel'
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))