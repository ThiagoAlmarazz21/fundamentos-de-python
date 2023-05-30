print('Este es el archivo de Metodos de listas!!!')

numbers = [1, 2, 3, 4, 5]
print(numbers[1])
numbers[-1] = 10
print(numbers)

# METODO append(): añade un ítem al final de la lista
numbers.append(11)
print(numbers)

# METODO insert(): agrega un ítem a la lista en un índice específico
numbers.insert(0, '0')
print(numbers)
numbers.insert(5, '5')
print(numbers)

# FUSION DE LISTAS
tasks = ['lavarme los dientes', 'hacer la cama', 'hacerme un cafe']
new_list = numbers + tasks
print('FUSION DE LISTAS:')
print(new_list)

# METODO index(): Devuelve el índice en el que aparece un ítem (error si no aparece).
index = new_list.index('hacer la cama')
new_list[9] = 'abrir las ventanas'
print(new_list)

# METODOS DELETE

# METODO remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.
new_list.remove('lavarme los dientes')
print(new_list)

# METODO pop(): Extrae un ítem de la lista y lo borra.
new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)

# METODO reverse(): le da vuelta a la lista
print('METODO REVERSE:')
new_list.reverse()
print(new_list)

# METODO sort(): ordena el array de menor a mayor
print('METODO SORT:')
numbers_a = [1, 4, 6, 3]
print(numbers_a)
numbers_a.sort()
print(numbers_a)

strings = ['re', 'ab', 'ed']
print(strings)
strings.sort()
print(strings)