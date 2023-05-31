print('Este es el archivo de FOR!!!')
print('---' * 15)

# for element in range(1, 21):
#   print(element)


gatos = ['mishi', 'ysy', 'pelusa']
for gato in gatos:
  print(gato)

print('---' * 15)

my_list = [23, 45, 67, 89, 43]
for num in my_list:
  print(num)

print('---' * 15)

my_tuple = ('thiago', 'almaraz', 'daniel', 'guada')
for name in my_tuple:
  print(name)

print('---' * 15)

product = {
  'name': 'Remera',
  'price': 500,
  'stock': 85,
}
for key in product:
  print(key,'=>',product[key])

print('---' * 15)

for key, value in product.items():
  print(key, '=>', value)

people = [
  {
    'name': 'thiago',
    'age': 19
  },
  {
    'name': 'guada',
    'age': 17
  },
  {
    'name': 'joel',
    'age': 19
  }
]

print('---' * 15)

for person in people:
  print('name =>',person['name'])
  print('age =>',person['age'])
  print('---' * 15)

print('---' * 15)

zoo = {
  'Leon': 8,
  'Jirafa': 4,
  'Hipopotamo': 10,
  'Mono': 7,
}

for animal, cantitad in zoo.items():
  print(f'En el zoologico tenemos el/la {animal} con una poblacion de {cantitad}')