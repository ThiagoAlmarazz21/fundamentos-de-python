print('Este es el archivo de While!!!')

counter = 0

while counter < 10:
  counter += 1
  print(counter)

print('---' * 10)

count = 0

while count < 20:
  count += 1
  if count == 15:
    break
  print(count)


# TABLA DE MULTIPLICAR CON CICLO WHILE
'''
contador = 0

y = int(input('Numero de la tabla: '))
x = int(input('Ingresa hasta que numero quieres multiplicar: '))

while contador < x:
  contador += 1
  resultado = y * contador
  print(f'{y} X {contador} = {resultado}')
'''

print('---' * 10)

day = 0

semana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']

while day < 7:
  print(f'Hoy es {semana[day]}')
  day += 1