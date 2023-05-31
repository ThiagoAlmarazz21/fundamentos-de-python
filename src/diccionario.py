print('Este es el archivo de Diccionarios!!!')

# [ ] = Listas
# ( ) = Tuplas
# { } = Diccionarios

my_dict = {}
print(type(my_dict))

my_dict = {
  'avion': 'objeto volador',
  'name': 'Thiago',
  'last_name': 'Almaraz',
  'age': 19
}

print(my_dict)
print('Cuantos elementos tenemos en el dict =>',len(my_dict))

print(my_dict['age'])
print(my_dict['last_name'])
# get(): maneja mejor los valores que no existen, prevenimos error y no se totea el programa
print('Un valor que no existe =>',my_dict.get('unValor')) 

print('avion' in my_dict)
print('otroqueno' in my_dict)
