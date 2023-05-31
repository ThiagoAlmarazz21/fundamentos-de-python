print('Este es el archivo de Diccionarios!!!')

person = {
  'name' : 'Thiago',
  'last_name' : 'Almaraz',
  'age' : 19,
  'langs' : ['Python', 'Javascript'],
}

print('ORIGINAL',person)
person['name'] = 'Guada'
person['age'] += 10
person['langs'].append('Rust')
print(person)

del person['last_name']
person.pop('age')
print(person)

print('ITEMS:')
print(person.items())
print('KEYS:')
print(person.keys())
print('VALUES:')
print(person.values())